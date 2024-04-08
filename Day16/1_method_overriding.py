# Unlike method overloading, method overriding is possible in Python

class Vehicle:
    def get_details(self):
        return "This is a vehicle"


class Car(Vehicle):
    def get_details(self):  # Method Overriding
        return "This is a car"
    

obj = Car()
print(obj.get_details())


class DjangoUserCreate:
    def create_user(self):
        self.user = "XYZ"


# class MyUserCreate(DjangoUserCreate):
#     def create_user(self):
#         super().create_user()
#         send_email(self.user)
#         pass