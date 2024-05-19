def year_suffix(years):
    if 11 <= years % 100 <=19:
        return 'лет'
    elif years % 10 == 1:
        return 'год'
    elif 2<= years %10 <=4 :
        return 'года'
    else:
        return 'лет' 