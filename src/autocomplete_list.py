
def autocomplete_list(input: str , master_list: list) -> list:
    result = []
    if not master_list:
        return []
    for word in master_list:
        if word.lower().startswith(input.lower()):
            result.append(word)
    return result

"""
def autocomplete_list(input: str, master_list: list) -> list:
    return [word for word in master_list if word.lower().startswith(input.lower())] if master_list else []
"""