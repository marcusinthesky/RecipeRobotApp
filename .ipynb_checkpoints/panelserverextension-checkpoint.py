from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the app.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "Dashboard.ipynb", "--allow-websocket-origin=*"])