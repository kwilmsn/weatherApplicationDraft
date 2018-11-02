#Katie Williamson
#Final Project Draft

'''Requirements: 

!!!Create a Python Application which asks the user for their zip code or city.
Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
Display the weather forecast in a readable format to the user.
!!!Use comments within the application where appropriate in order to document what the program is doing.
!!!Use functions including a main function.
!!!Allow the user to run the program multiple times.
!!!Validate whether the user entered valid data.  If valid data isn’t presented notify the user.
Use the Requests library in order to request data from the webservice.
!!!Use Python 3.
Use try blocks when establishing connections to the webservice.  You must print a message to the user indicating whether or not the connection was successful.'''
import requests
from pprint import pprint

apiKey = "0aed98e4a80ae218ee7bc30ae61384b9"
#Zip Code:   http://api.openweathermap.org/data/2.5/weather?zip=60007,us&appid=0aed98e4a80ae218ee7bc30ae61384b9
#City:   http://api.openweathermap.org/data/2.5/weather?q=Chicago,us&APPID=0aed98e4a80ae218ee7bc30ae61384b9
url = "http://api.openweathermap.org/data/2.5/weather"
headers = {
	'cache-control': "no-cache",
	}
#api.openweathermap.org/data/2.5/forecast/daily?zip={zip code},{country code}


def main():
	while True:
		#checking to make sure userChoice is an int
		try:
			userChoice = int(input("Would you like to put in a zip code or city name (1 for zip code, 2 for city): "))
		except:
			print('Please enter 1 or 2')
			continue
		#What program needs to do with the user input
		if userChoice == 1:
			zipCode()
			break
		elif userChoice == 2:
			cityName()
			break
		#checking to make sure userChoice is 1 or 2
		else:
			print('Please enter 1 or 2')
			continue
def zipCode():
	while True:
		#check to make sure userZipCode is a int
		try:
			userZipCode = int(input("Please enter your zip code: "))
			break #down to next while True
		except:
			print('Invalid zip code. Please try again')
			continue #up to "Please enter your zip code: "
	while True:
		#check to make sure userZipCode is 5 characters long...len() = find length...str() = len() needs a string to check length
		if len(str(userZipCode)) == 5:
			retrieveByZip(userZipCode)
			#display information
			print("\nThe weather in " + str(userZipCode) + " today is: \n\nTemperature: 		...°F \nWind: 			heaviness, ...m/s, direction (°) \nCloudiness: 		... \nPressure: 		... hpa \nHumidity: 		...% \nSunrise: 		00:00 \nSunset: 		00:00 \n")
			print("Tomorrow's Forecast: \n\nTemperature:  		...°F \nWind: 			heaviness, ...m/s, direction (°) \nCloudiness: 		... \nPressure: 		... hpa\n")
			break
		else:
			print('Invalid zip code. Please try again')
			#have to put userZipCode here because I'll have an infinite loop if it's at the top or bottom
			userZipCode = int(input("Please enter your zip code: "))
			continue #up to "Please enter your zip code: " 
def cityName():
	while True:
		userCityName = str(input('Please enter the name of your city: '))
		#checking to make sure userCity is only letters (no numbers or symbols)
		if userCityName.isalpha():
			retrieveByCity(userCityName)
			#display information
			print("\nThe weather in " + userCityName.title() + " today is: \n\nTemperature: 		...°F \nWind: 			heaviness, ...m/s, direction (°) \nCloudiness: 		... \nPressure: 		... hpa \nHumidity: 		...% \nSunrise: 		00:00 \nSunset: 		00:00 \n")
			print("Tomorrow's Forecast: \n\nTemperature:  		...°F \nWind: 			heaviness, ...m/s, direction (°) \nCloudiness: 		... \nPressure: 		... hpa\n")
			break
		else:
			print('Invalid city name. Please try again.')
			continue
def retrieveByZip(userZipCode):
	#pass the user input into the url to get back the right information
	queryString = {"zip":str(userZipCode)+",us","units":"imperial","APPID":apiKey}
	print(queryString)
	response = requests.request("GET", url, headers=headers, params=queryString)
def retrieveByCity(userCityName):
	#pass the user input into the url to get back the right information
	queryString = {"q":userCityName+",us","units":"imperial","APPID":apiKey}
	print(queryString)
	response = requests.request("GET", url, headers=headers, params=queryString)
def again():
	#program loop, letting the user input new information
	while True:
		again = input("Would you like to try again? (Please enter 'yes', 'y', 'no', or 'n') ")
		if again == 'yes' or again == 'y':
			main()
		elif again == 'no' or again == 'n':
			print('\nHave a Nice Day!')
			break
		#making sure user puts in 'yes', 'y', 'no', or 'n'
		else:
			print('Invalid input. Please try again')
			continue
main()
again()

