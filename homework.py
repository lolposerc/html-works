contacts = {}

def findFromName(name):
    return contacts.get(name)

def deleteFromName(name):
    return contacts.pop(name)

def addContact(name,phone):
    if findFromName(name):
        print(f"Телефон контакта: '{name}' успено изменён на: '{phone}'.")
    else:
        print(f"Контакт '{name}' успешно добавлен!")
    contacts[name] = phone

print("="*40)
print()

addContact("Иван","+7-123-456-78-90")
addContact("Мария","+7-987-654-32-10")
addContact("Алексей","+7-111-222-33-44")

print()
print("="*40)
print()

contactFind = findFromName("Иван")

if contactFind:
    print(f"Телефон: '{contactFind}' Найден по имени Иван!")
else:
    print(f"Телефон не был найден по имени Иван!")


contactDel = deleteFromName("Иван")
print(f"Контакт: 'Иван' Удалён!")

print()
print("="*40)
print()

addContact("Алексей","+7-444-333-222-11")

print()
print("="*40)
print()

print("Все контакты:")
print()

for name, phone in contacts.items():
    print(f"    Имя: '{name}',Телефон: '{phone}'")

print()
print("="*40)
