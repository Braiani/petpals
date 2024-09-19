from Application import Application

class Main(Application):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.mainloop()

if __name__ == "__main__":
    root = Main()

    root.start()