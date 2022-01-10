import os 
from subprocess import Popen, PIPE 

def add_user_to_group():
    username = input("Enter user to be added to group: ")
    output = Popen('groups', stdout=PIPE).communicate()[0] 
    print('Enter a list of groups to add user to')
    print('List should be separated by spaces, ex:\r\n group1 group2')
    print(f'Available groups are:\r\n {output}')  
    chosenGroups = input('Groups: ')
    output = output.split() 
    chosenGroups = chosenGroups.split()
    print('Add to:')
    found = True 
    groupString = ''
    
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print(f'- Existing Group {grp}')
                groupString = groupString + grp + ','
        if found == False:
            print(f'- New Group: {grp}')
            groupString = groupString + grp + ','
        else:
            found = False 

    groupString = groupString[:-1] + ' '

    while True:
        print(f'Add user {username} to these groups? (Y/N)')
        confirm = input('').upper()
        if confirm == 'N':
            break
        if confirm == 'Y':
            os.system(f'sudo usermod -aG {groupString} {username}') 
            break 