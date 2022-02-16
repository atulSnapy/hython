import sys, subprocess, os
from build_hython.version import VERSION
import source_code as sc
import eng_hin

class HythonLang() :

    def __init__(self) :
        self.root_path = os.getcwd()
        self.curr_path = self.root_path
        self.main_file = ""
        self.to_be_transpiled = []
        self.transpiled = []
        self.is_transpile_only = False
        self.ids = self.get_ids()
        self.transpiled_dir = "_hython_" #

        if self.show_help() == True :
            return

        self.is_transpile_only = sys.argv[1] == "t" or sys.argv[1] == "अ"
        if  self.is_transpile_only :
            main_file = sys.argv[2]
        else :
            main_file = sys.argv[1]
        
        self.to_be_transpiled.append(main_file)

        while len(self.to_be_transpiled) > 0 :
            file_name = self.to_be_transpiled.pop()
            
            valid_file_names = [
                file_name,
                file_name.split(".")[0]+".hy",
                file_name.split(".")[0]+".हाय"
            ]
            # print( os.path.exists(valid_file_names[0]), os.path.exists(valid_file_names[2]), os.path.exists(valid_file_names[2]) )
            for file in valid_file_names :
                if os.path.exists(file):
                    self.transpile(file)


        if not self.is_transpile_only :
            transpiled_main_file_path = os.path.join(self.transpiled_dir, main_file.split(".")[0] + ".py")
            subprocess_argv = ["python3", transpiled_main_file_path]
            subprocess_argv.extend(sys.argv[2:])
            print("++++++++++++++++++++RUNNING NOW"+transpiled_main_file_path)
            subprocess.call(subprocess_argv)
    
    def get_transpiled_path(self, file_name) :
        path = os.path.join(self.root_path, self.transpiled_dir)
        os.makedirs(os.path.join(path, "\\".join(file_name.split("\\")[:-1])), exist_ok = True)
        return os.path.join(self.transpiled_dir, file_name)

    def transpile(self,file_name):
        source_file = open(file_name, "rb")
        new_path = self.get_transpiled_path(file_name) # when transpiled_dir is not "" then use this
        # TO DO : Need to tranpile into __hython__ and remove _ from the end  of transpled files
        transpiled_file = open(new_path.split(".")[0] + ".py", "wb")

        try_written = False

        line_number = 0
        for line in source_file:
            line_number += 1
            line = line.decode("utf-8")
            # print(line)
            source_code = sc.Source_Code(line, line_number)
            indent_x = ""

            # get import names if any
            import_name = source_code.get_import().strip()
            if import_name != "" :
                self.to_be_transpiled.append(import_name + ".py")
                transpiled_code = source_code.source_line
            else :
                if not try_written :
                    # if no import write the try statement
                    transpiled_file.write("try:\n".encode("utf-8"))
                    try_written = True
            
                indent_x = "    "
                source_code.find_string()
                source_code.find_comments()
                for en_word, hi_word in self.ids:
                    source_code.replace(hi_word, en_word)
                    
                transpiled_code = (
                    indent_x
                    + source_code.source_line.rstrip()
                    + "      # line-"
                    + str(source_code.source_line_number)
                    + "\n"
                )
            transpiled_file.write(transpiled_code.encode("utf-8"))

        transpiled_file.write("\nexcept Exception as e:\n    print(e)".encode("utf-8"))
        last_line = "\n# Hython V : " + VERSION
        transpiled_file.write(last_line.encode("utf-8"))
        transpiled_file.close()
        source_file.close()

        self.transpiled.append(file_name)


    def show_help(self) :
        if (len(sys.argv) == 1
            or sys.argv[1] == "--version"
            or sys.argv[1] == "--help"
            or sys.argv[1] == "--संस्करण"
            or sys.argv[1] == "--सहायता"
            or sys.argv[1] == "--मदद" # might remove this
        ):
            print("hython version:", VERSION)
            print('"hython <file_name>" to run')
            print('"hython t <file_name> <other_files> .." to transpile')
            print(" ---------------------- ")
            print("हायथन संस्करण:", VERSION)
            print('"हायथन <फाईल>" रन करने हेतु।')
            print('"हायथन <फाईल> <और_फाईले> .." अनुवाद करने हेतु।')
            return True
        return False

    def get_ids(self):
        # with open("id.csv", "r") as file:
        #     id_string = file.read()
        id_string = eng_hin.ids
        id_pair_arr = id_string.strip().split("\n")
        ids = []

        for id_pair in id_pair_arr:
            ids.append(tuple(id_pair.split()))

        # this will sort in asending order accoding to hindi words
        ids.sort(key=lambda x: len(x[1]), reverse=True)
        # this will make sure that "=" appers before "<-"
        # ids[-1], ids[-2] = ids[-2], ids[-1]
        return ids


HythonLang()