
class addressType:
    def __init__(self, street="", city="", state="", zip_code=""):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def set_address(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_address(self):
        return self.street, self.city, self.state, self.zip_code

    def print_address(self):
        print("Street:", self.street)
        print("City:", self.city)
        print("State:", self.state)
        print("ZIP Code:", self.zip_code)


class personType:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def print_info(self):
        print("Name:", self.first_name, self.last_name)


class dateType:
    def __init__(self, month=0, day=0, year=0):
        self.month = month
        self.day = day
        self.year = year

    def set_date(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def print_date(self):
        if self.month == 0:
            print("Date of Birth: Not Available")
        else:
            print("Date of Birth:", self.month, "/", self.day, "/", self.year)


class extPersonType(personType):
    def __init__(self, first_name="", last_name="",
                 street="", city="", state="", zip_code="",
                 phone="", category="Friend",
                 month=0, day=0, year=0):

        super().__init__(first_name, last_name)

        self.address = addressType(street, city, state, zip_code)
        self.birthday = dateType(month, day, year)
        self.phone = phone
        self.category = category

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_birthday(self, month, day, year):
        self.birthday.set_date(month, day, year)

    def get_birthday(self):
        return self.birthday

    def set_address(self, street, city, state, zip_code):
        self.address.set_address(street, city, state, zip_code)

    def get_address(self):
        return self.address.get_address()

    def print_info(self):
        super().print_info()
        self.address.print_address()
        print("Phone:", self.phone)
        self.birthday.print_date()
        print("Category:", self.category)
        print()


class addressBookType:
    def __init__(self):
        self.address_book = []

    def add_person(self, person):
        self.address_book.append(person)

    def delete_person(self, first_name, last_name):
        for person in self.address_book:
            if (person.get_first_name().lower() == first_name.lower()
                    and person.get_last_name().lower() == last_name.lower()):
                self.address_book.remove(person)
                print("Person deleted.")
                return

        print("Person not found.")

    def display_address_book(self):
        if len(self.address_book) == 0:
            print("Address book is empty.")
        else:
            for person in self.address_book:
                person.print_info()

    def sort_address_book(self):
        self.address_book.sort(
            key=lambda person: person.get_last_name().lower()
        )

    def search_person(self, last_name):
        for person in self.address_book:
            if person.get_last_name().lower() == last_name.lower():
                person.print_info()
                return

        print("Person not found.")

    def print_birthdays(self, month):
        for person in self.address_book:
            if person.get_birthday().get_month() == month:
                print(person.get_first_name(), person.get_last_name())

    def print_category(self, category):
        for person in self.address_book:
            if person.get_category().lower() == category.lower():
                print(person.get_first_name(), person.get_last_name())

    def print_between_names(self, start_name, end_name):
        for person in self.address_book:
            last_name = person.get_last_name().lower()

            if start_name.lower() <= last_name <= end_name.lower():
                print(person.get_first_name(), person.get_last_name())
