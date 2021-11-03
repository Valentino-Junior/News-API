from flask import render_template
from . import main

@main.errorhandler(404)
def err (error):
    '''
    Function to render the 404 error page
    '''
    return render_template('error.html'),404