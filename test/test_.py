try:
    def मुख्य():      # line-1
        print("STARTING")      # line-2
          # line-3
        क = input("क का मुल्य :")      # line-4
        ख = input("ख का मुल्य :")      # line-5
          # line-6
        print("READ DONE")      # line-7
          # line-8
        क = int(क)      # line-9
        ख = int(ख)      # line-10
          # line-11
        print("ADD DONE")      # line-12
          # line-13
        print("क+ख=", क+ख)      # line-14
          # line-15
        print("EXITING")      # line-16
          # line-17
    मुख्य()      # line-18

except Exception as e:
    print(e)