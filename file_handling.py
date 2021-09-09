f = open('test.txt', 'w')
f.write('hej')
f.close()

f = open('test.txt', 'r')
print(f.read())
f.open()

with open('test.txt') as f: #stänger filen automatiskt efter intendent
        print(f.read())