from src.widget import types_cards_and_accounts, get_date

number_card_or_account = input("Введите тип карты или счета и их номер ")
print(types_cards_and_accounts(number_card_or_account))

curr_date = input("Введите строку с датой ")
print(get_date(curr_date))
