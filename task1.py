from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone number must be 10 digits.')
        super().__init__(value)
            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break
        raise ValueError('Record not found.')    
        

    def find_phones(self, phone):
        return next((p for p in self.phones if p.value == phone), None)


    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search_by_name(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
    
    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError('No record.')

    
if __name__ == "__main__":
    address_book = AddressBook()
    record1 = Record("Alice")
    record1.add_phone("1234567890")
    address_book.add_record(record1)

    record2 = Record("Bob")
    record2.add_phone("0987654321")
    address_book.add_record(record2)

    print("Address Book:")
    print(address_book)

    
    print("\nSearching for Alice:")
    print(address_book.search_by_name("Alice"))

    
    address_book.delete_record("Bob")
    print("\nAddress Book after deleting Bob:")
    print(address_book)

   
    record1.edit_phone("1234567890", "1112223333")
    print("\nAddress Book after editing Alice's phone:")
    print(address_book)