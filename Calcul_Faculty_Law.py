""" An application to calculate course grades, 
    semester GPA, and annual GPA for 
    the first year of law studies at the University of Constantine 1.
    by Student of Law Developer Sami Remili"""
import  sys
def main():
        print("# Welcome to faculty of law and political science #\n\n## Calculation App ##")
        opt = int(input("\n[1]-Unit rate calculation\n[2]-First semester calculation\n[3]-Second semester calculation\n[4]-Total \n[5]-About\n[6]-Exite\n[#]-Choose one: "))
        
        if opt == 5:
            print("Thank you for Use App")
            sys.exit()
     
        while True:     
            if opt == 1:
                Lect= input("Enter your module name: ").upper()
                qu= input("This module Have TD?: ").upper()

                if qu == "YES":
    
                    def Mod_Td():
                        lec= int(input("Enter your Module point: "))
                        Td = float(input("Enter your TD point: "))
                        lec_td = (lec + Td)/2
                        print(f"The Moeyn of your {Lect} is : {lec_td}")
                    Mod_Td()

                elif qu == "NO":
                    def Module():
                        td= float(input("Enter your Module point: "))
                        print(f"Your Moeyn of your {Lect} is : {td}")
                    Module()
                
                
            if opt == 2:
                    coef = 9
                    def  semester():
                        dos = float(input("Constitutional: "))
                        Td_do = float(input("Enter your TD Mark: "))
                        juri = float(input("Sciences juridiques: "))
                        Td_juri = float(input("Enter your TD Mark: "))
                        admi = float(input("Administratif: "))
                        Td_idae = float(input("Enter your TD Mark: "))
                        menh = float(input("Méthodologie: "))
                        tarikh = float(input("Histoire juridiques: "))
                        mojtame = float(input("Communauté inter: "))
                        term = float(input("Terminologie: "))
                
                        doss = (dos+Td_do)/2*2
                        jurii = (juri + Td_juri)/2*2
                        admii = (admi+Td_idae)/2*1
                
                        total =(doss + jurii+admii+ menh+ tarikh + mojtame + term) /coef
                        print("The average of 1 Semseter is"+"{:.2f}".format(total))
                        
                    semester()
                
            if opt == 3:
                    coef = 9
                    def  semester2():
                        dos = float(input("Constitutional: "))
                        Td_do = float(input("Enter your TD Mark: "))
                        juri = float(input("Sciences juridiques: "))
                        Td_juri = float(input("Enter your TD Mark: "))
                        admi = float(input("Administratif: "))
                        Td_idae = float(input("Enter your TD Mark: "))
                        menh = float(input("Méthodologie: "))
                        chari = float(input("Charia: "))
                        i9tisad = float(input("Political Economy: "))
                        term = float(input("Terminologie: "))
                
                        doss = (dos+Td_do)/2*2
                        jurii = (juri + Td_juri)/2*2
                        admii = (admi+Td_idae)/2*1
                
                        total =(doss + jurii+admii+ menh+
                        chari+ i9tisad + term) /coef
                
                        print("The average of 2 Semseter is"+"{:.2f}".format(total))
                    semester2()
                    
                        
            if opt ==4:
                st1 = float(input("1semester: "))
                st2 = float(input("2semester: "))
                result = (st1+st2)/2
                print("The année scolaire moyenne "+"{:.2f}".format(result))
                
            back = input("Back to Main Menu?: ").upper()
            if back == "YES":
                 return main()
                
main()

if  __name__== "__main__":
    main()
