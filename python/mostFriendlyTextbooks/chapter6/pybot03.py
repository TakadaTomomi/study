text_file = open('pybot.txt', encoding='utf-8')
raw_data = text_file.read()
text_file.close()
print(raw_data)