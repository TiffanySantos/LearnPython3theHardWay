#create class

class song(object):
#init class with __init__(self) function
    def __init__(self, lyrics):
        self.lyrics = lyrics
#add class function (somthing this thing does)
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# add in as many variables as you want which can be used when class fucntion is called
happy_bday = song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])

bulls_on_parade = song(["They rally around tha family",
                    "With pockets full of shells"])    

la_cucaracha = song(["La cucaracha, la cucaracha",
                    "Ya no puede caminar",
                    "Porque no tiene, porque le falta",
                    "Marijuana para fumar.."])         

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

la_cucaracha.sing_me_a_song()