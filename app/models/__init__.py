"""this file structure follows
http://flask.pocoo.org/docs/1.0/patterns/appfactories/
initializing db in app.db.base instead of in api.__init__.py
to prevent circular dependencies
"""
from .base import db, ma
from .cereal import Cereal

__all__ = ["db", "ma", "Cereal"]
