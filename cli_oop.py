from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, number):
        self.value = number


class Birthday(Field):
    def __init__(self, birthday):
        self.value = birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        if re.match('\d{2}.\d{2}.\d{4}', birthday):
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday sholud be in format DD.MM.YYYY")   
        

    def add_phone(self, number):
        if re.match("\d{10}", number):
            phone = Phone(number)
            self.phones.append(phone)
        else:
            raise ValueError("Phone number should have 10 digits")        
        

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
#               return f"Phone number {number} removed for {self.name.value}."
        return f"No phone number {number} found for {self.name.value}."

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
#               return f"Phone number {old_number} updated to {new_number}."
        return f"No phone number {old_number} found for {self.name.value}."

    def find_phone(self, number):
        if number in [phone.value for phone in self.phones]:
            return number
        else:
            return f"No phone number found for {self.name}"

    def __str__(self):
        if self.birthday:
            return f"Contact name: {self.name.value}, birthday {self.birthday.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name.value] = contact

    def find(self, name):
        if name in self.data:
            contact = self.data[name]
            return contact
        else:
            return f'No phone number found for {name}.'

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("95.95.2181")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("95.95.2385")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та виведення телефону для John
    john = book.find("John")
    print(john)  # Виведення: Contact name: John, phones: 1234567890; 5555555555

    # Знаходження та виведення телефону для John
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Знаходження та виlвидалення телефону для John
    john.remove_phone("1112223333")
    print(john)  # Виведення: Contact name: John, phones: 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Знаходження та виведення телефону для Jane
    jane = book.find("Jane")
    print(jane)  # Виведення: Contact name: Jane, phones: 9876543210
    # Видалення запису Jane
    book.delete("Jane")

    # Знаходження та виведення телефону для Jane
    jane = book.find("Jane")
    print(jane)  # Виведення: No phone number found for Jane.
