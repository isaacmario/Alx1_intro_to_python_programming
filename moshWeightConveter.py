weight = float(input('Enter your weight'))
unit = input('(K)gs or (L)bs')

if unit.upper() == 'K':
    converted = weight / 0.45
    print('weght in Lbs: ' + str(converted))
else:
    converted = weight * 0.45
    print('weight in Kgs: ' + str(converted))