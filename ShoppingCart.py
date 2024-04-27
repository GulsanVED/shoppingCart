class ShoppingCart:
    items = [['jeans  ','750 ',15],
             ['T-shirt','250 ',10],
             ['Shirt  ','450 ',20],
             ['Trouser','350 ',5]]
    
    # def __init__(self):
    #     self.userCart = []
    userCart = []
    def viewShopItems(self):
        print("\nItem  ","Price","Quantity")
        for item in ShoppingCart.items:
            print(item[0],item[1],item[2])

    def addToCart(self):
        print("What do you want to add to the cart:")
        print("\n1.Jeans 2.T-shirt 3.Shirt 4.Trouser")
        choosen_item,qty = input("\nEnter the number and quantity of the item you want to add like '1' '3': ").split(" ")
        choosen_item = int(choosen_item)
        qty = int(qty)
        if ShoppingCart.items[choosen_item-1][2] - qty >0:
            ShoppingCart.userCart.append([(ShoppingCart.items[choosen_item-1][0]).strip(),qty,ShoppingCart.items[choosen_item-1][1]])
            print("Item added to cart")
            ShoppingCart.items[choosen_item-1][2] = ShoppingCart.items[choosen_item-1][2] - qty
        else:
            print("Item is not in the stock")

    def removeItem(self):
        if ShoppingCart.userCart == []:
            print("There is no item in the cart")
        else:
            print(ShoppingCart.userCart)
            ri = input("\nEnter name of the item you want to remove:")
            for i in ShoppingCart.userCart:
                if ri in i:
                    ShoppingCart.userCart.remove(i)

            print("Item has been removed from Cart")
        
    def viewCart(self):
        total = 0
        if ShoppingCart.userCart == []:
            print("There is no item in the cart")
        else:
            print("\nItem","Quantity", "Price")
            for item in ShoppingCart.userCart:
                print(f"{item[0]}  {item[1]}    {item[2]}")
                total = total + int(item[1]) * int(item[2])
            print("Total = ",total)
        

def main():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        print("\nWhat you want: ")
        print("1.View all the items available in shop\n2.Add items to cart\n3.Remove items from cart\n4.View Cart")
        ch = int(input("Enter your Choice: "))
        match ch:
            case 1:
                shop_object = ShoppingCart()
                shop_object.viewShopItems()

            case 2:
                user_cart_object = ShoppingCart()
                user_cart_object.addToCart()

            case 3:
                remove_object = ShoppingCart()
                remove_object.removeItem()

            case 4:
                viewCart_object = ShoppingCart()
                viewCart_object.viewCart()

            case default:
                print("Invalid Entry!")
        print("\nDo you want to continue?:\nPress Y for Yes and N for No")
        flag = input("")

main()