
## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye



## Story 1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"csn_avlbl": "1"}
    - action_validate_location
    - slot{"loc_avlbl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avlbl": "1"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "soumyapanda1982@gmail.com"}
    - slot{"emailid": "soumyapanda1982@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_restart

## Story do_not_operate

* greet
    - utter_greet
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
    - action_validate_location
    - slot{"loc_avlbl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_restart

## dont send email
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"loc_avlbl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"csn_avlbl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avlbl": "1"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_goodbye
    - action_restart
## story interactive 10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_cuisine
    - slot{"csn_avlbl": "1"}
    - action_validate_location
    - slot{"loc_avlbl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avlbl": "1"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "soumyapanda1982@gmail.com"}
    - slot{"emailid": "soumyapanda1982@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_restart

## story interactive 11
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avlbl": "1"}
    - action_validate_cuisine
    - slot{"csn_avlbl": "1"}
    - action_validate_location
    - slot{"loc_avlbl": "1"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* email{"emailid": "abhinav06501@gmail.com"}
    - slot{"emailid": "abhinav06501@gmail.com"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_restart

## complete affirm-1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
	- action_validate_location
* restaurant_search{"loc_avlbl":"1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "abhinav06501@gmail.com"}
    - slot{"emailid": "abhinav06501@gmail.com"}
    - action_send_mail
    - utter_sent_email
* affirm
    - utter_restart
* reject
    - action_slot_reset
    - reset_slots
    - utter_goodbye

## complete affirm-2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "abhinav06501@gmail.com"}
    - slot{"emailid": "abhinav06501@gmail.com"}
    - action_send_mail
    - utter_sent_email
* affirm
    - utter_restart
* affirm
    - action_slot_reset
    - reset_slots
    - utter_startagain
	- utter_ask_location

## complete reject-1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* reject
    - utter_restart
* reject
    - action_slot_reset
    - reset_slots
    - utter_goodbye
	
## complete restart-2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* reject
    - utter_restart
* affirm
    - action_slot_reset
    - reset_slots
    - utter_startagain
	- utter_ask_location
	
## complete locaffirm-1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
	- action_validate_location
* restaurant_search{"loc_avlbl":"1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "abhinav06501@gmail.com"}
    - slot{"emailid": "abhinav06501@gmail.com"}
    - action_send_mail
    - utter_sent_email
* affirm
    - utter_restart
* reject
    - action_slot_reset
    - reset_slots
    - utter_goodbye

