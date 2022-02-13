try:
    # प्रोग्राम 4 : साधारण ब्याज      # line-1
          # line-2
    मूल = int(input("मूलधन : "))      # line-3
    दर = int(input("वृद्धि / दर : "))      # line-4
    समय = int(input("समय : "))      # line-5
          # line-6
    ब्orज = (मूल * दर * समय) / 100      # line-7
          # line-8
    print("ब्याज : ", ब्orज)      # line-9
    print("मिश्रधन : ",  मूल + ब्orज)      # line-10

except Exception as e:
    print(e)
# Hython V : 1.1.2