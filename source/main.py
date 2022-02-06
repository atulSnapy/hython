import sys, subprocess
import source_code as sc
import eng_hin

VERSION = "1.0.5"


def transpile(file_name):
    ids = get_ids()
    source_file = open(file_name, "rb")
    transpiled_file = open(file_name.split(".")[0] + "_.py", "wb")

    transpiled_file.write("try:\n".encode("utf-8"))

    line_number = 0
    indent_for_trsanplied = "    "
    for line in source_file:
        line_number += 1
        line = line.decode("utf-8")
        # print(line)
        source_code = sc.Source_Code(line, line_number)
        source_code.find_string()
        source_code.find_comments()
        for en_word, hi_word in ids:
            source_code.replace(hi_word, en_word)
        transpiled_code = (
            indent_for_trsanplied
            + source_code.source_line.rstrip()
            + "      # line-"
            + str(source_code.source_line_number)
            + "\n"
        )
        transpiled_file.write(transpiled_code.encode("utf-8"))

    transpiled_file.write("\nexcept Exception as e:\n    print(e)".encode("utf-8"))
    transpiled_file.close()
    source_file.close()


def get_ids():
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


def main():
    print()
    if (len(sys.argv) == 1
        or sys.argv[1] == "--version"
        or sys.argv[1] == "--help"
        or sys.argv[1] == "--संस्करण"
        or sys.argv[1] == "--सहायता"
        or sys.argv[1] == "--मदद"
    ):
        print("hython version:", VERSION)
        print('"hython <file_name>" to run')
        print('"hython t <file_name> <other_files> .." to transpile')
        print(" ---------------------- ")
        print("हायथन संस्करण:", VERSION)
        print('"हायथन <फाईल>" रन करने हेतु।')
        print('"हायथन <फाईल> <और_फाईले> .." अनुवाद करने हेतु।')
    elif sys.argv[1] == "t" or sys.argv[1] == "अ":
        for i in range(2, len(sys.argv)):
            transpile(sys.argv[i])
            print("...", sys.argv[i])
    else:
        file_name = sys.argv[1]
        subprocess_argv = ["python3", file_name.split(".")[0] + "_.py"]
        subprocess_argv.extend(sys.argv[2:])

        transpile(file_name)
        subprocess.call(subprocess_argv)


main()

