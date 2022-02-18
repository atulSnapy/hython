# import re


class Source_Code():


    def __init__(self, source_line, source_line_number):

        # this will hold the scanned source_line
        self.source_line        = source_line
        self.source_line_number = source_line_number

    # this will get list of all the imports (local and global/modules)
    def get_import(self) :
        import_name = ""
        # if the line is a import statement
        if self.source_line.startswith("आयात ") :
            temp_list = self.source_line.split(" ")
            print(temp_list)
            import_name = temp_list[1]
            self.source_line = "import " + import_name
        return import_name

    # this will find all the string thing
    def find_string(self):

        # array for storing position of double quote (\" not included)
        double_quote_pos = []
        # array for storing position of single quotes (\' not included) 
        single_quote_pos = []

        # to find double and single quotes
        for i in range(0, len(self.source_line)):

            if self.source_line[i] == '"':
                
                # when first double quote if found or a double quote without preceding \
                if len(double_quote_pos) == 0 or self.source_line[i-1] != "\\":
                    double_quote_pos.append(i)

            if self.source_line[i] == "'":

                # when first single quote is found or a single wuote without preceding \
                if len(single_quote_pos) == 0 or self.source_line[i-1] != "\\":
                    single_quote_pos.append(i)
        
        # when number of double quotes are odd i.e. string syntax is wrong
        if len(double_quote_pos) % 2 != 0:
            raise SyntaxError("String Error : odd double quotes : <" + self.source_line + ">")
            quit()

        # when number of single quotes are odd i.e. string syntax error
        if len(single_quote_pos) % 2 != 0:
            raise SyntaxError("String Error : odd single quotes : <" + self.source_line + ">")
            quit()


        # this will hold all the position where ever their is charater which is part of string
        self.string_ch_pos = []
        i = 0
        while i < len(double_quote_pos):
            self.string_ch_pos.extend(list(range(double_quote_pos[i], double_quote_pos[i+1]+1)))
            i += 2
        
        i = 0
        while i < len(single_quote_pos):
            self.string_ch_pos.extend(list(range(single_quote_pos[i], single_quote_pos[i+1]+1)))
            i += 2
    

    # this will find all comments
    def find_comments(self):
        self.comment_pos = -1
        for i in range(0, len(self.source_line)):
            if self.source_line[i] == '#':
                self.comment_pos = i
                break

    # this will replace all hi word with english word (actually not all, only those which are needed)
    def replace(self, hi_word, en_word):

        
        
        # position at which word found
        pos = self.find_to_replace(hi_word) 
        
        # loop till end on the scanned source_line if hindi word found
        while pos != -1:
            if self.comment_pos >= 0 and self.comment_pos >= pos:
                break
            
            
            # if word not inside inside string
            if pos not in self.string_ch_pos:
                # left part alredy replaced, now only replace on right part
                str_before = self.source_line
                left = self.source_line[:pos]
                right = self.source_line[pos:]
                self.source_line = left + right.replace(hi_word, en_word, 1)
                
                # increment all positoin of string as replaced word can varry in length
                for i in range(pos, len(self.string_ch_pos)):
                    self.string_ch_pos[i] += len(en_word)-len(hi_word)
                
                # if str_before == self.source_line : pos = -1 
            
            pos = self.find_to_replace(hi_word)

    def find_to_replace(self,hi_word) :        
        # if hi_word doesn't even exit then return -1, this is just to make things faster
        # and not search the whole line bekar me
        if self.source_line_number == 31:
            # print("IAM38")
            pass
        if self.source_line.find(hi_word) == -1:
            return -1

        pos = -1

        starts =    [' ',':','(',',','.','[','{','+','-','*','/','%']
        ends =      [' ',':',')',',','.',']','}','+','-','*','/','%']
        if hi_word.endswith('('): 
            ends.append('')
        else :
            ends.append('(')

        if self.source_line.startswith(hi_word) :
            for e in ends:
                pos = self.source_line.find(hi_word+e)
                if pos > -1 : return pos
        
        for s in starts:
            for e in ends:
                pos = self.source_line.find(s+hi_word+e)
                if pos > -1 : return pos + 1 # return pos + 1 as actual word start after s (starts list)
        
        if self.source_line.rstrip().endswith(hi_word) :
            for s in starts:
                pos = self.source_line.find(s+hi_word)
                if pos > -1 : return pos + 1 # return pos + 1 as actual word start after s (starts list)
        
        return pos