# sigmund_droid
Lego EV3 Programs

# Notes

- For line navigation, need to calibrate RLI to room light
- Consider using the Rotation Sensor to understand current location
- Ideas for lines: electrician's tape, colored duct tape

# Code Notes

- `globals` module holds location location and constants for navigating
- `navigation` module contains simple methods to move/turn'
- 'directory_app' module is a flask app to maintain Locations, Desks, People
    - initialize database with `db_upgrade.py`
    - create sample data with: `setup_sample_data.py`
    - start server with `run.py`
    - access admin via (http://127.0.0.1:5000/admin)
    - access apis via (http://127.0.0.1:5000/api/person)
    - search for person with: (http://127.0.0.1:5000/api/person?q={"filters":[{"name":"sid","op":"==","val":"a123456"}],"single":"true"}) or `sample_person_query.py`
    
# In Action

- Navigation: https://www.flickr.com/gp/marcprewitt/79bh3v

# See Also

- Simple smooth line following: https://www.youtube.com/watch?v=098MzecwvkI
- Simple explor3r robot: http://robotsquare.com/2015/10/06/explor3r-building-instructions/
- Utility to measure robot distance: http://ev3lessons.com/resources/wheelconverter/

# Configuration

- LargeMotor = B
- LargeMotor = C
- MediumMotor = A

- Color Sensor = 3
- IR Sensor = 4
