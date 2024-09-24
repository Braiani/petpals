from Application import Application

class Main(Application):
    def __init__(self) -> None:
        super().__init__()
        self.set_geometry(1920,1080)

    def start(self):
        self.janela.mainloop()

if __name__ == "__main__":
    root = Main()

    root.start()