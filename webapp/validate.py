def sketchpad_validate(title, description, status):
    errors = {}
    if not title:
        errors["title"] = "Поле обязательное"
    elif len(title) > 50:
        errors["title"] = "Должно быть меньше 50 символов"
    if not status:
        errors["status"] = "Поле обязательное"
    elif len(status) > 20:
        errors["author"] = "Должно быть меньше 50 символов"
    if not description:
        errors["description"] = "Поле обязательное"
    elif len(description) > 3000:
        errors["description"] = "Должно быть меньше 3000 символов"
    return errors
