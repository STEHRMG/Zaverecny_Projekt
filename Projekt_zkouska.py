import os

#import funkce 'cls' pro zpříjemnění uživatelského prostředí během běhu

class Pojistenec:

    """
    Třída reprezentujicí jednotlivé pojištěnné osoby
    """

    def __init__(self, krestni, prijmeni, telefon, vek):
        
        """
        Jednotlivé informace pojištěnných osob 
        """
        
        self._krestni = krestni
        self._prijmeni = prijmeni
        self._telefon = telefon
        self._vek = vek

    def __str__(self):

        """
        Textová reprezentace informací pojištěnných osob
        """

        return f"Křestní jméno: {self._krestni}, Příjmení: {self._prijmeni}, Telefonní číslo: {self._telefon}, Věk: {self._vek}" 

class SpravaPojistencu:
    
    """
    Třída reprezentující správu pojištěnných osob
    """

    def __init__(self):
        
        """
        Seznam pro správu pojištěnných osob
        """

        self.pojistenci = []

    def pridej_pojistence(self):

        """
        Metoda umožňující uživateli přidávat pojištěnné osoby a jejich informace
        """

        while True:
            krestni = input("Zadejte křestní jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            telefon = input("Zadejte telefonní číslo: ")
            vek = input("Zadejte věk: ")
            if krestni.isalpha() and krestni.istitle():
                break
            else:
                print("Křestní jméno musí být zadáno jako jedno slovo s počátečním velkým písmenem!")
        while True:
            if prijmeni.isalpha() and prijmeni.istitle():
                break
            else:
                print("Příjmení musí být zadáno jako jedno slovo s počátečním velkým písmenem!")
                prijmeni =  input("Zadejte příjmení: ")
        while True:    
            if len(telefon) == 9 and telefon.isnumeric():
                break
            else:
                print("Telefonní číslo má 9 čísel!")
                telefon = input("Zadejte telefonní číslo: ")
        while True:
            if vek.isnumeric():
                break
            else:
                print("Věk musí být zadán číselně!")
                vek =  input("Zadejte věk: ")
        telefon = "+420" + telefon
        novy_pojistenec = Pojistenec(krestni, prijmeni, telefon, vek)
        self.pojistenci.append(novy_pojistenec)
        print("Pojištěnec úspěšně přidán.")


    def najdi_pojistence(self):

        """
        Metoda umožňující uživateli vyhledat pojištěnnou osobu na základě jména, či příjmení
        """

        vyhledavany_vyraz = input("Zadej jméno, či příjmení pojištěnce, kterého si přeješ vyhledat: ")
        vysledek_vyhledavani = []
        for pojistenec in self.pojistenci:
            if vyhledavany_vyraz.lower() in pojistenec._krestni.lower() or vyhledavany_vyraz.lower() in pojistenec._prijmeni.lower():
                vysledek_vyhledavani.append(pojistenec)
        if vysledek_vyhledavani:
            print("Vyhledany pojištěnec: ")
            for pojistenec in vysledek_vyhledavani:
                print(pojistenec)
        else:
            print("Tento pojištěnec nebyl nalezen.")

    def vypis_vsech_pojistencu(self):

        """
        Metoda umožňující uživateli nechat vypsat všechny uložené pojištěnné osoby
        """

        for pojistenec in self.pojistenci:
            print(pojistenec)
          
    def beh(self):

        """
        Metoda umožňující programu fungovat - během ní si uživatel vybíra akci, kterou chce provést
        """

        while True:
            input("Pro pokračování stiskněte enter.")
            os.system("cls")
            print(40 * "_")
            print("Evidence pojištěných")
            print(40 * "_")
            print("\n")
            print("Vyberte si akci")
            print("1. Přidej pojištěného")
            print("2. Najdi pojištěného")
            print("3. Vypiš všechny uložené pojištěné")
            print("4. Konec")
            vyber = input("Napiš svůj výběr: ")
            if vyber == "1":
                self.pridej_pojistence()
            elif vyber == "2":
                self.najdi_pojistence()
            elif vyber == "3":
                self.vypis_vsech_pojistencu()
            elif vyber == "4":
                break
            else:
                print("Neplatná volba. Zkuse to znovu.")

#vytvoření objektů
spravapojistencu = SpravaPojistencu()
spravapojistencu.beh()