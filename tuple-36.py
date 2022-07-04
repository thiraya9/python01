tupleFruits = ("apple","banana","cherry") #Tuple
listFruits = ["apple","banana","cherry"] #List
print(tupleFruits)
print(listFruits)
#เปลี่ยนค่าในtuple
x=list(tupleFruits)#แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tupleFruits=tuple(x)
print("เปลี่ยนค่าtiple:",tupleFruits)
#เพิ่มค่าในtuple
x=list(tupleFruits)
x.append("melon")
tupleFruits=tuple(x)
print("เพิ่มค่าในtuple:",tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits=tuple(x)
print("ลบค่าในtuple:",tupleFruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitVege=tupleFruits+vege
print("join tuple:",fruitVege)
x = range(3,6)#จะหยุดก่อนค่าstop
for n in x:
    print("range x:",n)
y = range(3,20,2)
for m in y:
    print("range y:",m)
#นางสาวฐิรญา ร่่างเล็ก เลขที่ 36