year_str = input('あなたの生まれ年を西暦4桁で入力してください:')
year = int(year_str)
number_of_eto = (year + 8) % 12
eto_tuple = ('ねずみ年',
            'うし年',
            'とら年',
            'うさぎ年',
            'たつ年',
            'へび年',
            'うま年',
            'ひつじ年',
            'さる年',
            'とり年',
            'いぬ年',
            'いのしし年',)
eto_name = eto_tuple[number_of_eto]
print('あなたの干支は',eto_name,'です。')
