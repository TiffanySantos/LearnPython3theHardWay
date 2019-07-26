import mystuff
mystuff.apple()
print(mystuff.tangerine)

class Mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between."

    def apple(self):
        print("I a classy apples!")

#instantiate, similar to call a function but you're calling a class instead
thing = Mystuff()
thing.apple()
print(thing.tangerine)