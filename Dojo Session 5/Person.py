import re # Python doesn't automatically load the regular expression module 
          # you have to explicitly tell it to bring that tool into your script.
          # (See what a regular expression is below)


class Person:
    def __init__(self, name, age, email, phoneNumber, role):
        self._name = name
        self._age = age
        self._email = email
        self._phoneNumber = phoneNumber
        self._role = role

    # Name
    @property                                 # @property designates the property "name"
    def name(self):                           # this is considered as the "getter"
        return self._name

    @name.setter                              # By using self._name to store the data and self.name as the property interface,
    def name(self, value):                    # you separate the data storage from the access logic.
        self._name = value                    # This is considered as the "setter"          
                                              # The underscore (_) explicitly signals that an attribute, method, class, or module 
                                              # is intended for internal use only.  
    # Age
    @property                                 
    def age(self):                            
        return self._age                    
                                                  
    @age.setter                                            # Setters allows for additional logic around allowed values               
    def age(self, value):                                  # Since we know an age for a person cannot be below 0, we set that logic here
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value


    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"  # This is a regular expression. They are used in all coding languages
        if not re.match(email_regex, value):                               # A regular expression is a sequence of characters that defines a search pattern, 
            raise ValueError(f"Invalid email format: '{value}'")           # used for matching, locating, validating, or manipulating text within string typed data 
        self._email = value                                                # By using re via import and the built in method .match(), we can return a boolean
                                                                           # to perform a check on the email format. 


    # Phone Number
    @property                           
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        phone_regex = r"^\d{3}-\d{3}-\d{4}$"                                # Regex expecting the format XXX-XXX-XXXX                          
        if not re.match(phone_regex, value):
            raise ValueError(f"Invalid phone number format. Expected XXX-XXX-XXXX, got '{value}'")
        self._phoneNumber = value
    
    
    # Role
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        self._role = value