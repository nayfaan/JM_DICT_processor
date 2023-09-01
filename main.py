import os
import xml.dom.minidom
from operator import itemgetter
import json

global OUTPUT_PATH
OUTPUT_PATH = "output/"

def rom2hir(r):
    r2h = {
        "a": "あ",
        "i": "い",
        "u": "う",
        "e": "え",
        "o": "お",
        "ka": "か",
        "ki": "き",
        "ku": "く",
        "ke": "け",
        "ko": "こ",
        "ga": "が",
        "gi": "ぎ",
        "gu": "ぐ",
        "ge": "げ",
        "go": "ご",
        "sa": "さ",
        "shi": "し",
        "si": "し",
        "su": "す",
        "se": "せ",
        "so": "そ",
        "za": "ざ",
        "ji": "じ",
        "zi": "じ",
        "zu": "ず",
        "ze": "ぜ",
        "zo": "ぞ",
        "ta": "た",
        "chi": "ち",
        "ti": "ち",
        "tsu": "つ",
        "tu": "つ",
        "te": "て",
        "to": "と",
        "da": "だ",
        "di": "ぢ",
        "du": "づ",
        "de": "で",
        "do": "ど",
        "na": "な",
        "ni": "に",
        "nu": "ぬ",
        "ne": "ね",
        "no": "の",
        "ha": "は",
        "hi": "ひ",
        "fu": "ふ",
        "hu": "ふ",
        "he": "へ",
        "ho": "ほ",
        "ba": "ば",
        "bi": "び",
        "bu": "ぶ",
        "be": "べ",
        "bo": "ぼ",
        "pa": "ぱ",
        "pi": "ぴ",
        "pu": "ぷ",
        "pe": "ぺ",
        "po": "ぽ",
        "ma": "ま",
        "mi": "み",
        "mu": "む",
        "me": "め",
        "mo": "も",
        "ya": "や",
        "yu": "ゆ",
        "yo": "よ",
        "ra": "ら",
        "ri": "り",
        "ru": "る",
        "re": "れ",
        "ro": "ろ",
        "wa": "わ",
        "wo": "を",
        "n": "ん"
        }
    
    try:
        r = r2h[r]
    except:
        pass
    
    return(r)

def write2File(t,p):
    output = open(OUTPUT_PATH+p, 'w')
    print(json.dumps(t), file = output)
    output.close()

def printJDict(jd):
    write2File(jd,"full_dict.txt")
    output_JDPlain = open(OUTPUT_PATH+"full_dict_plain.txt", 'w')
    for entry in jd:
        print(entry[0],"　",entry[1], file = output_JDPlain)
    output_JDPlain.close()

def run():
    st_name = "st.txt"
    if not os.path.exists(OUTPUT_PATH+st_name):
        JMD = xml.dom.minidom.parse("input/JMdict.xml");
        print(JMD.nodeName)
        print(JMD.firstChild.tagName)
        
        entrys = JMD.getElementsByTagName("entry")
        J_dict = list()
        for entry in entrys:
            keb = entry.getElementsByTagName("keb")
            ke=[]
            for k in keb:
                ke.append(k.childNodes[0].data)
            
            reb = entry.getElementsByTagName("reb")
            re=[]
            for r in reb:
                re.append(r.childNodes[0].data)
            
            for k in ke:
                for r in re:
                    J_dict.append([k,r])
                    if not r:
                        J_dict.append([k,""])
                if not k:
                    J_dict.append(["",r])
                    
        printJDict(J_dict)
        
        st = list()
        for entry in J_dict:
            r = entry[1]
            if r:
                if r[0] == r[-1]:
                    st.append(entry)
                    
        st = sorted(st, key=itemgetter(1))
        
        st_kana = dict()
        for entry in st:
            r = entry[1]
            
            if not r[0] in st_kana:
                st_kana[r[0]] = [entry]
            else:
                st_kana[r[0]].append(entry)
        
        write2File(st_kana,st_name)
    else:
        output = open(OUTPUT_PATH+st_name, 'r')
        st_kana = json.load(output)
        output.close()        
        
    i = -1
    
    while not i == "0":
        i = input("Starting kana: ")
        
        i = rom2hir(i)
        
        try:
            kr = st_kana[i]
            for entry in kr:
                print(entry[0],"　",entry[1])
        except:
            print("kana not found")
            
        print()
        
            
    
        
    
if __name__ == "__main__":
    run()
