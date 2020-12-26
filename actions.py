from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from ssl import SSL_ERROR_EOF
import simple_mail
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import zomatopy
import json
import pandas as pd

ZOMATO_API_KEY = "7667690278598ab50d50f936c94bc760"

def validate_location(loc):
	tier1_cities = ["Ahmedabad", "Bengaluru", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai","Pune"]
	tier2_cities = ["Agra", "Ajmer", "Aligarh", "Amravati", "Amritsar", "Asansol", "Aurangabad", "Bareilly", "Belgaum", "Bhavnagar", "Bhiwandi", "Bhopal", "Bhubaneswar", "Bikaner", "Bilaspur", "Bokaro Steel City", "Chandigarh", "Coimbatore", "Cuttack", "Dehradun", "Dhanbad", "Bhilai", "Durgapur", "Dindigul", "Erode", "Faridabad", "Firozabad", "Ghaziabad", "Gorakhpur", "Gulbarga", "Guntur", "Gwalior", "Gurgaon", "Guwahati", "Hamirpur", "Hubli–Dharwad", "Indore", "Jabalpur", "Jaipur", "Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Kakinada", "Kannur", "Kanpur", "Karnal", "Kochi", "Kolhapur", "Kollam", "Kozhikode", "Kurnool", "Ludhiana", "Lucknow", "Madurai", "Malappuram", "Mathura", "Mangalore", "Meerut", "Moradabad", "Mysore", "Nagpur", "Nanded", "Nashik", "Nellore", "Noida", "Patna", "Pondicherry", "Purulia", "Prayagraj", "Raipur", "Rajkot", "Rajahmundry", "Ranchi", "Rourkela", "Salem", "Sangli", "Shimla", "Siliguri", "Solapur", "Srinagar", "Surat", "Thanjavur", "Thiruvananthapuram", "Thrissur", "Tiruchirappalli", "Tirunelveli", "Ujjain", "Bijapur", "Vadodara", "Varanasi", "Vasai-Virar City", "Vijayawada", "Visakhapatnam", "Vellore" ,"Warangal"]
	if loc in tier2_cities or loc in tier1_cities:
		return True
	else:
		return False

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key": ZOMATO_API_KEY}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("---------"+response)

		return [SlotSet('location',loc)]

class CheckLocation(Action):
	def name(self):
		return 'check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		if validate_location(loc):
			SlotSet('check_op',True)
		else:
			SlotSet('check_op',False)
		return True

class SendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self,dispatcher, tracker, domain):
		config = {"user_key": ZOMATO_API_KEY }
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		prc = tracker.get_slot('price')
		emailid = tracker.get_slot('emailid')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
		d = json.loads(results)
		rest_name_list = []
		rest_location_list = []
		rest_rating_list = []
		rest_price_list = []
		rest_df_html = ""

		if d['results_found'] == 0:
			dispatcher.utter_message("No Results")
		else:
			rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
			rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
			rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
			rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
			
			pd.set_option('display.max_colwidth', -1)
			rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
			
			if prc == "less than 300":
				rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
			elif prc == "300 to 700":
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
			else:
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
			
			rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
		
		rest_df_html = rest_df_sorted.head(10).to_html(index=False)
		html_msg = "<p>Hi!<br>Here are the top %s restaurants in %s for budget of %s<br><br>"%(cuisine,loc,prc)+rest_df_html+"</p>"
		simple_mail.mail_results(emailid, html_msg)

class  GetMail(Action):
	def name(self):
		return 'action_get_mail'	

	def run(self,dispatcher, tracker, domain):
		return [SlotSet('emailid',tracker.latest_message.text)]

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'


class ValidatePrice(Action):
    def name(self):
        return 'action_validate_price'
    def price_list(self):
        return["less than 300","300 to 700","more than 700"]
    def run(self, dispatcher, tracker, domain):
        prc = tracker.get_slot('price')
        if prc == None or prc.lower() not in self.price_list():
            dispatcher.utter_message("Please enter valid price range from the given list.")
            return [SlotSet('prc_avlbl',"0")]
        else:
            dispatcher.utter_message("Price range valid")
            return [SlotSet('prc_avlbl',"1")]

class ValidateCusine(Action):
	def name(self):
		return 'action_validate_cuisine'
	def cuisine_list(self):
		return ["chinese","mexican","italian","american","south indian","north indian"]
	def run(self, dispatcher, tracker, domain):
		csn = tracker.get_slot('cuisine')
		if csn == None or csn.lower() not in self.cuisine_list():
			dispatcher.utter_message("Please enter a Valid Cuisine.")
			return [SlotSet("csn_avlbl","0")]
		else:
			dispatcher.utter_message("Found the cuisine")
			return [SlotSet("csn_avlbl","1")]

class ValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
	def location_list(self):
		return ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bokarosteelcity","chandigarh","coimbatore","cuttack","dehradun","dhanbad","durgbhilainagar","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon","guwahatiâ€šgwalior","hublidharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada","kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","prayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain","bijapur","vadodara","varanasi","vasaivirarcity","vijayawada","visakhapatnam","warangal"]
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot("location")
		if loc.lower() not in self.location_list():
			dispatcher.utter_message("Location not Found.")
			return [SlotSet("loc_avlbl","0")]
		else:
			dispatcher.utter_message("Location Found.")
			return [SlotSet("loc_avlbl","1")]

	
