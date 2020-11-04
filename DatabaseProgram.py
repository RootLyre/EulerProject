from itertools import islice 
import re

def main():
    running = True
    while(running):
        val = input("\nWhat would you like to do?: \n" 
        "Enter a new person? Press 1 \n"  
        "Search for a person? Press 2 \n" 
        "Edit information? Press 3 \n"
        "Quit the program? Press 0 \n"  
        "Input: ")

        print(val)
        name = " "
        gender = " "
        age = " "
        occupation = " "
        #Check input
        file_path = 'Database.txt'
        if val not in ["0", "1", "2", "3"]:
           print('\n' "THIS IS NOT A VALID INPUT. PLEASE TRY AGAIN")
        #Edit Text File by Inserting åa new Person
        if(val == "0"):
            running = False
            print("Goodbye.")
        if(val == "1"):
            with open(file_path, 'a+') as f:
                print('\n' "Please enter the following information:" )
                name = input("Enter name: ")
                gender = input("Gender: ")
                age = input("Age: ")
                occupation = input("Occupation: ")

                #Write to File
                f.write(name)
                f.write("\n" + gender)
                f.write("\n" + age)
                f.write("\n" + occupation + "\n\n")
                f.close()
        #Search Feature
        
        if(val == "2"):
            #Counter: if the word appears more than once
            counter = 0
            names = []
            with open(file_path, 'r+') as f:
                searchFor = input("Who are you looking for?" '\n')
                lines = f.readlines()
                for line in lines:
                    if re.search(searchFor, line):
                        print("\nPerson(s) Found.")
                        print("Search Result #" + str(counter + 1))
                        counter += 1
                        names.append(line)
                        print(line)
                if(counter > 1):
                    number = input("Input the Search Result # of the person you wish to view: ")
                    lines = f.readlines()
                    print("Name being looked for: ", names[int(number)-1])

                #Reset the file pointer
                f.seek(0)
                #Cant do a "for line in lines" while inside another "for line in lines"
                count = 0
                lines = f.readlines()
                for line in lines:
                    if (re.search(names[int(number)-1], line)):
                        #Prepping to get next few lines that contain the person's info
                        count = 3
                        print(line)
                    if(count >= 0):
                        print(line)
                        count-=1
            f.close()

        
        #Edit Information
        if(val == "3"):
            newInfo = ""
            new_file_content = ""
            lineNumber = 0
            found = False
            with open(file_path, 'r+') as f:
                searchFor = input("Who are you looking for?" '\n')
                #Get line numbers as we run through this
                #Helps increment and come back to edit info for Gender/Age/Occupation
                #By the time it finds the name, its ALREADY on the Gender line
                #So Name must be line-1, age line+1, occupation line+2 
                for i, line in enumerate(f, 1):
                    if searchFor in line:
                            print("Did you mean this person?", line)
                            editThisPerson = input("Y/N \n")
                            if(editThisPerson == "Y"):
                                lineNumber = i
                                whatIsChanging = input("What info would you want to change? Name / Gender / Age / Occupation \n")
                                if(whatIsChanging == "Name"):
                                    newInfo = input("What is their new name? ")
                                    lineNumber-=1
                                elif(whatIsChanging == "Gender"):
                                    newInfo = input("What is their new gender? ")
                                elif(whatIsChanging == "Age"):
                                    newInfo = input("What is their new Age? ")
                                    lineNumber+=1
                                elif(whatIsChanging == "Occupation"):
                                    newInfo = input("What is their new Occupation? ")
                                    lineNumber+=2
                                else:
                                    print("You did not enter a valid option.")
            
                #Make sure all lines are copied
                #Got the info from previous Read
                #Now to copy / Edit the necessary info
                #This needs to be indented so the file is still open from before
                f.seek(0)
                list_of_lines = f.readlines()
                list_of_lines[lineNumber] = newInfo + "\n"

                overwrite_file = open(file_path, "w")
                overwrite_file.writelines(list_of_lines)
                overwrite_file.close()

        #End of main method

#-----------------------------------------------------------
main()
