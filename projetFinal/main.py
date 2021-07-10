
import interface


def main():

    print("\n\n\t\tWELCOM sur La Gestion des pays de la CEDEAO")

    continuer = 1
    while continuer == 1:
        interface.menu()
        continuer = int(input("Voulez vous continuer? OUI= 1 et NON = 0\n"))


if __name__ == '__main__':
    main()
