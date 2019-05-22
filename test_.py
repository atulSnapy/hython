try:
    def मुख्य():      # line-1
        क = input("क का मुल्य :")      # line-2
        ख = input("ख का मुल्य :")      # line-3
          # line-4
        क = int(क)      # line-5
        ख = int(ख)      # line-6
          # line-7
        print("क+ख=", क+ख)      # line-8
    मुख्य()      # line-9

except Exception as e:
    print(e)