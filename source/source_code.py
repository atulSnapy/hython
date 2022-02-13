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
            # # adding the new file name
            # temp_list[1] = temp_list[1].strip()+"_"
            # print(temp_list)
            # self.source_line = " ".join(temp_list) + "\n"
            # print(self.source_line)
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
            raise SyntaxError("String Error")
            quit()

        # when number of single quotes are odd i.e. string syntax error
        if len(single_quote_pos) % 2 != 0:
            raise SyntaxError("String Error")
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

        # this will hold till where we have searched/replaced
        word_replaced_index = 0
        # loop till end on the scanned source_line if hindi word found
        while self.source_line.find(hi_word, word_replaced_index) != -1:
            if self.comment_pos >= 0 and self.comment_pos <= word_replaced_index:
                break
            # position at which word found
            pos = self.source_line.find(hi_word, word_replaced_index)
            
            # if word not inside inside string
            if pos not in self.string_ch_pos:
                # left part alredy replaced, now only replace on right part
                left = self.source_line[:word_replaced_index]
                right = self.source_line[word_replaced_index:]
                self.source_line = left + right.replace(hi_word, en_word, 1)
                # increment all positoin of string as replaced word can varry in length
                for i in range(pos, len(self.string_ch_pos)):
                    self.string_ch_pos[i] += len(en_word)-len(hi_word)
            
            # increment the replaced word to effectively search and loop
            word_replaced_index = pos + len(en_word)