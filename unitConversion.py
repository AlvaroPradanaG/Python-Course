in_weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    out_weight =  float(in_weight) * 0.454
    print(f'Your weight is {out_weight} kg.')
elif unit.upper() == 'K':
    out_weight = float(in_weight) / 0.454
    print(f'Your weight is {out_weight} lbs.')
