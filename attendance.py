import pyttsx3
engine=pyttsx3.init()
class_data={39:"Abdul Sami",21:"Muhammad Hashir", 50:"Huzaifa Iftikhaaar",3:"Shahmeer Hassan"}
date=input("Enter the data: ")

for i in range(len(class_data)):
   
    print("type 0 to close...")
    roll_no=int(input("enter the roll no :  "))
    if roll_no==0:
        break
    engine.say(f"roll number {roll_no}  {class_data[roll_no]}")
    engine.runAndWait()
    status=input("Attendance status: ")
    with open(f"{date}","a") as f:
        f.write(f"roll number {roll_no}  {class_data[roll_no]} >>> {status} \n")



    

    
