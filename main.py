'''Project'''
# Номера телефонов определены следующим образом:Первым выступает международный код страны(у России - +7,
# у Великобритании - +44,у США - +1,у Германии - +49). После международного кода идет DEF-код, или префикс. Это
# негеографический, не привязанный к определенной местности идентификатор зоны, используемый в сетях подвижной
# мобильной связи. В России существует три крупные сотовые компании (Билайн,МТС,Мегафон). Именно по DEF-коду
# определяются сотовые номера по регионам России и по оператору.Компании МТС принаджелат коды 911 - Северо-запад,
# 912 - Урал, 913 - Сибирь, 914- Дальний восток,916 - Москва. У Мегафона 921 - Северо-запад, 922 - Урал,
# 923 - Сибирь, 924,934 - Дальний восток, 926,936 - Москва. У билайна же  Как можно заметить, все номера России после
# кода страны +7 начинаются с девятки. В России под мобильные сети выделены коды, начинающиеся с девятки,
# и это позволяет с легкостью определить, что вызов поступает с мобильного. Из ста DEF-кодов, сегодня не
# задействованными остается всего 18, и пока они находятся в резерве. После кода оператора идет 7-значная группа
# цифр, которая представляет собой уникальный номер абонента. По этим цифрам определить принадлежность к оператору
# или региону получится с учетов DEF-кода. На ввод подается номер телефона (например +7(913)4808282) и остаток денег на телефоне.
# Функция должна определить какой стране принадлежит номер, какому сотовому оператору и существует ли такой номер. А также определить сколько звонков
# у вас осталось.


