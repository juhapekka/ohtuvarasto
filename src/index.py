from varasto import Varasto

def luo_varastot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def tulosta_varastojen_tilanne(otsikko, mehua, olutta):
    print(otsikko)
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def tulosta_olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def muokkaa_mehuvarastoa(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def tulosta_virhetilanteet():
    print("Virhetilanteita:")
    virhe = Varasto(-100.0)
    print("Varasto(-100.0);")
    print(virhe)
    virhe = Varasto(100.0, -50.7)
    print("Varasto(100.0, -50.7)")
    print(virhe)

def testaa_lisays_ja_otto(mehua, olutta):
    print(f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\n")

    print(f"Mehuvarasto: {mehua}\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\n")

    print(f"Olutvarasto: {olutta}\nolutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\nOlutvarasto: {olutta}\n")

    print(f"Mehuvarasto: {mehua}\nmehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\nMehuvarasto: {mehua}")

def main():
    mehua, olutta = luo_varastot()
    tulosta_varastojen_tilanne("Luonnin jälkeen:", mehua, olutta)
    tulosta_olut_getterit(olutta)
    muokkaa_mehuvarastoa(mehua)
    tulosta_virhetilanteet()
    testaa_lisays_ja_otto(mehua, olutta)



if __name__ == "__main__":
    main()
