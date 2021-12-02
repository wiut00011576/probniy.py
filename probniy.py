print('did you do Cw Submission on Time?')
answer =input("yes/no")

if answer =="yes":
    print("Full mark")
    exit(0)

else:
    print('Within 24 hours?')

    answer =input("yes/no")
    if answer =="yes":
        print("is there a valid reason for Late Submission?")
        if answer == "yes":
            print("MC\nAccepted?")
            answer = input("yes/no ")
            if answer == "yes":
                print('Full Mark')
            else:
                print("-10 mark but not below 40")

        else:
            print("-10 mark but not below 40")


    else:
        print("Submited within 5 days?")
        answer =input("yes/no ")

        if answer == "yes":
            print("Is there a valid reason?")
            answer = input("yes/no ")
            
            if answer == "yes":
                print("MC late submission\n Accepted?")

                answer = input("yes/no ")

                if answer == "yes":
                    print("full mark")
                else:
                    print("Mark=0")
            
            else:
                print("Mark=0")


        else:
            print("Is there a valid reason?")
            answer =input("yes/no")
            if answer == "yes":
                print("MC(non-deferral deadline)\nAccepted\nDeferral reassessment")

            else:
                print("Mark=0")
  
