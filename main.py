import os
import xml.dom.minidom
from operator import itemgetter
import json

def run():
    output_path = "output/st.txt"
    if not os.path.exists(output_path):
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
        
        output = open(output_path, 'w')
        print(json.dumps(st_kana), file = output)
        output.close()
    else:
        output = open(output_path, 'r')
        st_kana = json.load(output)
        output.close()        
        
    i = -1
    while not i == "0":
        i = input("Starting kana: ")
        try:
            kr = st_kana[i]
            for entry in kr:
                print(entry[0],"　",entry[1])
        except:
            print("kana not found")
            
        print()
        
            
    
        
    
if __name__ == "__main__":
    run()
