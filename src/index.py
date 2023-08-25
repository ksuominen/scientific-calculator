from tkinter import Tk, StringVar
from ui.ui import UI


def main():
    window = Tk()
    window.title("Scientific calculator")
    window.resizable(0, 0)
    window.geometry("")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
