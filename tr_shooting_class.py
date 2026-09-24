import datetime 
 
class Member:
  expiry_days = 365
  def __init__(self, first, last):
    self.first_name = first
    self.last_name = last
 
    self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)
 
  def show_expiry(self):
    return f'{self.first_name} {self.last_name} expires on {self.expiry_date}'
 
  def show_status(self):
    return f'{self.first_name} {self.last_name} is a Member'
 
#Subclass for us to use for administrators
class Admin(Member):
  expiry_days = 365 * 100
 
  def __init__(self, first, last, secret):
    super().__init__(first,last)
    self.secret_code = secret
  def show_status(self):
    return f'{self.first_name} {self.last_name} is an Admin'
 
#Subclass for us to use for normal users
class User(Member):
  def show_status(self):
    return f'{self.first_name} {self.last_name} is a User'
  
print(Admin.__dict__)