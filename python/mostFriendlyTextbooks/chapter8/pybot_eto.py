def eto_command(command):
    eto, year = command.split()
    eto_list = ['ねずみ年',
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
            'いのしし年',]
    eto_number = (int(year) + 8) % 12
    eto_name = eto_list[eto_number]
    response = '{}年生まれの干支は{}です。'.format(year, eto_name)
    return response
