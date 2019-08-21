import os
from flask_script import Manager

from bdc_geoserver import app

manager = Manager(app)

@manager.command
def run():
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('PORT', '5000'))
    except ValueError:
        PORT = 5000

    app.run(HOST, PORT)

@manager.command
def test():
    """Run the unit tests."""
    import pytest
    pytest.main(["-s", "tests/"])

if __name__ == '__main__':
    manager.run()
