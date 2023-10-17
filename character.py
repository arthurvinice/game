class Char:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.speech = None

    def describe(self):
        print(f'{self.name} is here!')
        print(f'{self.description}')

    def set_speech(self, speech):
        self.speech = speech

    def chat(self):
        if self.speech is not None:
            print(f'[{self.name} say]: {self.speech}')
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, fight_item):
        print(f"{self.name} doesn't want to fight you.")
        return True

class Enemy(Char):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None

    def get_weakness(self):
        return self.weakness

    def set_weakness(self, weakness_item):
        self.weakness = weakness_item

    def fight(self, fight_item):
        if fight_item == self.weakness:
            print(f'You got away safely from '
                  f'{self.name} with {fight_item}')
            return True
        else:
            print(f'{self.name} smashed you, '
                  f'idiot!')
            return False
        
class Merchant(Char):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.item = 'solar relic'
    
    def get_item(self):
        user_guess = input(f"'If you say the password, I'll give this special item to fight against the monster Careful, you've got only ONE CHANCE.' The password is the result of 6+6/6. Password: ")
        if user_guess == 7:
            print(f"Well done! The item you must use it's: solar relic. Here you go. Use it wisely!")
            return True
        else:
            print(f"Wrong answer. Good luck out there, kid...")
            return False
        

        
        