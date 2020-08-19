class Category:
    ledger = []
    catName = ''
    def __init__(self, category):
        self.catName = category
    def __str__(self):
        out = ''
        catNameLen = len(self.catName)
        starLen = int((30-catNameLen)/2)
        for i in range(starLen):
            out += '*'
        out += self.catName
        for i in range(30-starLen-catNameLen):
            out += '*'
        out += '\n'

        print(self.ledger)
        
        for obj in self.ledger:
            out += obj["description"].ljust(23)[:23]
            out += str(obj["amount"]).rjust(7) + '\n'
            
        return out

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return  False

    def get_balance(self):
        totalFunds = 0
        for obj in self.ledger:
            totalFunds += obj["amount"]
        return totalFunds

    def transfer(self, amount, category):
        description = "Transfer to " + category.catName
        if self.withdraw(amount, description):
            description = "Transfer from " + self.catName
            category.deposit(amount, description)
            return True
        else:
            return False

    def check_funds(self, amount):
        totalFunds = 0
        for obj in self.ledger:
            totalFunds += obj["amount"]
        if totalFunds <= amount:
            return  False
        else:
            return True

def create_spend_chart(categories):
    str = ''

    return str

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)


print(food)