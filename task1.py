student={"rudra":95,"kiran":80,"alice":85}

c=0

while(c<3):
    try:
        print("--------------------------------------")
        name=input("Enter the students name: ")
        c=c+1
        name=name.lower()
        marks=student[name]
        print(f"{name}'s marks: {marks}")
        break
    except KeyError:
        print(f"Student {name} not found")
        print("Enter valid name")
        print(f"You have only {3-c} chances")
    finally:
        print("--------------------------------------")
        
