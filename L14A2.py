#Activity 2 - Linear Search Program
#Finding a number from a list
#Search goes from Left to Right

scores = [4,9,5,6,3,7,1,2,8,0]
#Numbers from 0 to 9

input("List: "+str(scores) +" n = 9   Linear Search - checks left to right.Press enter.")
target = int(input("Enter a number from 0 to 9 for me to find."))
input("Searching for"+ str(target) + "......Press enter to run....")
steps = 0
for score in scores:
    steps+=1
    if score == target:
        break
print("target =",target," found at position",steps," checks =",steps)

input("Compare with the best and worst cases.Press enter.")
mid = len(scores)//2
print("Best: 1 check -> 0(1)    Average:",mid,"checks -> 0(n)   Worst:9 checks -> 0(n)   Yours:",steps)

input("All three cases.Press enter.")
print("Best:0(1) Average:0(n) Worst(n) -> Big-0 = worst case = 0(n)")