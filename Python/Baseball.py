class favPlayer():
    def name(self):
        print("My favPlayer is Kershaw")
    def position(self, positionString):
        print(f"Kershaw's position is {positionString}")
        
class favPlayer2(favPlayer):
    def name(self):
        favPlayer.name(self)
    def position(self, positionString):
        print(f"Now he is a {positionString}")
        
def main():
    f = favPlayer()
    f2 = favPlayer2()
    f.name()
    f.position("pitcher")
    f2.name()
    f2.position("DH")
    
main()
