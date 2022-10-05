#ٌWriteD BY ME!
from subprocess import check_output
from string import ascii_uppercase
from os import system, walk, path
from colorama import Fore

CHANGED = ''

def find_drives():
	system_drives = []
	cmd = str(check_output("net share", shell=True))
	for i in ascii_uppercase:
		if i+':' in cmd:
			system_drives.append(i)
	return system_drives

def search(name, root) :
    result = []
    for root, dirs, files in walk(root) :
        for d in dirs :
            if name in d :
                result.append(path.join(root, d))
        for f in files :
            if name in f :
                result.append(path.join(root, f))
    return result

def show_list(root) :
    system('cls')
    global CHANGED
    for root, dirs, files in walk(root):
        print(Fore.CYAN+' (YoU ArE HerE)==> '+root)
        print(Fore.LIGHTGREEN_EX+'\n DireS : \n'+Fore.WHITE)
        for i in range(len(dirs)):
            if dirs[i] == CHANGED :
                print(Fore.LIGHTMAGENTA_EX+' >>'+dirs[i]+Fore.WHITE)
                CHANGED = ''
            else :
                print(' >>'+dirs[i])
        print(Fore.LIGHTGREEN_EX+'\n FileS : \n'+Fore.WHITE)
        for j in range(len(files)):
            if files[j] == CHANGED :
                print(Fore.LIGHTMAGENTA_EX+' >>'+files[j]+Fore.WHITE)
                CHANGED = ''
            else :
                print(' >>'+files[j])
        return dirs, files

system('cls')
print(Fore.CYAN+'''\n
    ███╗   ███╗ █████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗ ███████╗
    ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝ MMD FilE ManageR
    ██╔████╔██║███████║██╔████╔██║███████║██║  ██║██║   ██║█████╗  
    ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║██║   ██║██╔══╝   VersioN 1.85-WindowS
    ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝╚██████╔╝██║     
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     
\n''')
characters = ['/', '\\', ':', '*', '<', '>', '?', '"', '|']
while True :
    root = input(Fore.BLUE+'\n SelecT DrivE '+Fore.GREEN+str(find_drives())+Fore.GREEN+'==>'+Fore.WHITE).upper()
    if root in find_drives():
        break
    else :
        print(Fore.RED+'\n EnteR A CorrecT DrivE ')
