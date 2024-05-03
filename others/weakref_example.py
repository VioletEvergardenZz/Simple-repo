import weakref

# object 被弱应用
players=weakref.WeakValueDictionary()
# players=weakref.WeakKeyDictionary()
class player:
    
    # class 定义了__slots__这个member 这个class object就不支持弱引用了
    # __slots__=['id']
    __slots__=['id','__weakref__']
    def __init__(self):
        for i in range(1000):
            if i not in players:
                self.id=i
                break
        players[self.id]=self

def game():
    p1=player()
    p2=player()
    # print(dict(players))

for _ in range(10):
    game()

print(dict(players))