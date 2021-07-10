"""
 Cette module est l'interface d'affichage
"""


#importation module choice
import choice

def display (country):
    """fonction qui permet d'afficher un pays"""
    nom = country['name']
    capital = country['capital']
    continent = country['location']
    independance = country['independance']
    president = country['president']
    langue = country['langue']
    superficie = country['superficie']
    haditant = country['population']
    pib = country['pib']

    print(f"Nom                  ==>  {nom}")
    print(f"Capital              ==>  {capital}")
    print(f"Continent            ==>  {continent}")
    print(f"Date Independance    ==>  {independance}")
    print(f"Nom President Actuel ==>  {president}")
    print(f"Langue Offielle      ==>  {langue}")
    print(f"Superficie           ==>{superficie}")
    print(f"Nombre d'habitants   ==> {haditant}")
    print(f"PIB                  ==> {pib}")


# to display the application's menu
def menu():
    """Cette partie affiche le meenu """
    
    while True:
        try:
            print("\n\t\tTAPPEZ : ")
            print("1.Pour afficher un pays membre")
            print("2.Pour ajouter un nouveau pays")
            print("3.Pour modifier un pays membre")
            print("4.Pour supprimer un pays membre")
            print("5.Pour afficher tous les page")
            uChoice = int(input("\n\t\tVotre choix ?\n"))
            if uChoice in range(1,6):
                choice.userChoice(uChoice)
                break
        except:
            print ('\nChoix indisponible !')


 
  
 
    