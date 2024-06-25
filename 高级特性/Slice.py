receipt1 = "物品1: 苹果  数量: 5   单价: 3.00元"
receipt2 = "物品2: 香蕉  数量: 10  单价: 2.00元"
receipt3 = "物品3: 橙子  数量: 3   单价: 5.00元"

itme_slice=slice(5,7)
price_slice=slice(21,26)

print(f'item: {receipt1[itme_slice]}, price: {receipt1[price_slice]}')
print(f'item: {receipt2[itme_slice]}, price: {receipt2[price_slice]}')
print(f'item: {receipt3[itme_slice]}, price: {receipt3[price_slice]}')

'slice传参机制和range一样'