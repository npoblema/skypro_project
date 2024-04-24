from src.masks import masks_account, masks_card


def mask_card_or_account_number(data: str) -> str:
    """accepts strings — both the card type and the card number.
    returns the original strings with encrypted card numbers"""
    data_split = data.split()
    if "Счет" in data:
        return f"Счет {masks_account(data_split[-1])}"
    else:

        return f"{' '.join(data_split[:-1])} {masks_card(data_split[-1])}"


def get_new_type_of_date(date: str) -> str:
    """returns strings with date"""
    type_of_date = date.split("T")
    date_ = type_of_date[0].split("-")
    return f"{date_[2]}.{date_[1]}.{date_[0]}"
