#!flask/bin/python
from application import app, socketio

socketio.run(
    app,
    host="0.0.0.0",
    port=int("8500"),
    debug=True
)