import os      # line-1
try:
    def yay():      # line-2
        print("YAYYY")      # line-3
        print(os.getcwd())      # line-4
        print("YAYY? GAINA")      # line-5

except Exception as e:
    print(e)