def phonenumber(n):


    """st = n.split('(')
    areacode = st[0]
    oth = st[1]
    st1 = oth.split(')')
    prefix = st1[0]
    number = st1[1]"""
    # Определим страну
    while True:
        cntr = 0
        st = n.split('(')
        areacode = st[0]
        oth = st[1]
        st1 = oth.split(')')
        prefix = st1[0]
        number = st1[1]
        if areacode == '+7':
            cntr = 'Россия'
            break
        elif areacode == '+1':
            cntr = 'Соединенные Штаты Америки'
            break
        elif areacode == '+44':
            cntr = 'Великобритания'
            break
        elif areacode == '+49':
            cntr = 'Германия'
            break
        else:
            n = input('Введите номер телефона заново: ')
    # Определим сотового оператора
    while True:
        st = n.split('(')
        areacode = st[0]
        oth = st[1]
        st1 = oth.split(')')
        prefix = st1[0]
        number = st1[1]
        oper = 0
        if areacode == '+7':
            if int(prefix) < 920 and int(prefix) > 910:
                oper = 'МТС'
                break
            elif int(prefix) > 920 and int(prefix) < 940:
                oper = 'Мегафон'
                break
            elif int(prefix) > 962 and int(prefix) < 987:
                oper = 'Билайн'
                break
            else:
                n = input('Сотовый оператор не найден. Введите еще раз: ')
        else:
            oper = 'не найден.'
            break
    # Определим ваш регион
    while True:
        st = n.split('(')
        areacode = st[0]
        oth = st[1]
        st1 = oth.split(')')
        prefix = st1[0]
        number = st1[1]
        region = 0
        if areacode == '+7':
            if int(prefix) > 900 and int(prefix) < 1000:
                if int(prefix) == 921 or int(prefix) == 911:
                    region = 'Северо-Запад'
                    break
                elif int(prefix) == 922 or int(prefix) == 912:
                    region = 'Урал'
                    break
                elif int(prefix) == 923 or int(prefix) == 913:
                    region = 'Сибирь'
                    break
                elif int(prefix) == 914 or int(prefix) == 924:
                    region = 'Дальный Восток'
                    break
                elif int(prefix) == 916 or int(prefix) == 926 or int(prefix) == 936 or int(prefix) == 980 or int(
                        prefix) == 983 or int(prefix) == 986:
                    region = 'Москва и Московская область'
                    break
                else:
                    region = 'Остальные регионы'
                    break
            else:
                n = input('Такого региона не существует. Введите номер заново: ')
        else:
            region = 'Неизвестно'
            break


    #Преобразуем индивидуальный код к виду ***-**-**
    n1 = number[:3]
    n2 = number[3:5]
    n3 = number[5:7]
    new_number = n1 + '-' + n2 + '-' + n3
    nn = areacode + '(' + prefix + ')' + new_number

    """#Определим страну
    while True:
        if areacode == '+7':
            cntr = 'Россия'
            break
        elif areacode == '+1':
            cntr = 'Соединенные Штаты Америки'
            break
        elif areacode == '+44':
            cntr = 'Великобритания'
            break
        elif areacode == '+49':
            cntr = 'Германия'
            break
        else:
            n = input('Введите номер телефона заново: ')
    #Определим сотового оператора
    while True:
        oper = 0
        if areacode == '+7':
            if int(prefix) < 920 and int(prefix) > 910:
                oper = 'МТС'
                break
            elif int(prefix) > 920 and int(prefix) < 940:
                oper = 'Мегафон'
                break
            elif int(prefix) > 962 and int(prefix) < 987:
                oper = 'Билайн'
                break
            else:
                n = input('Сотовый оператор не найден. Введите еще раз: ')
        else:
            oper = 'не найден.'
            break
    #Определим ваш регион
    while True:
        region = 0
        if areacode == '+7':
            if int(prefix) > 900  and int(prefix) < 1000:
                if int(prefix) == 921 or int(prefix) == 911:
                    region = 'Северо-Запад'
                    break
                elif int(prefix) == 922 or int(prefix) == 912:
                    region = 'Урал'
                    break
                elif int(prefix) == 923 or int(prefix) == 913:
                    region = 'Сибирь'
                    break
                elif int(prefix) == 914 or int(prefix) == 924:
                    region = 'Дальный Восток'
                    break
                elif int(prefix) == 916 or int(prefix) == 926 or int(prefix) == 936 or int(prefix) == 980 or int(prefix) == 983 or int(prefix) == 986:
                    region = 'Москва и Московская область'
                    break
                else:
                    region = 'Остальные регионы'
                    break
            else:
                n = input('Такого региона не существует. Введите номер заново: ')
        else:
            region = 'Неизвестно'
            break"""



    m = int(input('Введите ваш остаток (в рублях): '))
    #Определим количество звонков внутри оператора и вне
    infzv = 0
    infzs = 0
    zv = m // 5
    if zv % 10 == 1 and zv != 11:
        infzv = 'Внутри оператора вы можете совершить ' + str(zv) + ' звонок'
    elif (zv % 10) > 1 and (zv % 10) < 5 and (zv < 11 or zv > 19):
        infzv = 'Внутри оператора вы можете совершить ' + str(zv) + ' звонка'
    elif zv > 10 and zv < 20:
        infzv = 'Внутри оператора вы можете совершить ' + str(zv) + ' звонков'
    elif (zv % 10) > 4 and (zv % 10) < 11:
        infzv = 'Внутри оператора вы можете совершить ' + str(zv) + ' звонков'
    elif zv % 10 == 0:
        infzv = 'Внутри оператора вы можете совершить ' + str(zv) + ' звонков'
    zs = m // 20
    if zs % 10 == 1 and zs != 11:
        infzs = 'Другим операторам вы можете совершить ' + str(zs) + ' звонок'
    elif (zs % 10) > 1 and (zs % 10) < 5 and zs < 11 and zs > 19:
        infzs = 'Другим операторам вы можете совершить ' + str(zs) + ' звонка'
    elif zs > 10 and zs < 20:
        infzs = 'Другим операторам вы можете совершить ' + str(zs) + ' звонков'
    elif (zs % 10) > 4 and (zs % 10) < 11:
        infzs = 'Другим операторам вы можете совершить ' + str(zs) + ' звонков'
    elif zs % 10 == 0:
        infzs = 'Другим операторам вы можете совершить ' + str(zs) + ' звонков'
    sr = 0
    sr = 'Ваш номер:' + nn + 'Страна:' + cntr + '.' +  'Сотовый оператор:' + oper + '.' + 'Регион:' + region + '.'
    sr = sr + '\n' + infzv
    sr = sr + '\n' + infzs
    return  sr
n = input('Введите номер телефона: ')
print(phonenumber(n))

