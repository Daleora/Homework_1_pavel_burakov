def changed_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    """
    return f"{card_number[:4]} {card_number[5:7]}{'*' * 2} {'*' * 4} {card_number[12:]}"


def changed_account_number(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    """
    return f"{'*' * 2}{account_number[-4::]}"
