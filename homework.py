emails = [
    "user1@example.com",
    "user2@example.com", 
    "user1@example.com",  # Дубликат
    "user3@example.com",
    "user2@example.com",  # Дубликат
    "admin@example.com",
    "user4@example.com"
]

EmailDuplicates = set(emails)

print()
print("="*40)
print()

print(f"Уникальные email: {EmailDuplicates}")

print()

print(f"Дубликатов было удалено: {len(emails)-len(EmailDuplicates)}")

print()


HaveAdminEmail = False

for email in EmailDuplicates:
    if email == "admin@example.com":
        HaveAdminEmail = True
        break

if HaveAdminEmail == True:
    print(f'email: "admin@example.com" есть в списке')
else:
    print(f'email: "admin@example.com" нет в списке')

print()
print("="*40)
print()
