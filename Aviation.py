from Flight import *
from Airport import *
# Developed by: Manaal Hashmi
# Date: April 12th
# Desc: A program that creates an aviation system that uses flight airport, and country details
# Inputs: flight details, airport details, files
# Outputs: flight details, airport details, connections, finding oceans crossed, getting all flights/airports
# from a file,finding all country/cities flights
class Aviation: # class that can preform opperations on  all flights, airports, and countries from a file
    
   with open('countries.txt', 'r') as file: # opens file and reads it
       lines = file.readlines() # reads the file line by line

   with open('countries.txt', 'w') as file: # re writting the file
       for line in lines: # re writes the file line by  line
           line = ' '.join(line.split()) # formatting each line correctly
           line = line.strip().replace(" ","") # getting rid of extra spaces
           file.write(line + "\n") # re writting the file with correct format
             
   def __init__(self): # creatinf dictionaries to store all file info on flights, airports, and countries
       self._allAirports =  {} #setting this to a dictionary
       self._allFlights = {} #setting this to a dictionary
       self._allCountries = {} #setting this to a dictionary
       
   def getAllAirports(self): # function that will return all airports
       return self._allAirports
   
   def getAllFlights(self): # function that will return all flights
       return self._allFlights

   def getAllCountries(self): # function that will return all countries
       return self._allCountries
       
   def setAllAirports(self, new_airports): # function that updates all airports
       self._allAirports = new_airports
       
   def setAllFlights(self, new_flights): # function that updates all flights
       self._allFlights = new_flights

   def setAllCountries(self, new_countries): # function that updates all countries
       self._allCountries = new_countries
       
   def loadData(self, airportFile, flightsFileName, countriesFile): # function that loads data for countries,flights,and airports
       try:
           self._allCountries = {} # establishing dictionary to be filled with countries and continents
           with open(countriesFile, "r", encoding='utf8') as file:
               for line_c2 in file:
                   country, continent = line_c2.strip().split(',')  # establishes what part of the line is continent or country 
                   country = country.strip() # creating country variable and getting rid of extra spaces
                   continent = continent.strip()  # creating continent variable and getting rid of extra spaces
                   self._allCountries[country] = ",".join([country, continent]) # this will make the country the key and return the country and continent
           
           self._allAirports = {} # establishing dictionary to be filled with airports
           with open(airportFile, "r", encoding='utf8') as file: # reading the airports file
                for line_a in file: # creating loop that reads file line by line
                    code, country, city = line_a.strip().split(',') # establishes what part of the line is code country etc
                    code = code.strip() # creating seprate variables and stripping any extra spaces
                    country = country.strip() # creating seprate variables and stripping any extra spaces
                    city = city.strip() # creating seprate variables and stripping any extra spaces
                    continent = self._allCountries[country] # continent references the countries file because it is included there
                    airport_object = Airport(code, city, country, continent) # creating an airport object
                    self._allAirports[code] = airport_object # making the code of the airport the key for the details in airport object
                   
           self._allFlights={} # establishing dictionary to be filled
           with open(flightsFileName,"r", encoding='utf8') as file: # reading the flights file
               for line_f in file: # creating loop that reads file line by line
                   line_f = line_f.strip() # stripping line so it can be indexed
                   parts = line_f.split(',') # establishes what part of the line is what by indexing the line by number 
                   flightNo = parts[0].strip() # creating seprate variables and stripping any extra spaces
                   origAirport = self._allAirports[parts[1].strip()] # creating seprate variables and stripping any extra spaces
                   destAirport = self._allAirports[parts[2].strip()] # creating seprate variables and stripping any extra spaces
                   flights_object = Flight(flightNo, origAirport, destAirport) # creating a flights object with the flight details
                   if str(origAirport) in self._allFlights: # makes sure that the key is the orgin airport and that its in the flights dictionary
                      self._allFlights[str(origAirport)].append(flights_object) # this will add the flight-object to the all flights dictionary
                      # and the orgin airport will be the key
                   else:
                       self._allFlights[str(origAirport)] = [flights_object] # if the orgin airport is not in the allflights dict
                       # it will find the flights object for that orgin using orgin as a key
           return True
       except: # if there are any exceptions the load data will fail and be false
           return False  

   def getAirportByCode(self, code): # this function will get all airports with a a given code 
       return self._allAirports[code] 
   
   def findAllCityFlights(self, city): # this function will
    city_flights = [] # creating a empty list for storing all flights involved with a given city
    for flights_list in self._allFlights.values(): # searching in the all flights dictionary
        for flight in flights_list: # this searchers per sub-line in the dictionary
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city: # if an orgin city or
                city_flights.append(flight) # destination city matches the given city it will be added to the list
    return city_flights # and return to the user all the flights with the given city
   
   def findFlightByNo(self, flightNo): # function for finding a flight with a given flight number
    for flights_list in self._allFlights.values(): # checking for the number in the all flights dictionary
        for flight in flights_list: # checking each sub - line in the dictionary
            if flight.getFlightNumber() == flightNo: # if one of the sublines contains a matching flight number
                return flight # it will return that flights info
    return -1 # if it doesn't exist it will return -1

   
   def findAllCountryFlights(self, country): # this function will find all flights that are assosiated with a given country
       country_flights = [] # creating an empty list to store the flight info of flights from or going to the given country
       for flights_list in self._allFlights.values(): # searching in the all flights dictionary
           for flight in flights_list: # searching by sub-line in the dictionary to see if a flight in it has either
           # an orgin codes that corresponds to a country that matches the given country or a dest code's country that matches
                if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country:
                   country_flights.append(flight) # if there are matches it will be added to the country flight list created before
       return country_flights # and return it to the user
   
   def findFlightBetween(self, origAirport, destAirport): # this function can find dircet flights or connections
       
       if origAirport not in self._allAirports.values() or destAirport not in self._allAirports.values():
           return -1 # making sure the given airport is included in the all airports dictionary created from a given file
       for flights_list in self._allFlights.values(): # checking inside of the all flights dictionary 
            for flight in flights_list: # checking per sub line of info
              if flight.getOrigin().getCity() == origAirport.getCity() and flight.getDestination().getCity()==destAirport.getCity():
                    flightNo = flight.getFlightNumber() # if a flight matches both the given orgin and destination that means theres a 
                    # direct flight between the two given places. The loop gets the orgin airport code and then its city and the given orgins city and
                    # checks if they match, and also checks if the two destination cities match
                    return f"Direct Flight({flightNo}): {flight.getOrigin().getCode()} to {flight.getDestination().getCode()}"
                    # then returns the flight number of the dircect flight and the airport codes of the orgin and destination
       
       connection_codes = [] # creating an empty list to store connecting flight codes in
       for flight in self._allFlights[str(origAirport)]: # looking in the all flights dictionary using the orgin airport code as the key to find connections
           for con_flight in self._allFlights[str(flight.getDestination())]: # checking if the given connecting flight info is in the dictionary keyed by the destination code
               if destAirport.getCity() == con_flight.getDestination().getCity(): # if a destination city matches one in the flight dictionary
                   connection_codes.append(con_flight.getOrigin().getCode()) # it will add it to th connection code dictionary and find the code of the orgin flight
                 
       set_connection_codes = set(connection_codes) # creating a set of connection codes from the previously made dictionary
       if len(set_connection_codes) > 0: # if the length of the set is creater than zero 
           return set_connection_codes # it will return any info in the set whether its a single hop or direct flight
       else:
           return -1 # if theres nothing in the set (no connections) it will return -1 to the user
       
   def findReturnFlight(self, firstFlight): # fucntion to find a return flight
       
        for flight in self._allFlights[str(firstFlight.getDestination())]: # using the given first flights destination
           # as a key in the all flights dictionary if a destination city matches  the city of the first flight 
           if flight.getDestination().getCity() == firstFlight.getOrigin().getCity():
               return flight # it will return the flight objects for the found return flight
        else:
           return -1 # if nothing was found it will return -1
       
   def findFlightsAcross(self, ocean): # function that returns flight codes that crossed a given ocean
       flight_codes = [] # creating an empty list to store flight codes that go across a given ocean in
       for flights_list in self._allFlights.values(): # searching in the all flights dictionary
          for flight in flights_list: #  searching by sub-line of info in the all flights dictionary
              green_zone = {"NorthAmerica","SouthAmerica"} # establishing each colour zone by its country
              red_zone = {"Asia","Australia"}
              blue_zone = {"Africa","Europe"}
             
              comma_index = flight.getOrigin().getContinent().find(",")  # this function is to eventually remove the country
              # from get continent because the get continent returns both the country and the continent
              origin_continent = flight.getOrigin().getContinent()[comma_index+1:].strip() # this finds the orgin continent and should 
              comma_index = flight.getDestination().getContinent().find(",") # not include the extra country
              destination_continent = flight.getDestination().getContinent()[comma_index+1:].strip() # finds destination continent
             
              if ocean == "Atlantic":
                  #a flight crosses the Atlantic if the origin is the from one of
                  #the countries in the green zone and the destination is to
                  #one country in the blue zone or vice versa.
                  if (origin_continent in green_zone and destination_continent in blue_zone) or (destination_continent in green_zone and origin_continent in blue_zone):
                      flight_codes.append(flight.getFlightNumber()) # adds the found flight number for the zones that are assosiated witht the Atlantic ocean into list
              if ocean == "Pacific":    
                  #
                  #A flight crosses the Pacific if the origin is the from one of
                  #the countries in the green zone and the destination is to
                  #one country in the red zone or vice versa.
                  
                 
                  if (origin_continent in green_zone and destination_continent in red_zone) or (destination_continent in green_zone and origin_continent in red_zone):
                      flight_codes.append(flight.getFlightNumber())  # adds the flight number for flights that cross zones assosiated with the Pacific ocean into the list
                       
              set_flight_codes = set(flight_codes)   # creates a set out of the flight codes
       if not flight_codes: # if nothing was found -1  will be returned
           return -1 
       
       return set_flight_codes # returns the flight codes set to user