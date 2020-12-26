## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- i am looking for an [indian](cuisine) spot
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "300 to 700"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- test
- [Mexican](cuisine) + [300 to 700](price) budget + [near me](location)
- show me restaurant with average price budget of [less than rs 300]{"entity": "price", "value": "less than 300"}
- show me restaurant with average price budget of [under rs 300]{"entity": "price", "value": "less than 300"}
- show me restaurant with average price budget of [below 300]{"entity": "price", "value": "less than 300"}
- [<300]{"entity": "price", "value": "less than 300"}
- show me restaurant with average price budget of [less than 300](price)
- show me restaurant with average price budget [between rs 300 and 700]{"entity": "price", "value": "300 to 700"}
- show me restaurant with average price budget of [Rs.300 to Rs.700]{"entity": "price", "value": "300 to 700"}
- show me restaurant with price budget of [300 to 700 rs]{"entity": "price", "value": "300 to 700"}
- [300-700]{"entity": "price", "value": "300 to 700"} range
- [300-700]{"entity": "price", "value": "300 to 700"}
- [more than rs 700]{"entity": "price", "value": "more than 700"}
- show me restaurant with average price budget of [above rs 700]{"entity": "price", "value": "more than 700"}
- show me restaurant with average price budget of [more than 700](price)
- show me some restaurants in [high range]{"entity": "price", "value": "more than 700"}
- show me some [high end]{"entity": "price", "value": "more than 700"}
- [> rs.700]{"entity": "price", "value": "more than 700"}
- [>700]{"entity": "price", "value": "more than 700"}
- I am looking a restaurant in [560093](location)
- looking for [chinese](cuisine) restaurant
- [bangalore](location)
- [Between](price) [Rs.300 and 700](price)

## intent:email
- [soumyapanda1982@gmail.com](emailid)
- [rahul.jain@yahoo.co.in](emailid)
- [shruti_joshi@gmail.in](emailid)
- [rajeev_mathur@hotmail.web](emailid)
- [divyaj17@yahoo.com](emailid)
- [soumyapanda1982@gmail.com](emailid)

## synonym: more than 700
- more than rs 700
- >700
- expensive
- > 700
- gourmet
- classy
- high class
- fancy
- > 700 Rs
- >700 Rs
- more than Rs 700
- above 700
- over 700 rs.

## synonym:300 to 700
- moderate
- between rs 300 and 700
- Rs.300 to Rs.700
- 300 to 700 rs
- 300-700
- 300 to 700
- reasonable
- between rs. 300 and 700
- around 700
- < 700
- mid budget
- mid range
- medium price
- > 300
- within 500 Rs
- good price
- rs.300
- rs.500
- upto 700 rs.
- 700

## synonym:4
- four

## synonym:bangalore
- Bengaluru
- blr

## synonym:chennai
- chnnai
- madras
- Chn

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:delhi
- New Delhi
- dilli
- DEL

## synonym:less than 300
- less than rs 300
- under rs 300
- below 300
- <300
- cheap
- between Rs. 100 and 300
- pocket-friendly
- budget
- low cost
- < 300
- budget friendly
- budget-friendly
- low-cost
- inexpensive
- under 300
- upto 300 rs
- 300
- less than rs. 300"
- less than 300"
- under 300"
- upto 300

## synonym:more than 700
- above rs 700
- high range
- high end
- > rs.700

## synonym:mumbai
- Bombay
- BOM
- MUM

## synonym:vegetarian
- veggie
- vegg

## regex:email
- ^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
- Ahmedabad
- Bengaluru
- Chennai
- Delhi
- Hyderabad
- Kolkata
- Mumbai
- Pune
- Agra
- Ajmer
- Aligarh
- Amravati
- Amritsar
- Asansol
- Aurangabad
- Bareilly
- Belgaum
- Bhavnagar
- Bhiwandi
- Bhopal
- Bhubaneswar
- Bikaner
- Bilaspur
- Bokaro Steel City
- Chandigarh
- Coimbatore
- Cuttack
- Dehradun
- Dhanbad
- Bhilai
- Durgapur
- Dindigul
- Erode
- Faridabad
- Firozabad
- Ghaziabad
- Gorakhpur
- Gulbarga
- Guntur
- Gwalior
- Gurgaon
- Guwahati
- Hamirpur
- Hubli
- Dharwad
- Indore
- Jabalpur
- Jaipur
- Jalandhar
- Jammu
- Jamnagar
- Jamshedpur
- Jhansi
- Jodhpur
- Kakinada
- Kannur
- Kanpur
- Karnal
- Kochi
- Kolhapur
- Kollam
- Kozhikode
- Kurnool
- Ludhiana
- Lucknow
- Madurai
- Malappuram
- Mathura
- Mangalore
- Meerut
- Moradabad
- Mysore
- Nagpur
- Nanded
- Nashik
- Nellore
- Noida
- Patna
- Pondicherry
- Purulia
- Prayagraj
- Raipur
- Rajkot
- Rajahmundry
- Ranchi
- Rourkela
- Salem
- Sangli
- Shimla
- Siliguri
- Solapur
- Srinagar
- Surat
- Thanjavur
- Thiruvananthapuram
- Thrissur
- Tiruchirappalli
- Tirunelveli
- Ujjain
- Bijapur
- Vadodara
- Varanasi
- Vasai
- Virar City
- Vijayawada
- Visakhapatnam
- Vellore
- Warangal
