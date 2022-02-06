try:
    def गुणक(वाक्य):      # line-1
        try:      # line-2
            print("===",eval(वाक्य))      # line-3
        except:      # line-4
            print("===""त्रुटि!!!!!!!!!")      # line-5
          # line-6
    def मुख्य():      # line-7
          # line-8
        print("-.-.-.-.- हायथन गणक (कैलकुलेटर) -.-.-.-.-")      # line-9
        print("-.-.-.-.- बाहर निकलनें के लिए 'ब'दबाए -.-.-.-.-")      # line-10
          # line-11
        चालू_रखे = True      # line-12
        while चालू_रखे:      # line-13
            वाक्य = ""      # line-14
            while not वाक्य:      # line-15
                वाक्य = input("::: ").strip()      # line-16
            if वाक्य != "ब":      # line-17
                गुणक(वाक्य)      # line-18
            else:      # line-19
                चालू_रखे = False      # line-20
    मुख्य()      # line-21

except Exception as e:
    print(e)