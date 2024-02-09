class Airport: # establishing airport class of functions that includes an airports code,city,country, and continent
# Developed by: Manaal Hashmi
# Date: April 12th
# Desc: A program that uses an airports code and what city and country the airport is from to display these sub details
# Inputs: airport details,files
# Outputs: airport details, and continent of the airport
    cleaned_lines = [] # opening a dictionary to re write the file with correct format
    with open('airports.txt', 'r') as file: # reading the file
        for line in file: # reading one line of the file
            line = ' '.join(line.split()) # formatting the file correctly
            cleaned_lines.append(line.strip().replace(" ","")) #formatting getting rid of spaces
        
            

    with open('airports.txt', 'w') as file: # re writting the file with the new clean lines
        for line in cleaned_lines: # line by line the file will be re written
            file.write(str(line)+"\n") 

    def __init__(self, code, city, country,continent): # establishes the main assets if the airport class
        self.code = code 
        self.city = city
        self.country = country
        self.continent = continent
        
    def __repr__(self):
        return f"{self.code} ({self.city}, {self.country})" # reperesents the airport class when its called as code (city,country)

    def getCode(self):  # gets the code of the airport 
        return self.code
    
    def getCity(self): # gets the city of the airport
        return self.city
    
    def getCountry(self): # gets the country of the airport
        return self.country
    
    def getContinent(self): # gets the continent of the airport
        return self.continent
    
    def setCity(self, city): # updates the airport city
        self.city = city
    
    def setCountry(self,country): # updates the airport country
        self.country = country
        
    def setContinent(self,continent): # updates the airport continent
        self.continent = continent