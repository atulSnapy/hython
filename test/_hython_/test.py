import im      # line-1
try:
          # line-2
    def मुख्य():      # line-3
        print("STARTING")      # line-4
          # line-5
        क = input("क का मुल्य :")      # line-6
        ख = input("ख का मुल्य :")      # line-7
          # line-8
        print("READ DONE")      # line-9
          # line-10
        क = int(क)      # line-11
        ख = int(ख)      # line-12
          # line-13
        print("ADD DONE")      # line-14
          # line-15
        print("क+ख=", क+ख)      # line-16
          # line-17
        print("EXITING")      # line-18
        im.yay()      # line-19
        print("DONE")      # line-20
          # line-21
    मुख्य()      # line-22

except Exception as e:
    print(e)