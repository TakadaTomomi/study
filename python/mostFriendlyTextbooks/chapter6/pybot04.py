command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line[0]
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

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