name = 'Alice'
if name == 'Alice' :
    print('Hello Alice')
    age = int(input('Hey,Alice,How old are you?'))
    if age < 18:
        print('Oh,you still are little girl.')
    elif 18 <= age <= 25:
        print('Hey,you are a teen.')
    else:
        print('You are beautiful')
else:
    print('You are not Alice,kiddo')
