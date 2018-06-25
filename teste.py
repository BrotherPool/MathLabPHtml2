import sys

def main():
    inputado=''
    print("\nDigite 0 para sair: ")
    teste=input()
    if teste == '0':
        sys.exit(1)
    else:
        i=0
        final = ''
        final+="<p>"
        for x in teste:
            if x=='$':
                if i==0:
                    final+=chr(92)+'('
                    i=1
                elif i==1:
                    final+=chr(92)+')'
                    i=0
            else:
                final+=x
                    
        final+="</p>"
    print ("\n"+final)
    main()

##        text_file = open("Output.txt", "w")
##        text_file.write(final)
##        text_file.close()
      
        
    

if __name__ == "__main__":
    main()
