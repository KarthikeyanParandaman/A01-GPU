import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from datetime import datetime
from mygpu import MyGpu
JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)
class Add(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values = {

            }
        template = JINJA_ENVIRONMENT.get_template('add.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        if not user:
            return self.redirect("/")
        if self.request.get("cancel"):
            return self.redirect("/")
        name = self.request.get('users_name')
        mygpu_key = ndb.Key('MyGpu', name)
        mygpu = mygpu_key.get()
        if mygpu:
            return self.redirect("/")

        mygpu = MyGpu(id = name)
        mygpu.manufacturer = str(self.request.get('users_manufacturer'))
        mygpu.date_issued = datetime.strptime(self.request.get("users_date_issued"),'%Y-%m-%d')
        mygpu.geometry_shader = self.request.get('users_geometry_shader') == "on"
        mygpu.tesselation_shader = self.request.get('users_tesselation_shader') == "on"
        mygpu.shaderInt16 = self.request.get('users_shaderInt16') == "on"
        mygpu.sparse_binding = self.request.get('users_sparse_binding') == "on"
        mygpu.texture_compressionETC2 = self.request.get('users_texture_compressionETC2') == "on"
        mygpu.vertex_pipeline_storesandAtomics  = self.request.get('users_vertex_pipeline_stores') == "on"
        mygpu.put()
        self.redirect('/')
