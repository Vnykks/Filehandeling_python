file = open ('sample.sample.txt', 'r')
content = file.read()
file.close()

print(f"Content of 'sample.txt':{content}")