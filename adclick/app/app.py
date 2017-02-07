#!/usr/bin/env python
# coding=utf-8
from adclick.conf import settings
from flask import Flask
from flask import Blueprint, request, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_admin import Admin, BaseView, expose
import warnings
from flask.exthook import ExtDeprecationWarning

warnings.simplefilter('ignore', ExtDeprecationWarning)


app = Flask(__name__)
app.config["SECRET_KEY"] = "appstat"

admin = Admin(app)


## debugtoolbar
if settings.DEBUG:
    app.debug = True
    app.config['DEBUG_TB_PANELS'] = (
        'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
        'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
        'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
        'flask.ext.debugtoolbar.panels.logger.LoggingPanel',
        #'flask.ext.mongoengine.panels.MongoDebugPanel'
    )
    DebugToolbarExtension(app)



if __name__ == "__main__":
    app.run()