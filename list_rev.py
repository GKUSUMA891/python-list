#reverse the list
#using reverse ()
list=[91,20,340,50,60,80]
print("before",list)
list.reverse()
print("after",list)
#using slising
list_name=[91,20,34,5,6,80]
print("before",list_name)
list1=list_name[::-1]
print("after",list1)
#using fun 
def reverse(list):
    list=[12,34,56,78,90]
    print("before reverse",list)
    list.reverse()
    return list
print(reverse(list))

