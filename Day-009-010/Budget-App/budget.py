import math

class Category:
    # Set init function
    def __init__(self, category):
        self.catName = category
        self.ledger = list()
    
    # String representation of class
    def __str__(self):
        out = ''
        # Add name with stars
        catNameLen = len(self.catName)
        starLen = int((30-catNameLen)/2)
        for i in range(starLen):
            out += '*'
        out += self.catName
        for i in range(30-starLen-catNameLen):
            out += '*'
        out += '\n'
        
        # Add description and amount from ledger
        for obj in self.ledger:
            out += obj["description"].ljust(23)[:23]
            out += "{:.2f}".format(obj["amount"]).rjust(7) + '\n'

        # Add total balance
        out += 'Total: ' + "{:.2f}".format(self.get_balance())
            
        return out

    def deposit(self, amount, description=''):
        # Add amount to ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        # Remove amount from ledger if there is enough funds
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return  False

    def get_balance(self):
        # Get balance
        totalFunds = 0
        for obj in self.ledger:
            totalFunds += obj["amount"]
        return totalFunds

    def transfer(self, amount, category):
        # Transfer amount if there is enough balance and add descriptions
        if self.withdraw(amount, "Transfer to " + category.catName):
            category.deposit(amount, "Transfer from " + self.catName)
            return True
        else:
            return False

    def check_funds(self, amount):
        # Check funds and return true if there is enough funds
        totalFunds = 0
        for obj in self.ledger:
            totalFunds += obj["amount"]
        if totalFunds < amount:
            return  False
        else:
            return True

# Spend chart
def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    line = '    '
    spendTotal = 0
    spend = 0
    spendList = dict()
    largestName = 0

    for category in categories:
        line += '---'
        spendList.setdefault(category.catName, 0)
        if len(category.catName) > largestName:
            largestName = len(category.catName)
        for obj in category.ledger:
            if obj['amount'] < 0:
                spend += obj['amount']
        spendList[category.catName] = -spend
        spendTotal += -spend
        spend = 0
    line += '-'

    for key, val in spendList.items():
        spendList[key] = int(math.floor((val/spendTotal)*100))

    for i in range(11):
        i = (10 - i)*10
        chart += str(i).rjust(3) + '|'
        for val in spendList.values():
            if val >= i:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    
    chart += line.rjust(len(line)) + '\n'

    for i in range(largestName):
        chart += '     '
        for key in spendList.keys():
            if i < len(key):
                chart += key[i] + '  '
            else:
                chart += '   '
        if i != largestName-1:              
            chart += '\n'

    return chart