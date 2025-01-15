class Simple:

    def __init__(self, name: str):
        print("FROM SIMPLE CONSTRUCTOR")
        self.name = name

    def get_name(self) -> str:
        print("GET NAME METHOD")
        return self.name
