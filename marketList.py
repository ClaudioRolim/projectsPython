import os

listProduct = []
valueProduct = []
shopList = ''

while True:
    optionsList = input(
        """
    ################ MARKET SHOPPING LIST ############## 
    [1]INSERT 
    [2]DELETE
    [3]LIST 
    [4]OUT\n
    ENTER OPTION: """)
    try:
        if optionsList == '1':
            os.system('clear')
            item = input('Which product do you want to add?\n==> ')
            listProduct.append(item)
            value = float(input('Which price do you want to add?\n==> '))
            valueProduct.append(value)
            print("{}\t\t{:.2f}".format(item, value))

        if optionsList == '2':
            os.system('clear')
            for index, name in enumerate(listProduct):
                print(index, name.upper())
            for i in listProduct:
                removeItem = int(input('Which product do you want to remove?\n==> '))
                del (listProduct[removeItem])
                del (valueProduct[removeItem])

                if len(listProduct) == 0:
                    print('Empty List.')
                else:
                    deleted = f"{index}\t\t{name}\t\t{value}"
                    print(deleted)

        if optionsList == '3':
            os.system('clear')
            if len(listProduct) == 0:
                print('Empty List.')
            else:
                for item, value in zip(listProduct, valueProduct):
                    shopList = f'\n{item.upper()}\t\tU$ {value:.2f}'
                    print(shopList)

        if optionsList == '4':
            print('Out list.')
            os.system('clear')
            exit(0)

    except IndexError:
        print("Out of range.")
        continue
    except ValueError:
        print('Incorrect value...')
        continue
    except TypeError:
        print('Please, enter a number.')
        continue
    except NameError:
        print("Please, enter a number.")
        continue
    finally:
        os.system('clear')
