
import cherrypy
from cherrypy import expose

class TemperatureConverter():
    @expose
    def index(self):
        return "Hello World"
    #decorate the function
    @expose
    def celciusToFahrenheit(self, temperature):
        temp = int(temperature)
        tempInFahrenheit = (temp*9 + 160) / 5
        #return str(tempInFahrenheit);
        return("The temp of " , temperature , " in celcius is " ,
               str(tempInFahrenheit) , " in Fahreiheit")

    @expose
    def fahrenheitToCelcius(self, temperature):
        tempInCelcius = ((temperature - 32)/9)*5
        print("The temp of " , temperature , "in fahrenheit is" ,
              tempInCelcius , "in Celcius")

cherrypy.quickstart(TemperatureConverter())
