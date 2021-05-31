from quantAPP.config import Config


class Cei:
    def __init__(self):
        config = Config()
        self.cpf = config.CPF
        self.key = config.KEY
    def get(self):
        return self.cpf, self.key


if __name__ == '__main__':
    cei = Cei()
    print(cei.get())

