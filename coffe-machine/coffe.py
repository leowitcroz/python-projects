penny = 0.01
quarter = 0.25
nickel = 0.05
dime = 0.10
water = 1000
milk = 1000
coffe_grain = 500
cont = False
profit = 0


#coffe = 50, 18g
#latte = 200,24,150
#mocha 250 24 100





while cont == False:

    user = input('what would you like to order? coffe/latte/mocha \n')
    print('-'*20)

    if user == 'report':
        print(f' water: {water} \n coffe grains: {coffe_grain} \n milk:{milk} \n profits: {profit}')
        print('-'*20)
        


    if user == 'latte':
        if coffe_grain >= 200 and water >= 24 and milk >=150:
            pen = int(input('number of pennys: ')) * penny
            print('-'*20)
            quart = int(input('number of quarters: ')) * quarter
            print('-'*20)
            nick = int(input('number of nickels: ')) * nickel
            print('-'*20)
            dim = int(input('number of dimes: ')) * dime
            print('-'*20)
            cash = pen + quart + nick + dim 
            if cash < 2.50:
                print('not enough money, sorry')
                quit()
            else:
                water = water - 200
                coffe_grain = coffe_grain - 24
                milk = milk - 150
                profit = profit +2.50
                change = cash - 2.50
                print(f'your change is {change:.2f} \n ENJOY YOUR LATTE')
        else:
            print('not enought ingredients')
            quit()



    if user == 'coffe':
        if coffe_grain >= 50 and water >= 18:
            pen = int(input('number of pennys: ')) * penny
            print('-'*20)
            quart = int(input('number of quarters: ')) * quarter
            print('-'*20)
            nick = int(input('number of nickels: ')) * nickel
            print('-'*20)
            dim = int(input('number of dimes: ')) * dime
            print('-'*20)
            cash = pen + quart + nick + dim 
            if cash < 1.50:
                print('not enough money, sorry')
                quit()
            else:
                water = water - 50
                coffe_grain = coffe_grain - 18
                profit = profit +1.50
                change = cash - 1.50
                print(f'your change is {change:.2f} \n ENJOY YOUR COFFE')
        else:
            print('not enought ingredients')
            quit()



    if user == 'mocha':
        if coffe_grain >= 250  and water >= 24 and milk >= 100:
            pen = int(input('number of pennys: ')) * penny
            print('-'*20)
            quart = int(input('number of quarters: ')) * quarter
            print('-'*20)
            nick = int(input('number of nickels: ')) * nickel
            print('-'*20)
            dim = int(input('number of dimes: ')) * dime
            print('-'*20)
            cash = pen + quart + nick + dim
            if cash < 3.00:
                print('not enough money, sorry')
                quit()
            else:
                water = water - 250
                coffe_grain = coffe_grain - 24
                milk = milk - 100
                profit = profit + 3.00
                change = cash - 3.00
                print(f'your change is {change:.2f} \n ENJOY YOUR MOCHA')
        else:
            print('not enought ingredients')
            quit()



