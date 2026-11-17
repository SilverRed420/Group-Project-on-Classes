import classes as c

DATA_FILE = "addressbook.txt"


def load_data(book, filename=DATA_FILE):
    """Load entries (8 lines each) from the data file into the address book."""
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip() != ""]
    except FileNotFoundError:
        print("Data file", filename, "not found.")
        return

    for i in range(0, len(lines) - 7, 8):
        name_parts = lines[i].split(None, 1)
        first = name_parts[0]
        last = name_parts[1] if len(name_parts) > 1 else ""
        month, day, year = (int(x) for x in lines[i + 1].split())
        street, city, state, zip_code = lines[i + 2: i + 6]
        phone = lines[i + 6]
        category = lines[i + 7]

        book.add_person(c.extPersonType(first, last, street, city, state,
                                        zip_code, phone, category,
                                        month, day, year))
    print("Loaded", len(book.address_book), "entries from", filename)


def save_data(book, filename=DATA_FILE):
    """Write the address book back out in the same 8-line format."""
    with open(filename, "w") as f:
        for p in book.address_book:
            street, city, state, zip_code = p.get_address()
            b = p.get_birthday()
            f.write(f"{p.get_first_name()} {p.get_last_name()}\n")
            f.write(f"{b.get_month()} {b.get_day()} {b.get_year()}\n")
            f.write(f"{street}\n{city}\n{state}\n{zip_code}\n")
            f.write(f"{p.get_phone()}\n{p.get_category()}\n")
    print("Address book saved to", filename)


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def add_entry(book):
    first = input("First name: ")
    last = input("Last name: ")
    month = read_int("Birth month (1-12, 0 if unknown): ")
    day = read_int("Birth day: ") if month else 0
    year = read_int("Birth year: ") if month else 0
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP code: ")
    phone = input("Phone: ")
    category = input("Category (Family/Friend/Business): ")
    book.add_person(c.extPersonType(first, last, street, city, state,
                                    zip_code, phone, category,
                                    month, day, year))
    print("Entry added.\n")
    book.display_address_book()


def menu():
    print("""
===== ADDRESS BOOK =====
 1. Display address book
 2. Sort by last name
 3. Search by last name (show full info)
 4. Print birthdays in a month
 5. Print names between two last names
 6. Print names by category
 7. Add entry
 8. Delete entry
 9. Save address book
 0. Exit""")


def main():
    book = c.addressBookType()
    load_data(book)

    while True:
        menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            book.display_address_book()
        elif choice == "2":
            book.sort_address_book()
            print("Sorted by last name.\n")
            book.display_address_book()
        elif choice == "3":
            book.search_person(input("Last name: "))
        elif choice == "4":
            book.print_birthdays(read_int("Month (1-12): "))
        elif choice == "5":
            book.print_between_names(input("Start last name: "),
                                     input("End last name: "))
        elif choice == "6":
            book.print_category(input("Family, Friend, or Business: "))
        elif choice == "7":
            add_entry(book)
        elif choice == "8":
            book.delete_person(input("First name: "), input("Last name: "))
            book.display_address_book()
        elif choice == "9":
            save_data(book)
        elif choice == "0":
            if input("Save before exiting? (y/n): ").lower().startswith("y"):
                save_data(book)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()