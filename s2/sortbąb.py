
list=[4,123,1,2,5,8,8,61,1]
class SortBubble:
    @staticmethod
    def sort(list):
        number=len(list)
        for j in range (number-1):
            for i in range (number-1-j):
                if list[i]>list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
        return list
    print(sort(list))



