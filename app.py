import os
import ptvsd
from flask import Flask

DEBUGGER_PORT = int(os.environ['DEBUGGER_PORT'])
HOST = os.environ['HOST']

# when FLASK_ENV=development reloading is enabled when file changes are detected
# this has the undesireable effect of calling `ptvsd.enable_attach` each time there's a reload
# if VSCode has already attached to this debugger when `ptvsd.enable_attach` is called, an expection will be raised

# specifically this execption is: OSError(10048, 'Only one usage of each socket address (protocol/network address/port) is normally permitted', None, 10048, None)

try:
    print('Enabling debugger on '+HOST+':'+repr(DEBUGGER_PORT))
    ptvsd.enable_attach(address=(HOST, DEBUGGER_PORT))
except Exception as ex:
    print('Debugger setup failed: '+repr(ex))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, VSCode!'
