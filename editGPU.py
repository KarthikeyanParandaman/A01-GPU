import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from datetime import datetime

from mygpu import MyGpu

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class EDITGPU(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        # URL that will contain a login or logout link
        # and also a string to represent this
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
        template = JINJA_ENVIRONMENT.get_template('editGPU.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        if self.request.get("cancel"):
            return self.redirect("/")

        name = self.request.get('name')

        mygpu_key = ndb.Key('MyGpu',name)
        mygpu = mygpu_key.get()
        mygpu.manufacturer = self.request.get('manufacturer')
        mygpu.date_issued = datetime.strptime(self.request.get("date_issued"),'%Y-%m-%d')
        mygpu.geometry_shader = self.request.get('geometryShader') == "on"
        mygpu.tesselation_shader = self.request.get('tesselationShader') == "on"
        mygpu.shaderInt16 = self.request.get('shaderInt16') == "on"
        mygpu.sparse_binding = self.request.get('sparseBinding') == "on"
        mygpu.texture_compressionETC2 = self.request.get('textureCompressionETC2') == "on"
        mygpu.vertex_pipeline_storesandAtomics  = self.request.get('vertexPipelineStores') == "on"
        mygpu.put()
        self.redirect("/")
