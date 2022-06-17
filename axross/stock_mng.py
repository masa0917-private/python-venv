# 商品情報に関するClass
class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.worth = price * quantity
    def show(self):
        print('ID: {id} \t 個数: {quantity}\t 価格: {price}\t 総額(価格*個数): {worth}'.format(id = self.id, name = self.name, quantity = self.quantity, price = self.price, worth = self.worth))

# 在庫に関するClass
class Stock:
    def __init__(self):
        self.items_list = []

    # 商品を追加する関数
    def add(self, product):
        flag = False
        for i in self.items_list:
            if i.name == product.name:
                i.quantity += product.quantity
                i.worth += product.worth
                flag = True
                break
        if flag == False:
            self.items_list.append(product)
        print('{name} {quantity}個入庫しました'.format(name = product.name, quantity = product.quantity))

    # 商品を減らす関数
    def delete(self, product):
        flag = False
        for i in self.items_list:
            if i.name == product.name:
                flag = True
                if i.quantity >= product.quantity:
                    i.quantity -= product.quantity
                    i.worth -= product.worth
                    print('{name} {quantity}個出庫しました'.format(name = product.name, quantity = product.quantity))
                    break
                else:
                    print('個数が足りません')
        if flag == False:
            print('{name}が存在しません'.format(name = product.name))

    # 在庫情報を出力
    def print_info(self, *target):
        print('-' * 90)
        if len(target) > 0:
            for i in target:
                flag = False
                for j in self.items_list:
                    if(i == j.name):
                        flag = True
                        j.show()
                if flag == False:
                    print('{name}は存在しません'.format(name = i))
        else:
            for i in self.items_list:
                i.show()
            total_product = len(self.items_list)
            total_worth = 0
            for item in self.items_list:
                total_worth = 0
            for item in self.items_list:
                total_worth += item.worth
            print('商品種類数： {product}\n 在庫合計金額： {worth}'.format(product = total_product, worth = total_worth))
            print('-' * 90)

# 在庫情報を数量でソートする関数
    def sort_stock(self, k = 'quantity', r = False):
        if k == 'quantity':
            sorted_stock = sorted(self.items_list, key = lambda x: x.quantity, reverse = r)
        elif k == 'worth':
            sorted_stock = sorted(self.items_liste, key = lambda x: x.worth, reverse = r)
        for i in sorted_stock:
            i.show()
        print('-' * 90)