root += ':\\'
dirs, files = show_list(root)
copy = ''
cut = ''
while True :
    select = input(Fore.YELLOW+'\n SelecT DirectorY, FilE OR CommanD ==>'+Fore.WHITE)

    if select == '/help' :
        print(Fore.CYAN+'''
╔══════════════════════════════════════════════════╗
|    /back    :   ReturN TO PreviuS DirectorY       |
|
|    /root    :   GO TO ThE CurrenT DrivE RooT      |
|
|    /change  :   ChangE CurrenT DrivE              |
|
|    /rename  :   RenamE A FoldeR/FilE              |
|
|    /new     :   CreatE A NeW FoldeR/FilE          |
|
|    /delete  :   DeletE A FoldeR/FilE              |
|
|    /copy    :   CopY FilE(s) TO ClipboarD         |
|
|    /cut     :   CuT A FoldeR/FilE TO ClipboarD    |
|
|    /paste   :   PstE A FoldeR/FilE FroM ClipboarD |
|
|    /clipboard:  ShowS WhatS IN ClipboarD          |
|
|    /search  :   SearcH A FoldeR/FilE              |
|
|    /tree    :   ShoW TreE OF FolderS              |
|
|    /refresh :   ReloaD DirectorY LisT             |
|
|    /exit    :   ClosE FilE ManageR                |
╚══════════════════════════════════════════════════╝''')

    elif select == '/back' :
        if root.rfind('\\') != -1 :
            slash = root.rfind('\\')
            root = root[:slash]
        else :
            root += '\\'
        if root.find('\\') == -1 :
            root += '\\'
        dirs, files = show_list(root)

    elif select == '/root' :
        slash = root.find('\\')
        root = root[:slash+1]
        dirs, files = show_list(root)

    elif select == '/change' :
        system('cls')
        while True :
            root = input(Fore.BLUE+'\n SelecT DrivE '+Fore.GREEN+str(find_drives())+Fore.GREEN+'==> '+Fore.WHITE).upper()
            if root in find_drives() :
                break
            else :
                print(Fore.RED+'\n EnteR A CorrecT DrivE ')
        root += ':\\'
        dirs, files = show_list(root)

    elif select == '/rename' :
        found = False
        name = input(Fore.BLUE+'\n SelecT DirectorY OR FilE TO RenamE ==>'+Fore.WHITE)
        if name in dirs or name in files :
            change = input(Fore.MAGENTA+'\n EnteR NeW NamE ('+Fore.RED+'WithouT /\*:><?"|'+Fore.MAGENTA+') ==>'+Fore.WHITE)
            for char in characters :
                if char in change :
                    found = True
            if not found :
                system('ren \"'+root+'\\'+name+'\" '+change)
                CHANGED = change
                dirs, files = show_list(root)
            else :
                print(Fore.RED+'\n FoldeR/FilE NamE CanT ContaiN ThiS CharacterS '+Fore.BLUE+' /\*:><?"| ')
        else :
            print(Fore.RED+'\n NO SucH A FilE OR DirectorY!\n')

    elif select == '/new' :
        found = False
        which = input(Fore.BLUE+'\n CreatE A NeW FoldeR OR FilE ? O/I :'+Fore.WHITE).upper()
        new = input(Fore.MAGENTA+'\n EnteR NamE ('+Fore.RED+'WithouT /\*:><?"|'+Fore.MAGENTA+') ==>'+Fore.WHITE)
        for char in characters :
                if char in new :
                    found = True
        if not found :
            if which == 'O' :
                if new not in files and new not in dirs :
                    system('md '+root+'\\'+new)
                    CHANGED = new
                    dirs, files = show_list(root)
                else :
                    print(Fore.RED+'\n NamE '+new+' IS AlredY ExisT!')
            if which == 'I' :
                if new not in files and new not in dirs :
                    open(root+'\\'+new , 'w').close()
                    CHANGED = new
                    dirs, files = show_list(root)
                else :
                    print(Fore.RED+'\n NamE '+new+' IS AlredY ExisT!')
        else :
            print(Fore.RED+'\n FoldeR/FilE NamE CanT ContaiN ThiS CharacterS /\*:><?"| ')

    elif select == '/delete' :
        delete = input(Fore.BLUE+'\n SelecT DirectorY OR FilE TO DeletE ==>'+Fore.WHITE)
        if delete in files :
            sure = input(Fore.MAGENTA+'\n ArE YoU SurE YoU WanT TO DeletE '+delete+' ? Y/N :'+Fore.WHITE).upper()
            if sure == 'Y' :
                system('del \"'+root+'\\'+delete+'\"')
                dirs, files = show_list(root)
            else :
                print(Fore.RED+'\n CanceleD!')
        elif delete in dirs :
            sure = input(Fore.MAGENTA+'\n ArE YoU SurE YoU WanT TO DeletE '+delete+' ? Y/N :'+Fore.WHITE).upper()
            if sure == 'Y' :
                system('rd /s /q \"'+root+'\\'+delete+'\"')
                dirs, files = show_list(root)
            else :
                print(Fore.RED+'\n CanceleD!')
        else :
            print(Fore.RED+'\n NO SucH A FilE OR DirectorY!\n')

    elif select == '/copy' :
        need = ''
        copy = input(Fore.BLUE+'\n SelecT DirectorY OR FilE TO CopY ==>'+Fore.WHITE)
        if copy in dirs or copy in files :
            chang = copy
            if copy in dirs :
                need = '\\'+copy
            copy = root+'\\'+copy
            print(Fore.GREEN+'\n SaveD IN ClipboarD!')
            cut = ''
        else :
            print(Fore.RED+'\n NO SucH A FilE OR DirectorY!\n')

    elif select == '/cut' :
        cut = input(Fore.BLUE+'\n SelecT DirectorY OR FilE TO CuT ==>'+Fore.WHITE)
        if cut in dirs or cut in files :
            chang = cut
            cut = root+'\\'+cut
            print(Fore.GREEN+'\n SaveD IN ClipboarD!')
            copy = ''
        else :
            print(Fore.RED+'\n NO SucH A FilE OR DirectorY!\n')

    elif select == '/paste' :
        if copy != '' :
            if need :
                system('md \"'+root+need+'\"')
                system('copy \"'+copy+'\" \"'+root+need+'\"')
                need = ''
            else :
                system('copy \"'+copy+'\" \"'+root+'\"')
            copy = ''
            CHANGED = chang
            dirs, files = show_list(root)
        elif cut != '' :
            system('move \"'+cut+'\" \"'+root+'\"')
            cut = ''
            CHANGED = chang
            dirs, files = show_list(root)
        else :
            print(Fore.RED+'\n ClipboarD IS EmptY!\n')

    elif select == '/clipboard' :
        if copy :
            print(Fore.GREEN+'\n'+copy)
        elif cut :
            print(Fore.GREEN+'\n'+cut)
        else :
            print(Fore.RED+'\nClipboarD IS EmptY!')

    elif select == '/search' :
        name = input(Fore.BLUE+'\n EnteR NamE TO SearcH ==>'+Fore.WHITE)
        list = search(name, root)
        if list :
            for res in list :
                res = res.replace(root, '')
                print(Fore.GREEN+res)
        else :
            print(Fore.RED+'\n NoT FounD!')

    elif select == '/tree' :
        print(Fore.MAGENTA)
        system('tree \"'+root+'\"')

    elif select == '/refresh' :
        dirs, files = show_list(root)

    elif select in dirs :
        if root[-1] != '\\' :
            root += '\\'
        root += select
        dirs, files = show_list(root)

    elif select in files :
        system('\"'+root+'\\'+select+'\"\n')

    elif select == '/exit' :
        exit()

    else :
        print(Fore.RED+'\n NO SucH A FilE OR DirectorY! NeeD "/help"?\n')