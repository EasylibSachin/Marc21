input_string1 = "01041cam  2200265 a 4500001002000000003000400020005001700024008004100041010002400082020002500106020004400131040001800175050002400193082001800217100003200235245008700267246003600354250001200390260003700402300002900439500004200468520022000510650003300730650001200763^###89048230#/AC/r91^DLC^19911106082810.9^891101s1990####maua###j######000#0#eng##^##$a###89048230#/AC/r91^##$a0316107514 :$c$12.95^##$a0316107506 (pbk.) :$c$5.95 ($6.95 Can.)^##$aDLC$cDLC$dDLC^00$aGV943.25$b.B74 1990^00$a796.334/2$220^10$aBrenner, Richard J.,$d1941-^10$aMake the team.$pSoccer :$ba heads up guide to super soccer! /$cRichard J. Brenner.^30$aHeads up guide to super soccer.^##$a1st ed.^##$aBoston :$bLittle, Brown,$cc1990.^##$a127 p. :$bill. ;$c19 cm.^##$a\"A Sports illustrated for kids book.\"^##$aInstructions for improving soccer skills. Discusses dribbling, heading, playmaking, defense, conditioning, mental attitude, how to handle problems with coaches, parents, and other players, and the history of soccer.^#0$aSoccer$vJuvenile literature.^#1$aSoccer.^\\"
input_string2 = "001002000000003000400020005001700024008004100041010002400082020002500106020004400131040001800175050002400193082001800217100003200235245008700267246003600354250001200390260003700402300002900439500004200468520022000510650003300730650001200763^"
bold_text = "\033[1m"
reset_style = "\033[0m"

def findCaret(input_string1):
    return input_string1.find('^')


def leaderData(leader):
    leader_len=len(leader)
    print(f"{bold_text}Leader :{reset_style}\n{leader}\n{bold_text}Leader length :{reset_style}{leader_len}\n")


global directory_dict
directory_dict={}

def dirData(directory):
    dir_len=len(directory)
    print(f"{bold_text}Directory{reset_style} :\n{directory}\n{bold_text}Directory length :{reset_style}{dir_len}")
    j=1
    k=0
    for i in range(0,dir_len,12):
        # print(directory[i:i+12])
        current_dir=directory[i:i+12]
        #directory
        directory_dict[j]=[current_dir,current_dir[k:k+3],current_dir[k+3:k+7],current_dir[k+7:]]
        j+=1
    print(f'{bold_text}Directory dictionary :{reset_style}',directory_dict,'\n')

global variable_field_dict
variable_field_dict={}

def variableFieldData(variable_field):
    variable_field_len=len(variable_field)
    print(f"{bold_text}Variable_field{reset_style} :\n{variable_field}\n{bold_text}Variable field length :{reset_style}{variable_field_len}")
    c=1
    for curr_item in directory_dict.keys():
        curr_item_len=int(directory_dict[curr_item][2])
        for j in range(0,variable_field_len,curr_item_len):
            variable_field_dict[c]=variable_field[1:curr_item_len]
            variable_field=variable_field[curr_item_len:]
            c+=1
            break
    print(f'{bold_text}Variable field dictionary :{reset_style}',variable_field_dict,'\n')


def printWholeData():
    for i in directory_dict.keys() and variable_field_dict.keys():
        print(f'{i}: ',end='')
        for j in range(len(directory_dict[i])):
            print(directory_dict[i][j],end=' ')
        print(f'{variable_field_dict[i]}\n')
            


    

    

def leaderDirVarfields(input_string1):
    leader=input_string1[0:24]
    no_of_dirs=(findCaret(input_string1)-24)//12
    directory=input_string1[24:24+no_of_dirs*12]
    variable_field=input_string1[24+no_of_dirs*12:]
    leaderData(leader)
    dirData(directory)
    variableFieldData(variable_field)


total_length_1_record=len(input_string1)
print("Total length of Marc record(1) :",total_length_1_record,"\n")
leaderDirVarfields(input_string1)
printWholeData()

