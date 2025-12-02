import re
class Car:
    def __init__(self, brand, model, year, price_perday):
        self.brand = brand
        self.model = model
        self.year = year
        self.price_perday = price_perday
    def get_info(self):
        return f"""
Brand: {self.brand}
Model: {self.model}
Year: {self.year}
Price: {self.price_perday}
"""

class User:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.cars = []
    def get_info(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Phone Number: {self.phone_number}
    """

class RentalSystem:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.users = []
        self.rentals = []
        
    def register_user(self):
        name = input("Ismingizni kiriting: ")
        age = input("Yoshingizni kiriting: ")
        phone_number = input("Telefon raqamingizni kiriting: ")

        for u in self.users:
            if u.phone_number == phone_number:
                print("Bu foydalanuvchi allaqachon ro‘yxatdan o‘tgan!")
                return
        
        user = User(name, age, phone_number)
        self.users.append(user)
        print("Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!")

    def add_car(self):
        brand = input("Brandni Kiriting")
        model = input("Modelini Kiriting")
        try:
            year = int(input("Yilini Kiriting"))
            price_perday = int(input("Kunlik Summasini Kiriting"))
        except ValueError as r:
            print(f"Xato Qayta Kiriting {r}")
            return
        car = Car(brand, model, year, price_perday)
        if car not in self.cars:
            self.cars.append(car)

    def rented_cars(self):
        return self.rentals

    def view_all_cars(self):
        for i in self.cars:
            print(i.get_info())
    
    def get_rentcar(self):
        if not hasattr(self, "current_user"):
            print("Ijaraga olish uchun avval login qiling!")
            return
        brand = input("Brandni kiriting: ")
        model = input("Modelni kiriting: ")

        try:
            year = int(input("Yilini kiriting: "))
        except ValueError:
            print("Yil faqat raqam bo‘lishi kerak!")
            return

        for c in self.cars:
            if c.brand == brand and c.model == model and c.year == year:
                self.rentals.append(c)
                self.cars.remove(c)
                self.current_user.cars.append(c)
                print("Mashina ijaraga olindi!")
                return
        
        print("Kiritilgan mashina topilmadi.")

    def return_car(self):
        if not hasattr(self, "current_user"):
            print("Mashina qaytarish uchun login qiling!")
            return

        user = self.current_user

        if not user.cars:
            print("Sizda ijaraga olingan mashina yo‘q.")
            return

        print("\n--- Sizdagi ijaraga olingan mashinalar ---")
        for i, car in enumerate(user.cars, start=1):
            print(f"{i}. {car.brand} {car.model} {car.year}")

        try:
            index = int(input("Qaysi mashinani qaytarmoqchisiz (raqam kiriting): "))
            car_to_return = user.cars[index - 1]
        except:
            print("Xato tanlov!")
            return
        self.cars.append(car_to_return)

        user.cars.remove(car_to_return)

        if car_to_return in self.rentals:
            self.rentals.remove(car_to_return)

    print("Mashina muvaffaqiyatli qaytarildi!")

    def login(self):
        phone_number = input("Telefon raqamingizni kiriting: ")

        user_found = None
        for u in self.users:
            if u.phone_number == phone_number:
                user_found = u
                break

        if not user_found:
            print("Bunday foydalanuvchi topilmadi!")
            return

        self.current_user = user_found

        print(f"Xush kelibsiz, {user_found.name}!")

        while True:
            print("\n1. Mashinalarni ko‘rish")
            print("2. Mashina ijaraga olish")
            print("3. Mashinani Qaytarish")
            print("4. Chiqish")

            choice = input("Tanlovingiz: ")

            if choice == "1":
                self.view_all_cars()
            elif choice == "2":
                self.get_rentcar()
            elif choice == "3":
                self.return_car()
            elif choice == "4":
                print("dastur tugadi")
                break
            else:
                print("Noto‘g‘ri tanlov!")

    def admin(self):
        print("Admin paneliga xush kelibsiz!")
        while True:
            print("\n1. Mashina qo‘shish")
            print("2. Hamma mashinalarni ko‘rish")
            print("3. Chiqish")

            choice = input("Tanlovingiz: ")

            if choice == "1":
                self.add_car()
            elif choice == "2":
                self.view_all_cars()
            elif choice == "3":
                print("Admin paneldan chiqildi.")
                break
            else:
                print("Noto‘g‘ri tanlov!")
                self.view_all_cars()


    def manager(self):
        while True:
            print("\n--- RENTAL SYSTEM ---")
            print("1. Admin rejimi")
            print("2. Ro‘yxatdan o‘tish")
            print("3. Kirish")
            print("4. Chiqish")

            choice = input("Tanlovingiz: ")

            if choice == "1":
                password = "password_admin"
                j = input("Admin parolini kiriting: ")
                if j == password:
                    self.admin()
                else:
                    print("Noto‘g‘ri parol!")
            elif choice == "2":
                self.register_user()
            elif choice == "3":
                self.login()
            elif choice == "4":
                print("Dastur tugadi.")
                break
            else:
                print("Xato tanlov!")

system = RentalSystem("CarRent")
system.manager()