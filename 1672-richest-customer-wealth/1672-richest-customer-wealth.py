class Solution(object):
    def maximumWealth(self, accounts):
        sum=[]
        total=0

        for i in range (len(accounts)):
            total=0
            for j in(accounts[i]):
                total +=j
            sum.append(total)

        return (max(sum))

      
        
        