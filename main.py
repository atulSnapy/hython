import sys, subprocess
import source_code as sc

def transpile(file_name):
    ids             = get_ids()
    source_file     = open(file_name, 'rb')
    transpiled_file = open(file_name.split('.')[0]+"_.py", 'wb')

    transpiled_file.write("try:\n".encode('utf-8'))

    line_number     = 0
    indent_for_trsanplied = "    "
    for line in source_file:
        line_number += 1
        line = line.decode('utf-8')
        # print(line)
        source_code = sc.Source_Code(line, line_number)
        source_code.find_string()
        source_code.find_comments()
        for en_word, hi_word in ids:
            source_code.replace(hi_word, en_word)
        transpiled_code = indent_for_trsanplied+source_code.source_line.rstrip()+"      # line-"+str(source_code.source_line_number)+"\n"
        transpiled_file.write(transpiled_code.encode('utf-8'))
    
    transpiled_file.write("\nexcept Exception as e:\n    print(e)".encode('utf-8'))
    transpiled_file.close()
    source_file.close()

def get_ids():
    ids  = []
    file = open('id.csv', 'rb')

    for line in file:
        ids.append(tuple(line.decode('utf-8').split()))
    file.close()
    return ids


def main():

    if sys.argv[1] == "t":
        for i in range(2, len(sys.argv)):
            transpile(sys.argv[i])
            print("...", sys.argv[i])
    else:
        file_name = sys.argv[1]
        subprocess_argv = ["python3",file_name.split('.')[0]+"_.py"]
        subprocess_argv.extend(sys.argv[2:])

        transpile(file_name)
        subprocess.call(subprocess_argv)

main()