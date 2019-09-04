"""this file structure follows
http://flask.pocoo.org/docs/1.0/patterns/appfactories/
initializing db in app.db.base instead of in api.__init__.py
to prevent circular dependencies
"""
from .base import db, ma

# You must import all of the new Models you create to this page
__all__ = ["db", "ma"]
