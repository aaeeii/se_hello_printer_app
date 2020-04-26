from flask import Flask
from hello_world import views
app = Flask(__name__)

import hello_world.views # noqa
# from hello_world import views
