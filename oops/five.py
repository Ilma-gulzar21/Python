
class player:
    player_count=0

    def __init__(self,name,level):
        self.name=name
        self.level=level
        player.player_count=self.player_count+1

    def display(self):
        print("name = ",self.name)
        print("level = ",self.level)

p1=player("ilma",10)
p2=player("aliya",12)
p3=player("anas",18)
p4=player("misbah",9)
print("total player = ",player.player_count)

