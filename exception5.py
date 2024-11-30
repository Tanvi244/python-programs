def main():

    Ans = 0

 

   
    

    try:
        print("enter first no:") 
        No1 = int(input())

        print("enter sec no:")
        No2 = int(input())
        Ans = No1 / No2



    except ZeroDivisionError as zobj:
        print("exception occured:",zobj)

    except ValueError as vobj:
        print("exceoption occured:",vobj)#nahi yet error sort ya vakyane ka asa hota

    except Exception as eobj:
        print("exception:",eobj)
    

    print("division : ",Ans)

if __name__ == "__main__":
    main()
       
        
