#import module "datetime" to convert string into datetime
from datetime import datetime

#Create a dictionary with every weekday and nested plate number
weekdays = {0 : [0, 1], 1 : [2, 3], 2 : [4, 5], \
            3 : [6, 7], 4 : [8, 9], 5 : "road", \
            6 : "road"}

class PicoPlaca(object):
    """Attemp to check pico y placa for my car.""" 
    def __init__(self, license_plate, check_date, check_time):
        """Initialize license_plate, date and time atributes"""
        self.license_plate = license_plate
        self.check_date = check_date
        self.check_time = check_time

    def car_query_parameters(self):
        """Print car parameters"""
        print "You entered the following information:" \
              + "\n license: " + "\t" + self.license_plate.upper() \
              + "\n date: " + "\t\t" + self.check_date \
              + "\n and time: " + "\t" + self.check_time

    def check_picoplaca(self):
        """Return whether or not that car can be on the road"""
        """Create a control variable for restricted hours"""
        restricted = False
        """Create time intervals for restrictec hours"""
        morning1, morning2, afternoon1, afternoon2 = "07:00", "09:30", "16:00", "19:30"
        """Convert strings into datetime format"""
        date_format = datetime.strptime(self.check_date + " " + self.check_time, "%d-%m-%Y %H:%M")
        """Validate hours to road"""
        if datetime.strptime(self.check_time, "%H:%M") >= datetime.strptime(morning1, "%H:%M") and \
           datetime.strptime(self.check_time, "%H:%M") <= datetime.strptime(morning2, "%H:%M") or \
           datetime.strptime(self.check_time, "%H:%M") >= datetime.strptime(afternoon1, "%H:%M") and \
           datetime.strptime(self.check_time, "%H:%M") <= datetime.strptime(afternoon2, "%H:%M"):
            """Validate  weekday"""
            for k, v in weekdays.items():
                if date_format.weekday() == k:
                    """Validate last digit license plate"""
                    for i in v:
                        if self.license_plate[-1] == str(i):
                            """Modify control variable"""
                            restricted = True
        if restricted == True:
            print "Sorry, this time are restricted hours.."
        else:
            print "Great! you can road in this time!."

#Create and instance into PicoPlaca class using input(), raw_input() for Python2
my_car = PicoPlaca(raw_input("Full license plate (XXX-####): "), \
                   raw_input("Date (DD-MM-YYYY): "), \
                   raw_input("Time 24-hour (HH:MM): "))

#Call method to review the entered information
my_car.car_query_parameters()

#Call method to check picoplaca
my_car.check_picoplaca()
