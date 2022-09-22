"""Main module"""

from computer_shop import Computer, ReBuy, Shop


def main() -> None:
    print('CREATE COMPUTER')
    computer = Computer(
        "Triston XPT 3352",
        "1.4 GHz Quad‑Core Intel Core i5",
        256, 16,
        "Unix", 2016, 1400)

    print(computer)

    print('\nCOMPUTER SHOP')
    print('#' * 20)
    shop = Shop()

    shop.buy(computer)
    shop.update_price(1, 1450)
    shop.print_item(1)

    print('SELL')
    shop.sell(1)

    print('PRINT AFTER SELLING')
    shop.print_item(1)

    rebuy = ReBuy()
    rebuy.buy(computer)

    print('\nREBUY SHOP')
    print('#' * 20)

    print('REFURBISH')
    rebuy.refurbish(1, 'Linux Mint')
    rebuy.print_item(1)

    print('R SELL')
    rebuy.sell(1)

    print('PRINT AFTER R SELLING')
    rebuy.print_item(1)


if __name__ == '__main__':
    main()
