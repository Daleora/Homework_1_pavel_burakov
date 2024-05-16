from src.masks import changed_account_number, changed_card_number

def types_cards_and_accounts(number_card_or_account: str) -> str:
    """Функция принимает на вход строку с информацией — тип карты/счета и номер карты/счета
    и возвращает исходную строку с замаскированным номером карты/счета
    """
    split_num = number_card_or_account.split(" ")
    if len(split_num[-1]) == 16:
        split_num[-1] = changed_card_number(split_num[-1])
    else:
        split_num[-1] = changed_account_number(split_num[-1])

    return " ".join(split_num)