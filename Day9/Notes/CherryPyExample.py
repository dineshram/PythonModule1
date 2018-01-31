import cherrypy
from cherrypy import expose

class Converter:
    @expose
    def index(self):
        return "Hello World!"

    @expose
    def fahr_to_celc(self, degrees):
        temp = (float(degrees) - 32) * 5 / 9
        return "%.01f" % temp

    @expose
    def celc_to_fahr(self, degrees):
        temp = float(degrees) * 9 / 5 + 32
        #return "%.01f" % temp
        return "<html><body>The temperature in fahrenheit is %d</body></html>" % temp

cherrypy.quickstart(Converter())
