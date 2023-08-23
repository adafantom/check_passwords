import urwid


def has_digit(password):
    return any(elem.isdigit() for elem in password)


def is_very_long(password):
    return len(password) > 12 


def has_letters(password):
  return any(elem.isalpha() for elem in password)


def has_upper_letters(password):
    return any(elem.isupper() for elem in password)


def has_lower_letters(password):
    return any(elem.islower() for elem in password)


def has_symbols(password):
    return any((not elem.isalpha()) and (not elem.isdigit()) for elem in password)


def on_ask_change(edit, new_edit_text):
    score = 0
    func_names = [
          is_very_long(new_edit_text),
          has_digit(new_edit_text),
          has_letters(new_edit_text),
          has_upper_letters(new_edit_text),
          has_lower_letters(new_edit_text),
          has_symbols(new_edit_text)
    ]
    for func in func_names:
      if func:
          score += 2
    reply.set_text("Рейтинг пароля: %s" % score) 


if __name__ == '__main__':
    ask = urwid.Edit('Введите ваш пароль: ', mask = "*")
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
