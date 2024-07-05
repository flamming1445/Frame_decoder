# This has been created to convert c files list into easisly readable frame to then decode 

Source_folder="trame_lists"
Results_folder="results"

def Get_data_from_c_file(file_source):
    content=""
    with open(file_source, 'r') as file:
        content = file.read()          
    return content

def Get_next_line(content,line_lenght):
    i = 0
    line_content=""
    j = 0
    while j < line_lenght+1:
        line_content=""
        while i < len(content) and content[i] != '\n':
            line_content += content[i]
            i+=1
        i+=1
        j+=1
    return line_content

def Convert_c_lists_to_raw_data(file_source,file_destination):
    content = Get_data_from_c_file(file_source)
    i = 0
    while i < 200 :
        line = Get_next_line(content,i)
        if line == "\n":
            i+=1
        if line[0] == '/':
            i+=1
        else:
            return 0
    return 0

Convert_c_lists_to_raw_data("../"+Source_folder+"/test.c","")




