import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os

from mygpu import MyGpu

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class GPUINFO(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		name = self.request.get('name')
		mygpu_key = ndb.Key('MyGpu',name)
		mygpu = mygpu_key.get()

		if mygpu is None:
			self.redirect("/")

		template_values = {
			'gpu_array' : MyGpu.query().fetch(),
			'mygpu' : mygpu
		}

        # pull the template file and ask jinja to render
        # it with the given template values
		template = JINJA_ENVIRONMENT.get_template('GPUinfo.html')
		self.response.write(template.render(template_values))
