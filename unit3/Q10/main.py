from temp import celsius_to_fahrenheit
from temp import fahrenheit_to_celsius
from temp import celsius_to_kelvin


def main():
    while True :
          print("/ntemp convert program")
          print("1,celsius_to_fahrenheit")
          print("fahrenheit_to_celsius")
          print("celsius_to_kelvi")
          print("4, Exit")

          try :
               choice = int(input("enter 1-4 choice"))
               
               if choice == 1 :
                    c = float(input("enter temperature in celsius"))
                    f = celsius_to_fahrenheit.convert(c)
                    print(f"{c} degree celsius is equal to {f} degree fahrenheit")

               elif choice == 2 :
                    f = float(input("enter temperature in fahrenheit"))
                    c = fahrenheit_to_celsius.convert(f)
                    print(f"{f} degree fahrenheit is equal to {c} degree celsius")

               elif choice == 3 :
                    c = float(input("enter temperature in celsius"))
                    k = celsius_to_kelvin.convert(c)
                    print(f"{c} degree celsius is equal to {k} degree kelvin")

               elif choice == 4 :

                        print("exiting the program")
                        break

                    

        
          except ValueError :
               print("invalid input, please enter a number between 1 and 4")

if __name__ == "__main__":
    main()  
