import sys
# Main of the program


def main():
        first_argument = int(sys.argv[1])
        second_argument = int(sys.argv[2])
        print(add_func(first_argument,second_argument))

def add_func(x,y):
        new_numb = x+y
        return new_numb

main()