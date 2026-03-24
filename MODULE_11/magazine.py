class Publication:
    def __init__(self, name):
        self.name=name

class Book(Publication):
    def __init__(self, name, author, p_count):
        super().__init__(name)
        self.author=author
        self.p_count=p_count

    def print_information(self):
        print(f"The {self.name} by {self.author} has {self.p_count} pages")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor=editor

    def print_information(self):
        print(f"The {self.name} by {self.editor}")

magazine=Magazine("Donald Duck", "Aki Hyyppä")
book=Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
book.print_information()