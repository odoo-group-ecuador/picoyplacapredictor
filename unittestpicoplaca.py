import unittest
from datetime import datetime

#Create a dictionary with every weekday and nested plate number
weekdays = {0 : [0, 1], 1 : [2, 3], 2 : [4, 5], \
            3 : [6, 7], 4 : [8, 9], 5 : "road", \
            6 : "road"}

def check_picoplaca(license_plate, check_date, check_time):
    """Return whether or not that car can be on the road"""
    """Create a control variable for restricted hours"""
    restricted = False
    """Create time intervals for restrictec hours"""
    morning1, morning2, afternoon1, afternoon2 = "07:00", "09:30", "16:00", "19:30"
    """Convert strings into datetime format"""
    date_format = datetime.strptime(check_date + " " + check_time, "%d-%m-%Y %H:%M")
    """Validate hours to road"""
    if datetime.strptime(check_time, "%H:%M") >= datetime.strptime(morning1, "%H:%M") and \
       datetime.strptime(check_time, "%H:%M") <= datetime.strptime(morning2, "%H:%M") or \
       datetime.strptime(check_time, "%H:%M") >= datetime.strptime(afternoon1, "%H:%M") and \
       datetime.strptime(check_time, "%H:%M") <= datetime.strptime(afternoon2, "%H:%M"):
        """Validate  weekday"""
        for k, v in weekdays.items():
            if date_format.weekday() == k:
                """Validate last digit license plate"""
                for i in v:
                    if license_plate[-1] == str(i):
                        """Modify control variable"""
                        restricted = True
    if restricted == True:
        return "Sorry, this time are restricted hours.."
    else:
        return "Great! you can road in this time!."
                        
class TestPicoPlaca(unittest.TestCase):
    """UnitTest for PicoPlaca"""
    
    def test_check_picoplaca(self):
        """Validate restricted hours"""
        control_variable = check_picoplaca("plk-1234", "17-01-2017", "16:00")
        self.assertEqual(control_variable, "Great! you can road in this time!.")

if __name__ == '__main__':
    unittest.main()
        







        
