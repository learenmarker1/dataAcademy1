
def hello_world():
    print('hello world!')

def hello_anything(string):
    print('hello '+ string)

if __name__ == '__main__':
    hello_world()

    string = input('what should i say?')

    hello_anything(string)