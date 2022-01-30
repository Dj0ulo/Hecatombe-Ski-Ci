from time import sleep

def symptomatique():
    return True if input("Symptomatique: ") == "oui" else False
def totalement_vaccine():
    return True if input("Vacciné il y a moins de 5 mois mais plus de 2 semaines: ") == "oui" else False
def partiellement_vaccine():
    return True if input("Vacciné il y a plus de 5 mois: ") == "oui" else False
def test_antigene():
    return True if input("Antigène positif: ") == "oui" else False
def test_pcr():
    return True if input("PCR positif: ") == "oui" else False

UN_JOUR = 24*60*60

def quarantaine(jour):
    print("Jour %d : Quarantaine aujourd'hui" % (jour+1))
    sleep(UN_JOUR)
def prudence(jour):
    print("Jour %d : Prudence aujourd'hui" % (jour+1))
    sleep(UN_JOUR)

if __name__ == "__main__":
    if symptomatique():
        if test_pcr():
            for jour in range(7):
                quarantaine(jour)
    else:
        totalement = totalement_vaccine()
        if totalement:
            for jour in range(10):
                prudence(jour)
        else:
            partiellement = partiellement_vaccine()
            if partiellement:
                for jour in range(7):
                    quarantaine(jour)
                    if jour == 3 and not test_antigene():
                        break
            else:
                for jour in range(10):
                    quarantaine(jour)
                    if jour == 6 and not test_antigene():
                        break
            print("Poursuivre autotest au jour 8, 9 et 10")
    print("Prenez soin de vous et de vos proches, soyez responsables !")
