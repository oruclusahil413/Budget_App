from Source_A.Classes import Category

def create_spend_chart(categories):

    title="Percentage spent by category"
    food = Category('Food')

    food.deposit(1000,'initial deposit')
    food.withdraw(10.15,'groceries')
    food.withdraw(15.89,'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)

    print(food.get_balance())

    print(clothing.get_balance())
