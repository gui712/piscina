import sys 
import os

def curriculum(file):
    content = open(file, 'r').read()
    content_set = open('settings.py', 'r').read()

    new_dict = {}

    for i in filter(None, content_set.split('\n')):
        new_dict[i.split('=')[0].strip(" '")] = i.split('=')[1].strip(" '")

    text = content.format(**new_dict)

    file_name = file.replace('.template', '.html')

    output_file = open(file_name,'w')
    output_file.write(text)


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        sys.exit("Invalid Number of Arguments")
    if not(sys.argv[1].endswith('.template')):
        sys.exit("Invalid Extension")
    if not(os.path.isfile(sys.argv[1])):
        sys.exit("File Does Not Exist")    
    curriculum(sys.argv[1])
