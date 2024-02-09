from Airport import *
# Developed by: Manaal Hashmi
# Date: April 12th
# Desc: A program that uses a flight number, and orgin and destination airports to display flight details 
# Inputs: flight details, new flight details, files
# Outputs: flight details, whethere flight is domestic or international, or displaying the orgin airport and dest airports cities
class Flight: # establishign flight class of funcs that includes flight numbers,orgin, destintion codes, and checks if domestic flight
    
    with open('flights.txt', 'r') as file: # opens file and reads it
        lines = file.readlines() # reads the file line by line
   
    with open('flights.txt', 'w') as file: # re writting the file
            for line_f1 in lines: # re writes the file line by  line
                line_f1 = ' '.join(line_f1.split()) # formatting each line correctly
                line_f1 = line_f1.strip().replace(" ","") # getting rid of extra spaces
                file.write(str(line_f1)+"\n") # re writting the file with correct format
           
    def __init__(self, flightNo, origAirport, destAirport): # establishing main assets of the flights class 
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport): # making sure the flight info is
            raise TypeError("The origin and destination must be Airport objects") #in airport objects and exists there
        
        letter_count = 0 # counting the letters in the flight code
        num_count = 0 # establishing a variable for counting letters that starts at zero
        for char in flightNo: # counting charecters in the flight number
            if char.isalpha(): # making dure its only counting letters with .isalpha
                letter_count += 1 # this will loop and add one to the count when a single letter is found
            elif char.isdigit(): # this does the same thing except with counting the numbers with .isdigit
                num_count += 1 # this will loop and add 1 to the count for every number in the flight number
                
        if letter_count != 3 or num_count != 3: # making sure the count is in the correct format (3letters 3numbers) 
            print("The flight number format is incorrect") # letting the user know if there is a incorrect flight number
            
            
        self.flightNo = flightNo # if the main variables are established after letting user know of any errors
        self.origAirport = origAirport
        self.destAirport = destAirport
           
    def __repr__(self): # this repr will return the flight class in a format that displays the orgin and destination as their cities
        flight_type = "unknown" # instead of showing the orgin and destination as codes the unknown is for establishing the variable
        if self.isDomesticFlight() == True: # if the self.isDomestic is true the flight type should be domestic
            flight_type = "[domestic]"
        elif self.isDomesticFlight() == False: # if its false it should be international
            flight_type = "[international]"
        return (f"Flight({self.flightNo}): {self.origAirport.city} -> {self.destAirport.city} {flight_type}")
        # now it will return the flight class in this format above
           
    def __eq__(self, other): # 
        if self.origAirport == other.origAirport and self.destAirport == other.destAirport: # checking to see
            return True # if self and other flights are considered the same flight
        else: # if true its the same flight and if false its not
            return False # if two flight details have the same orgin and destination its likley they are the same flight
        
    def getFlightNumber(self): # gets the flight number of a flight
        return self.flightNo      
        
    def getOrigin(self): # gets the orgin of a flight
        return self.origAirport
        
    def getDestination(self): # gets the destination of the flight
        return self.destAirport
        
    def isDomesticFlight(self): # tells user if the flight is domestic or international
        if self.origAirport.country == self.destAirport.country: # if the orgin and destinations country are the same then
            return True  # the flight should be domestic so this will return true for is a domesticflight
        else:
            return False # and false if it is not a domestic flight
    
      
    def setOrigin(self, origin): # allow user to update the orgin of the flight
        self.origAirport = origin
    
    def setDestination(self, destination): # allow user to update the destination of the flight
        self.destAirport =  destination