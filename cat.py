choice = ''
while choice!=6:
    print("\n1 - Read/Open File\n2 - Create/Write File\n3 - Concatenate File\n4 - Edit File (Append)\n5 - Edit File (Prepend)\n6 - Exit")
    choice = int(input("Choice: "))
    if choice == 1:
        filename = input("Filename: ")
        with open(filename+".txt",'r') as f:
            for line in f:
                print(line, end='')
    if choice == 2:
        filename = input("Save as: ")
        content = input("File content: ")
        with open(filename+".txt",'w') as f:
            f.write(str(content))
    if choice == 3:
        final_file = input("Save to: ")
        num_files = int(input("Number of files to concatenate: "))
        file_list = list()
        for x in range(num_files):
            file = input("Filename: ")
            file_list.append(file+".txt")
        
        with open(final_file+'.txt', 'w') as outfile:
            for fname in file_list:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line + " ")
    if choice == 4:
        filename = input("Filename to edit(append): ")
        content = input("Content to add: ")
        with open(filename+".txt",'a') as f:
            f.write(" "+str(content))
    if choice == 5:
        filename = input("Filename to edit(prepend): ")
        content = input("Content to add: ")
        with open(filename+".txt",'r+') as f:
            old = f.read()
            f.seek(0)
            f.write(str(content) + " " + old)
    if choice == 6:
        print("Thanks!")
        break
    


        
