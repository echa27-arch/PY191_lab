import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # INITIALIZE THE DISPLAY
    display = text[0:cursor] + "|" + text[cursor:]

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # LEFT ARROW
        elif key == curses.KEY_LEFT:
            if cursor > 0:
                cursor -= 1

            display = text[0:cursor] + "|" + text[cursor:]

        # RIGHT ARROW
        elif key == curses.KEY_RIGHT:
            if cursor < len(text):
                cursor += 1

            display = text[0:cursor] + "|" + text[cursor:]

        # BACKSPACE
        elif key in (8, 127, curses.KEY_BACKSPACE):
            if cursor > 0:
                text = text[0:cursor - 1] + text[cursor:]
                cursor -= 1

            display = text[0:cursor] + "|" + text[cursor:]

        # ENTER
        elif key == 10:
            text = text[0:cursor] + "\n" + text[cursor:]
            cursor += 1

            display = text[0:cursor] + "|" + text[cursor:]

        # INSERT CHARACTER
        elif 32 <= key <= 126:
            character = chr(key)

            text = text[0:cursor] + character + text[cursor:]
            cursor += 1

            display = text[0:cursor] + "|" + text[cursor:]


curses.wrapper(main)