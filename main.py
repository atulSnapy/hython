import sys, subprocess
import source_code as sc
VERSION = "1.0.3"

def transpile(file_name):
    ids             = get_ids()
    source_file     = open(file_name, 'rb')
    transpiled_file = open(file_name.split('.')[0]+"_.py", 'wb')

    transpiled_file.write("try:\n".encode('utf-8'))

    line_number     = 0
    indent_for_trsanplied = "    "
    for line in source_file:
        line_number += 1
        line = line.decode('utf-8')
        # print(line)
        source_code = sc.Source_Code(line, line_number)
        source_code.find_string()
        source_code.find_comments()
        for en_word, hi_word in ids:
            source_code.replace(hi_word, en_word)
        transpiled_code = indent_for_trsanplied+source_code.source_line.rstrip()+"      # line-"+str(source_code.source_line_number)+"\n"
        transpiled_file.write(transpiled_code.encode('utf-8'))
    
    transpiled_file.write("\nexcept Exception as e:\n    print(e)".encode('utf-8'))
    transpiled_file.close()
    source_file.close()

def get_ids():
    id_string = """
        and	और
        as	जैसे
        assert	निश्चित
        break	अवरोध
        class	वर्ग
        continue    जारी
        def परि
        del	मिटाओ
        elif	या_अगर
        else	अन्यथा
        except	त्रुटि
        False	असत्य
        finally	अन्तिम
        for	क्रमशः
        global	सर्व
        if	अगर
        import	आयात
        in	में
        is	है
        lambda	मिराज
        None	शून्य
        nonlocal	बेस्थानीय
        not	नहीं
        or	या
        pass	छोडो
        raise	उठाओ
        return	वापस
        True	सत्य
        try	प्रयास
        while	जबतक
        with	लेकर
        yield	उपज
        abs(	समपूर्ण(
        all(	सब(
        any(	कोईभी(
        ascii(	आसकी(
        bin(	द्विग(
        bool(	द्वाफल(
        bytearray(	बाइट_व्यूह(
        bytes(	बाइटस(
        callable(	प्रतिदेय(
        chr(	अक्षर(
        classmethod(	वर्ग_क्रिया(
        compile(	संकलन(
        complex(	जटिल(
        delattr(	गुण_मिटाओ(
        dict(	कोश(
        dir(	संहिता(
        divmod(	भाग_शेष(
        enumerate(	क्रमागत(
        eval(	मुल्यांकन(
        exec(	प्रयोग(
        filter(	छानो(
        float(	चल(
        format(	रचना(
        frozenset(	अचल_सम्मुचय(
        getattr(	गुण_लो(
        globals(	सर्वकोश(
        hasattr(	गुण_है(
        hash(	हैश(
        help(	मदद(
        hex(	षष्ठ(
        id(	पहचान(
        input(	पूछो(
        int(	अंक(
        isinstance(	अवतार_है(
        issubclass(	उपवर्ग_है(
        iter(	पुनरावर्तक(
        len(	माप(
        list(	सुची(
        locals(	देशकोश(
        map(	नक्शा(
        max(	उच्च(
        memoryview(	स्मृति_दृश्य(
        min(	न्यून(
        next(	अगला(
        object(	वस्तु(
        oct(	अष्ट(
        open(	खोलो(
        ord(	यूनिकोड_अक्षर(
        pow(	घात(
        print(	लिखो(
        property(	गुण(
        range(	सीमा(
        repr(	पठनीय(
        reversed(	उलटा(
        round(	पूूणांकन(
        set(	समुच्चय(
        setattr(	गुण_(
        slice(	टुकडा(
        sorted(	क्रमम्(
        @staticmethod(	@अटल_क्रिया(
        str(	माला(
        sum(	योग(
        tuple(	टपल(
        type(	प्रकार(
        vars(	चर(
        zip(	संकु(
        capitalize(	प्रथम_ऊ(
        casefold(	प्रत्येक_नि(
        center(	मध्य(
        count(	गिनो(
        encode(	कुटलेख(
        endswith(	अंत_में(
        expandtabs(	रिक्त_(
        find(	खोजो(
        format(	रचना(
        format_map(	रचना_नक्शा(
        index(	सूचक(
        isalnum(	अक्षर_अंक_है(
        isalpha(	अक्षर_है(
        isdecimal(	दशमलव_है(
        isdigit(	अंक_है(
        isidentifier(	_है(
        islower(	नीचला_है(
        isnumeric(	अंक_है(
        isprintable(	छाप_है(
        isspace(	खाली_है(
        istitle(	शीर्षक_है(
        isupper(	ऊपरी_है(
        join(	मेल(
        ljust(	बाया_ज(
        lower(	नीचला(
        lstrip(	बाया_छा(
        maketrans(	अनुवाद_तालिका(
        partition(	बांटे(
        replace(	बदलो(
        rfind(	उ_खोजौ(
        rindex(	उ_सूचक(
        rpartition(	उ_विभाजन(
        rsplit(	बाया_विभाजन(
        rstrip(	बाया_उघाडो(
        split(	उघाडो(
        splitlines(	पंक्ति_उघाडो(
        startswith(	शूरू_में(
        swapcase(	अक्षर_बदलो(
        title(	शीर्षक(
        translate(	अनुवाद(
        upper(	ऊपरी(
        zfill(	शू_भरो(
        append(	जोडो(
        clear(	साफ(
        copy(	नकल(
        extend(	बढाओ(
        insert(	डालो(
        pop(	निकालो(
        remove(	हटाओ(
        reverse(	उलटा(
        sort(	क्रम(
        fromkeys(	चाबी_से(
        get(	लो(
        items(	वस्तूए(
        keys(	पूंजी(
        popitem(	वस्तू_निकालो(
        setdefault(	शेष_रखो(
        update(	नया_जोडो(
        values(	मान(
        add(	जमा(
        difference(	अंतर(
        difference_update(	अंतर_निकालो(
        discard(	रद्द(
        intersection(	सर्वनिष्ठ(
        intersection_update(	सर्वनिष्ठ_निकालो(
        isdisjoint(	भिन्न_है(
        issubset(	उपसमुच्चय_है(
        issuperset(	उच्चसमुच्चय_है(
        symmetric_difference(	सममित_अंतर(
        symmetric_difference_update(	सममित_अंतर_जोडो(
        union(	सम्मिलन(
        update(	सम्मिलन_जोडो(
        == =
        = <-"""
    id_pair_arr = id_string.strip().split('\n')
    ids = []
    
    for id_pair in id_pair_arr:
        ids.append(tuple(id_pair.split()))

    # this will sort in asending order accoding to hindi words
    ids.sort(key = lambda x: len(x[1]), reverse = True)
    #this will make sure that "=" appers before "<-"
    ids[-1], ids[-2] = ids[-2], ids[-1]
    return ids


def main():
    if sys.argv[1] == "--version" or sys.argv[1] == "--help" or sys.argv[1] == "--संस्करण" or sys.argv[1] == "--सहायता"  or sys.argv[1] == "--मदद" :
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
        subprocess_argv = ["python3",file_name.split('.')[0]+"_.py"]
        subprocess_argv.extend(sys.argv[2:])

        transpile(file_name)
        subprocess.call(subprocess_argv)

main()