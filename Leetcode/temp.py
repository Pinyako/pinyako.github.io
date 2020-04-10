def copy_string(text):
    a = ''
    s = len(text)
    for i in text:
        if i == 'o':
            print('return here')
            return
        a += i
    else:
        print(a[s-1])

if __name__ == '__main__':
    text = 'Helloworld'
    try:    
        copy_string(text)
    except Exception as e:
        print(e)
        