from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

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
		config={ "user_key":"7667690278598ab50d50f936c94bc760"}
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
