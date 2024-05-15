from src.masks import changed_account_number, changed_card_number

card_number = input("Введите номер карты ")
print(changed_card_number(card_number))


account_number = input("Введите номер счета ")
print(changed_account_number(account_number))
