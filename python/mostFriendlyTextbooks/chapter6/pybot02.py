bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'さようなら': 'サヨウナラ',
}

while True:
    command = input('pybot> ')
    response = ''
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            break
    if not response:
        response = '何を言っているかわからない'
    print(response)

    if 'さようなら' in command:
        break
