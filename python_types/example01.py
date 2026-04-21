goods = []

g1 = {"name":"Good1","description":"Best good for all","price":1000,"weight":10,"height":30,"width":20}
g2 = {"name":"Good2","description":"Wearst good of all","price":100,"weight":1,"height":35,"width":25,"list":[12,34,5]}

goods.append(g1)
goods.append(g2)


gd=[{"name":"Good1","description":"Best good for all","price":1000,"weight":10,"height":30,"width":20},{"name":"Good2","description":"Wearst good of all","price":100,"weight":1,"height":35,"width":25}]

gd1 = []
gd1.append({"name":"Good1","description":"Best good for all","price":1000,"weight":10,"height":30,"width":20})
gd1.append({"name":"Good1","description":"Best good for all","price":1000,"weight":10,"height":30,"width":20})


# print(g1)
# print(f'{g1["name"]} - {g1["price"]}')

# print(goods)
# print(goods[1]["name"])


for i in range(len(goods)):
    print(f'{goods[i]["name"]} - {goods[i]["price"]}')

eur_uah = {"ccy":"EUR","base_ccy":"UAH","buy":"51.45000","sale":"52.45000"}
# print(eur_uah["sale"])

api_pb = [{"ccy":"EUR","base_ccy":"UAH","buy":"51.45000","sale":"52.45000"},{"ccy":"USD","base_ccy":"UAH","buy":"43.85000","sale":"44.45000"}]

for i in range(len(api_pb)):
    print(f'{api_pb[i]["ccy"]} - {api_pb[i]["buy"]}')







