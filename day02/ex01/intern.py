class Intern:
    def __init__(self,name = "My name? I'm nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return f'{self.name}'


    class Coffee:
        def __str__(self):
            return f'This is the worst coffee you ever tasted.'

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')

    def make_coffee(self):
        Intern.Coffee()    

def main():
    p0 = Intern()
    p1 = Intern('Mark')
    print(p0)
    print(p1)
    try:
        p0.work()
    except Exception as e:
        print(e)
        print(p1.make_coffee())        


if __name__ == '__main__':
    main()