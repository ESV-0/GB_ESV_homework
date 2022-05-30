# Домашнеее задание, урок-2, задание-5

product = [57.8, 46.51, 97, 64.50, 2036, 888.20, 666.30, 17.77, 99.99, 100]

print(id(product))
product.sort()
print(product)
product.sort(reverse=True)
print(product)
print(id(product))

for price in product:
    R = int(price)
    K = (price - R) * 100
    print(f'Цена товара: {R} руб. {K:02.0f} коп.')

print('  Цены пяти самых дорогих товаров:')
product = [x for x in product[0:5]]

for price in product:
    R = int(price)
    K = (price - R) * 100
    print(f'Цена товара: {R} руб. {K:02.0f} коп.')
