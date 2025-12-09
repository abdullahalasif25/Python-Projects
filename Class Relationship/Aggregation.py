class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_zip, new_area):
        self.name = new_name
        self.address.change_address(new_city, new_zip, new_area)

class Address:

    def __init__(self, city, zipcode, area):
        self.city = city
        self.zipcode = zipcode
        self.area = area

    def change_address(self, new_city, new_zip, new_area):
        self.city = new_city
        self.zipcode = new_zip
        self.area = new_area    


addr= Address('Dhaka',1000, 'Lalbag')
cust = Customer('Asif', 'Male', addr)

cust.edit_profile('Ashik', 'Kishoreganj','2300', 'Sadar')

print(cust.address.area )
