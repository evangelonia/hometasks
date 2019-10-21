import time

""" Create a class Person that has at least attributes first_name and
last_name, use property decorators to create getters and setters for the email
and fullname, email should be first_name.last_name@email.com
and fullname just first_name together with last_name separated by a space
character.  """


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def calc_avg_speed(seconds):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                time.sleep(seconds)
                return result

            return wrapper

        return decorator

    @property
    @calc_avg_speed(1.5)
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def fullname(self):
        return f"{self.first_name}.{self.last_name}"

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name


email_1 = Person("Yeva", "Stromvas")
print(email_1.fullname)
print(email_1.email)
