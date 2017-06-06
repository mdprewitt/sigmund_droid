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
   
- Using the [law of sines](https://www.mathsisfun.com/algebra/trig-sine-law.html), we can find our x, y coordinates if we know the direction we are heading
  and the distance we have travelled.  
 
        .
        .       \
        .       |\       
        .       |X\      
        .       |  \ z
        .     y |   \    
        .       |    \   
        .       |     \  
        .       |Z    Y\ 
        .       ---------
        .           x

Known values:

    - z=10cm (distance we travelled)
    - Y=60 degrees (angle we tavelled)
    - Z=90 degrees
    
Calculated:

    - X = 180 - (Y + Z) = 30 degrees
    
    - x/sin(X) = z/sin(Z)
    - x = sin(X) * z/sin(Z)
    - x = sin(30) * 10 / sin(90)
    - x = .5 * 10 / 1 = 5 cm
    
    - y/sin(Y) = z/sin(Z)
    - y = sin(Y) * z/sin(Z)
    - y = .87 * 10 / 1 = 8.7 cm
  
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
