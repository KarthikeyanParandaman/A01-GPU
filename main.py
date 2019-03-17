import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from add import Add
from editGPU import EDITGPU
from GPUinfo import GPUINFO
from mygpu import MyGpu
from CompareGPU import COMPAREGPU
from FeatureSearch import FEATURESEARCH
JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        url_string = ''
        welcome = 'Welcome back'
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'

        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'

        user_array = MyGpu.query()

        template_values = {
            'url' : url,
            'url_string' : url_string,
            'user' : user,
            'welcome' : welcome,
            'user_array' : user_array,

            }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        #url = ''
        #url_string = ''
        #welcome = 'Welcome back'

        user = users.get_current_user()

        if not user:
            return self.redirect("/")

        name = self.request.get('users_name')

        mygpu_key = ndb.Key('MyGpu', name)
        mygpu = mygpu_key.get()

        if myuser:
            return self.redirect("/")


app = webapp2.WSGIApplication([
('/', MainPage),
('/add', Add),
('/GPUinfo', GPUINFO),
('/editGPU', EDITGPU),
('/CompareGPU', COMPAREGPU),
('/FeatureSearch', FEATURESEARCH),
], debug=True)
