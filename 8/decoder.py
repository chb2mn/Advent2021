from pprint import pprint
from copy import deepcopy

data = []
unique_num = 0

total = 0

with open('input.txt', 'r') as fin:
    #fin = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    #fin = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    #    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    #    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    #    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    #    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    #    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    #    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    #    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    #    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    #    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
    #]
    for line in fin:
        top     ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        bot     ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        topr    ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        topl    ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        botr    ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        botl    ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        mid     ={'a', 'b', 'c', 'd', 'e', 'f', 'g'} 
        parts = line.split('|')
        conns = parts[0].split()
        conns_by_len = {}
        for conn in conns:
            try:
                conns_by_len[len(conn)].append(set(conn))
            except KeyError:
                conns_by_len[len(conn)] = [set(conn)]
        pprint(conns_by_len)        
        top  = conns_by_len[3][0]-conns_by_len[2][0] #The top of the 7
        topr = deepcopy(conns_by_len[2][0])
        botr = deepcopy(conns_by_len[2][0])
        topl = conns_by_len[4][0]-conns_by_len[2][0] #"4"-"1"
        mid  = conns_by_len[4][0]-conns_by_len[2][0] #"4"-"1"
        
        topl -= bot.intersection(*conns_by_len[5]) #using bot here because it's a full set
        mid -= topl

        botr -= bot.intersection(*conns_by_len[6])
        topr -= botr

        bot = bot.intersection(*conns_by_len[6]) - top - topr - botr - topl - mid
        botl = botl - bot  - top - topr - botr - topl - mid
        
        top  = next(iter(top))
        bot  = next(iter(bot))
        topr = next(iter(topr))
        topl = next(iter(topl))
        botr = next(iter(botr))
        botl = next(iter(botl))
        mid  = next(iter(mid))
        '''
        print("top:", top)
        print("bot:", bot)
        print("topr:", topr)
        print("topl:", topl)
        print("botr:", botr)
        print("botl:", botl)
        print("mid:", mid)

        break
        '''
        display = parts[1].split()
        decoded_num = ""
        for num in display:
            if len(num) == 2: #1
                decoded_num += "1"
            elif len(num) == 4: #4
                decoded_num += "4"
            elif len(num) == 7: #8
                decoded_num+="8"
            elif len(num) == 3: #7
                decoded_num+="7"
            elif len(num) == 5: #532
                if topl in num:
                    decoded_num+='5'
                elif botl in num:
                    decoded_num +='2'
                else:
                    decoded_num +='3'
            elif len(num) == 6: #096
                if mid not in num:
                    decoded_num+='0'
                elif botl not in num:
                    decoded_num += '9'
                else:
                    decoded_num+='6'
        print(int(decoded_num))
        total += int(decoded_num)
print(total)
