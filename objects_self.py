class Duck:
    walk = 'This duck walks'
    sound = 'Quack, quack'

    def quack(self):
        print(self.sound)
    
    def move(self):
        print(self.walk)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__': main()