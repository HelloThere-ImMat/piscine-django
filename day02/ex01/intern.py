class Intern: 
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def make_coffee(self):
        return Intern.Coffee()


if __name__ == "__main__":
    intern1 = Intern()
    intern2 = Intern("Mark")

    print(intern1)  # Output: My name? I'm nobody, an intern, I have no name.
    print(intern2)  # Output: Mark

    coffee = intern2.make_coffee()
    print(coffee) # Output: This is the worst coffee you ever tasted.

    try:
        intern1.work()
    except Exception as e:
        print(e)  # Output: I'm just an intern, I can't do that...