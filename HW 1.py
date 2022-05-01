def get_nucleotide_frequencies(a):
    A =C =G =num1 = 0
    a =a.upper()
    empty = dict({})
    for i in a:
        if i == "A":
            A +=1
        elif i =="C":
            C+=1
        elif i == "G":
            G +=1
        else:
            for e in a:
                if e == i:
                    num1 += 1
                    del e
            empty[i] = num1
            num1 = 0


    print(" A:",A,"\n","C:", C,"\n","G:",G)
    print("junk:", end = "")
    return empty





frequencies = get_nucleotide_frequencies("ACTGTCACGRFRTNHYCTCGACCSGTGTCACGT")
print(frequencies)