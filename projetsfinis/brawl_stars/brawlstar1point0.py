import random

PV_colt = 30
ATK_colt = random.randint(10, 15)
PV_carl = 40
ATK_carl = random.randint(5, 10)
ch_capacité_carl = random.randint(1, 2)
PV_bartaba = 15
ATK_bartaba = random.randint(1, 5)
PV_bartaba_2 = 15
ATK_bartaba_2 = random.randint(1, 5)
esquive_ch = random.randint(1, 3)

print("\f1) Colt : il a 30PV et entre 10 et 15 d'ATK")
print("2) Carl : il a 40PV et entre 5 et 10 d'ATK + la capacité de pouvoir toucher 2 brawler en une attaque !")
perso = input("\fEntrez le numéro du perso que vous voulez avoir : ")
perso = int(perso)
if perso == 1:
    print("\fvous avez choisi Colt, bonne chance !")
    print("\fVous allez attaquer 2 bartaba ! Ils ont tout les deux 15PV et entre 0 et 5 d'ATK")
    print("\fLes bartabas s'approchent de vous et lancent une première attaque qu'ils ratent")

    attaque_1 = input(
        "Pour attaquer entrez 1 et si vous voulez fuire entrez un autre chiffre (un dé sera lancé et donnera un nombre \fqui correspondera aux nombres de dêgats que vous ferez) : ")
    attaque_1 = int(attaque_1)
    if attaque_1 == 1:
        PV_bartaba = PV_bartaba - ATK_colt
        phrase_1 = f"\fVous avez réussi à toucher le bartaba,\f il a perdu {ATK_colt} de pv il n'en n'a plus que {PV_bartaba} ! "
        phrase_2 = f"\fVous avez tuer le bartaba du 1er coup !!!"
        if PV_bartaba > 0:
            print(phrase_1)
            print(
                "\f le bartaba vous contre-attaque en lançant une bouteille empoisonnée")
        elif PV_bartaba == 0:
            print(phrase_2)
            print(
                "\f le deuxième bartaba vous attaque et lance une bouteille empoisonnée !")

        esquive = input(
            "vous pouvez essayer d'esquiver l'attaque en appuyant sur 2 ! Sinon appuyer sur un autre chiffre !\f (vous avez 1 chance sur 3 de l'esquiver ! ) : ")
        esquive = int(esquive)
        if esquive == 2 and esquive_ch == 3:
            print("\fvous avez réussi à l'esquiver !!! Vous ne prenez aucun dêgats ! ")
        elif esquive != 2 or esquive_ch != 3:
            print("\fVous êtes toucher par le bartaba !")
            PV_colt = PV_colt - ATK_bartaba
            phrase_3 = f"Le bartaba vous attaque de {ATK_bartaba} d'ATK , il ne vous reste plus que {PV_colt} PV !"
            print(phrase_3)

        attaque_2 = input(
            "\fA vous de contre-attaquer le bartaba en appuyant sur 1 ! \fEt si vous voulez fuire, appuyer sur un autre chiffre : ")
        attaque_2 = int(attaque_2)
        if attaque_2 == 1:
            ATK_colt = random.randint(10, 15)
            if PV_bartaba > 0:
                PV_bartaba = PV_bartaba - ATK_colt
                phrase_4 = f"\fVous avez fait {ATK_colt} d'ATK, le premier bartaba est mort !"
                print(phrase_4)
            elif PV_bartaba <= 0:
                PV_bartaba_2 = PV_bartaba_2 - ATK_colt
                phrase_5 = f"\fVous avez fait {ATK_colt} d'ATK sur le deuxième bartaba, il ne lui reste que {PV_bartaba_2} PV !"
                phrase_6 = f"\Vous avez fait {ATK_colt} d'ATK vous avez retuer le deuxième bartaba du premier coup, vous êtes vraiment trop fort !!!"
                if PV_bartaba_2 > 0:
                    print(phrase_5)
                elif PV_bartaba_2 == 0:
                    print(phrase_6)
                    print(
                        "Vous avez téminé la première manche le plus rapidement possible bravo !!!")

            if PV_bartaba_2 <= 0:
                print("")
            elif PV_bartaba_2 > 0:
                esquive_2 = input(
                    "\fLe deuxième bartaba riposte, pour essayer d'esquiver l'attaque du deuxième bartaba entrez 2 : ")
                esquive_2 = int(esquive_2)
                esquive_ch = random.randint(1, 3)
                if esquive_2 == 2 and esquive_ch == 3:
                    print(
                        "Vous arriver à esquiver l'attaque et vous vous en sorter indemne !")
                elif esquive_2 != 2 or esquive_ch != 3:
                    PV_colt = PV_colt - ATK_bartaba_2
                    phrase_7 = f"\fLe deuxième Bartaba réussi à vous attaquer et ils vous fait {ATK_bartaba_2} d'ATK, il vous reste {PV_colt} de PV "
                    print(phrase_7)

            if PV_bartaba_2 <= 0:
                print("")
            elif PV_bartaba_2 > 0:
                attaque_3 = input(
                    "Pour riposter entrez 1. Sinon si vous voulez fuire appuyez sur un autre chiffre : ")
                attaque_3 = int(attaque_3)
                if attaque_3 == 1:
                    ATK_colt = random.randint(10, 15)
                    PV_bartaba_2 = PV_bartaba_2 - ATK_colt
                    if PV_bartaba_2 <= 0:
                        phrase_8 = f"\fVous avez fait {ATK_colt} de dêgats ! Le deuxième bartaba et mort, vous avez fini la première manche !"
                        print(phrase_8)
                    elif PV_bartaba_2 > 0:
                        phrase_9 = f"\fVous avez fait {ATK_colt} de dêgats ! Il ne reste plus que {PV_bartaba_2} pv au deuxième bartaba !"
                        print(phrase_9)

                        esquive_3 = input(
                            "\fLe deuxième bartaba va sûrement lancer sa dernière attaque,\f si vous voulez essayer de l'esquiver entrer 2, sinon entrez un autre nombre.(Il y a toujours 1 chance sur 3 de réussir à l'esquiver) :")
                        esquive_3 = int(esquive_3)
                        esquive_ch = random.randint(0, 3)
                        if esquive_3 == 2 and esquive_ch == 3:
                            print("\fVous réussissez à l'esquiver ! ")
                        elif esquive_3 != 2 or esquive_ch != 3:
                            ATK_bartaba_2 = random.randint(1, 5)
                            PV_colt = PV_colt - ATK_bartaba_2
                            phrase_10 = f"\fVous êtes toucher ! Le deuxième bartaba vous inflige {ATK_bartaba_2} d'ATK, il vous reste {PV_colt} PV !"
                            print(phrase_10)

                        attaque_4 = input(
                            "\fC'est sûrement la dernière attaque, pour riposter entrez 1 ! Si vous voulez fuir entrez un autre chiffre : ")
                        attaque_4 = int(attaque_4)
                        if attaque_4 == 1:
                            ATK_colt = random.randint(10, 15)
                            PV_bartaba_2 = PV_bartaba_2 - ATK_colt
                            phrase_11 = f"Vous avez fait {ATK_colt} d'ATK, le deuxième bartaba est mort vous finnissez la première manche !"
                            print(phrase_11)
                        else:
                            print("\f\fVous fuyez et abandonnez la partie...")

                else:
                    print("\f\fVous fuyez et abandonnez la partie...")

        else:
            print("\f\fVous fuyez et abandonnez la partie...")

    else:
        print("\f\fVous fuyez et abandonnez la partie...")


elif perso == 2:
    print("\fVous avez choisi Carl, bonne chance !")
    print("\fVous allez attaquer 2 bartaba ! Ils ont tout les deux 15PV et entre 0 et 5 d'ATK")
    print("\fLes bartabas s'approchent de vous et lancent une première attaque qu'ils ratent")

    atq_1 = input("Pour attaquer entrez 1, et pour fuire entrez un autre chiffre. \f(Si vous attaquez un dé sera lancé et donnera un nombre qui correspondera à votre attaque) : ")
    atq_1 = int(atq_1)
    if atq_1 == 1:
        PV_bartaba = PV_bartaba - ATK_carl
        phrase_12 = f"\fVous avez fait {ATK_carl} d'ATK, il reste {PV_bartaba} PV au bartaba !"
        print(phrase_12)

        défense_1 = input(
            "\fLe bartaba riposte ! Pour essayer d'esquiver entrez 2 (Vous avez 1 chance sur 3 de l'esquiver)\f Sinon appuyer sur un autre chiffre : ")
        défense_1 = int(défense_1)
        if défense_1 == 2 and esquive_ch == 3:
            print("\fVous avez réussi à esquiver l'attaque du bartaba !")
        elif défense_1 != 2 or esquive_ch != 3:
            PV_carl = PV_carl - ATK_bartaba
            phrase_13 = f"\fVous êtes touché par le bartaba, il vous a fait {ATK_bartaba} points de dêgats, il vous reste {PV_carl} PV"
            print(phrase_13)

        atq_2 = input("\fMaintenant vous allez essayer d'utiliser votre capacité ! \f(elle consiste a toucher 2 brawler en même temps, avec une chance de réussite de 1 chance sur 2 !). \fSi vous voulez simplement attaquer entrez 1 et si vous voulez utiliser votre capacité entrez 2. Pour fuire appuyer sur un autre chiffre : ")
        atq_2 = int(atq_2)
        ATK_carl = random.randint(5, 10)
        if atq_2 == 1 or atq_2 == 2:
            if atq_2 == 1:
                PV_bartaba = PV_bartaba - ATK_carl
                if PV_bartaba > 0:
                    phrase_14 = f"\fVous infligez {ATK_carl} d'ATK au premier bartaba, il lui reste {PV_bartaba} PV"
                    print(phrase_14)
                elif PV_bartaba <= 0:
                    phrase_15 = f"\fVous réussissez à tuer le premier bartaba en lui infligeant {ATK_carl} d'ATK !"
            elif atq_2 == 2 and ch_capacité_carl == 2:
                PV_bartaba = PV_bartaba - ATK_carl
                PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                if PV_bartaba > 0:
                    phrase_16 = f"\fVous réussissez à toucher les 2 bartabas en leur infligeant {ATK_carl} d'ATK chacun ! \fIl reste {PV_bartaba} PV au premier bartaba et {PV_bartaba_2} PV au deuxième bartaba"
                    print(phrase_16)
                elif PV_bartaba <= 0:
                    phrase_17 = f"\fVous réussissez à tuer le premier bartaba et à toucher le deuxième bartaba en leur infligeant {ATK_carl} d'ATK chacun ! \fIl reste {PV_bartaba_2} PV au deuxième bartaba "
                    print(phrase_17)
            elif atq_2 == 2 and ch_capacité_carl != 2:
                PV_bartaba = PV_bartaba - ATK_carl
                if PV_bartaba > 0:
                    phrase_18 = f"\fVous ratez votre capacité mais vous réussissez à infliger {ATK_carl} d'ATK au premier bartaba, il lui reste {PV_bartaba} PV"
                    print(phrase_18)
                elif PV_bartaba <= 0:
                    phrase_19 = f"\fVous ratez votre capacité mais vous réussissez à tuer le premier bartaba en lui infligeant {ATK_carl} d'ATK !"
                    print(phrase_19)

            défense_2 = input(
                "\fLe bartaba vous contre-attaque, pour essayer d'esquiver son attaque entrez 2 (c'est toujours 1 chance sur 3 d'y arriver)\fSinon entrez un autre chiffre : ")
            défense_2 = int(défense_2)
            esquive_ch = random.randint(1, 3)
            ATK_bartaba = random.randint(1, 5)
            if défense_2 == 2 and esquive_ch == 3:
                print(
                    "\fVous avez réussi à esquiver l'attaque ! Vous ne prenez aucun dêgats !")
            elif défense_2 != 2 or esquive_ch != 3:
                PV_carl = PV_carl - ATK_bartaba
                phrase_20 = f"\fLe bartaba réussi à vous toucher, il vous inflige {ATK_bartaba} d'ATK, il vous reste {PV_carl} PV"
                print(phrase_20)

            atq_3 = input("\fC'est à votre tour si vous voulez attaquer entrez 1 \fet si vous voulez essayer d'attaquer avec votre capacité entrez 2 !(Vous avez toujours 1 chance sur 2 de réussir votre capacité)\fPour fuir appuyez sur un autre chiffre : ")
            atq_3 = int(atq_3)
            ATK_carl = random.randint(5, 10)
            ch_capacité_carl = random.randint(1, 2)
            if atq_3 == 1 or atq_3 == 2:
                if atq_3 == 1:
                    if PV_bartaba > 0:
                        PV_bartaba = PV_bartaba - ATK_carl
                        phrase_21 = f"\fVous avez infligé {ATK_carl} d'ATK, le premier bartaba est mort !"
                        print(phrase_21)
                    elif PV_bartaba <= 0:
                        PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                        phrase_22 = f"\fVous avez infligé {ATK_bartaba_2} d'ATK au deuxième bartaba, il lui reste {PV_bartaba_2} PV"
                        phrase_23 = f"\fVous avez tué le deuxième bartaba en lui infligeant {ATK_carl} d'ATK ! \fVous avez fini la première manche le plus rapidement possible, bien joué vous êtes trop fort !!!"
                        if PV_bartaba_2 > 0:
                            print(phrase_22)
                        elif PV_bartaba_2 <= 0:
                            print(phrase_23)
                elif atq_3 == 2 and ch_capacité_carl == 2:
                    if PV_bartaba > 0:
                        PV_bartaba = PV_bartaba - ATK_carl
                        PV_bartaba_2 = PV_carl - ATK_carl
                        phrase_24 = f"\fVous avez réussi votre capacité et vous avez tué le premier bartaba en lui infligeant {ATK_carl} d'ATK ! \fEt vous avez infligé {ATK_carl} d'ATK au deuxième bartaba, il ne lui reste que {PV_bartaba_2} PV"
                        phrase_25 = f"\fVous avez réussi votre capacité et vous avez tué les deux bartabas d'un coup en leur infligeant {ATK_carl} d'ATK !\f\fVous avez fini la première manche le plus rapidement possible, bravo vous êtes trop fort !"
                        if PV_bartaba_2 > 0:
                            print(phrase_24)
                        elif PV_bartaba_2 <= 0:
                            print(phrase_25)
                    elif PV_bartaba <= 0:
                        PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                        phrase_26 = f"\fVous réussissez votre capacité en infligeant {ATK_carl} d'ATK mais vous ne toucher que le deuxième bartaba vu que le premier est mort !\fIl reste {PV_bartaba_2} PV au deuxième bartaba !"
                        phrase_27 = f"\fVous réussissez votre capacité et vous tuez le bartaba restant en lui infligeant {ATK_carl} d'ATK !\f\fVous avez fini la première manche le plus rapidement possible, bravo vous êtes trop fort !"
                        if PV_bartaba_2 > 0:
                            print(phrase_26)
                        elif PV_bartaba_2 <= 0:
                            print(phrase_27)
                elif atq_3 == 2 and ch_capacité_carl != 2:
                    if PV_bartaba > 0:
                        PV_bartaba = PV_bartaba - ATK_carl
                        phrase_28 = f"\fVous ratez votre capacité mais vous réussissez à tuer le premier bartaba en lui infligeant {ATK_carl} d'ATK"
                        print(phrase_28)
                    elif PV_bartaba <= 0:
                        PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                        phrase_29 = f"\fVous ratez votre capacité mais ce n'est pas grave vu qu'il reste un seul bartaba !\fVous réussissez tout de même à infliger {ATK_carl} d'ATK au deuxième bartaba, il ne lui reste que {PV_bartaba_2} PV !"
                        phrase_30 = f"\fVous ratez votre capacité mais ce n'est pas grave vu qu'il reste un seul bartaba que vous réussissez à tuer en lui infligeant {ATK_carl} d'ATK !\f\fBien joué vous avez fini la première manche le plus rapidement possible, bravo vous êtes trop fort !"
                        if PV_bartaba_2 > 0:
                            print(phrase_29)
                        elif PV_bartaba_2 <= 0:
                            print(phrase_30)

                if PV_bartaba_2 > 0:
                    défense_3 = input(
                        "\fLe deuxième bartaba veut se venger de l'élimination de son camarade en lançant une bouteille empoisonnée !\f Si vous voulez essayer de l'esquiver entrez 2 sinon entrez un autre chiffre : ")
                    défense_3 = int(défense_3)
                    esquive_ch = random.randint(1, 3)
                    ATK_bartaba_2 = random.randint(1, 5)
                    if défense_3 == 2 and esquive_ch == 3:
                        print("\fVous réussissez à esquiver l'attaque !")
                    else:
                        PV_carl = PV_carl - ATK_bartaba_2
                        phrase_31 = f"\fVous êtes touchés par l'attaque ! Le deuxième bartaba vous inflige {ATK_bartaba_2} d'ATK, il vous reste {PV_carl} PV"
                        print(phrase_31)

                    atq_4 = input(
                        "\fPour attaquer le deuxième bartaba entrez 1 et pour lui montrer de quel bois vous vous chauffez et l'attaquer avec votre capacité entrez 2 ! \fSinon, si vous voulez fuir entrez un autre chiffre : ")
                    atq_4 = int(atq_4)
                    ATK_carl = random.randint(5, 10)
                    ch_capacité_carl = random.randint(1, 2)
                    if atq_4 == 1 or atq_4 == 2:
                        if atq_4 == 1:
                            PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                            if PV_bartaba_2 > 0:
                                phrase_32 = f"\fVous attaquez le bartaba et vous lui infligez {ATK_carl} d'ATK, il lui reste {PV_bartaba_2} PV !"
                                print(phrase_32)
                            elif PV_bartaba_2 <= 0:
                                phrase_33 = f"\fVous réussissez à tuer le deuxième bartaba en lui infligeant {ATK_carl} d'ATK ! \f\fVous avez fini la première manche !"
                                print(phrase_33)
                        elif atq_4 == 2 and ch_capacité_carl == 2:
                            PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                            if PV_bartaba_2 > 0:
                                phrase_34 = f"\fVous réussissez votre capacité mais cela n'a pas servi à grand chose vu qu'il ne reste qu'un bartaba ! \fVous réussissez quand même à faire {ATK_carl} d'ATK sur le deuxième bartaba, il lui reste {PV_bartaba_2} PV !"
                                print(phrase_34)
                            elif PV_bartaba_2 <= 0:
                                phrase_35 = f"\fVous avez réussi votre capacité et vous réussissez à tuer le deuxième bartaba en lui infligeant {ATK_carl} d'ATK ! \f\fVous avez fini la première manche !"
                                print(phrase_35)
                        elif atq_4 == 2 and ch_capacité_carl != 2:
                            PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                            if PV_bartaba_2 > 0:
                                phrase_36 = f"\fVous ratez votre capacité mais ce n'est pas grave vu qu'il ne reste qu'un seul bartaba, \fet que vous réussissez à lui infliger {ATK_carl} d'ATK, il lui reste {PV_bartaba_2} PV ! "
                                print(phrase_36)
                            elif PV_bartaba_2 <= 0:
                                phrase_37 = f"\fVous ratez votre capacité mais ce n'est pas grave vu qu'il ne reste qu'un seul bartaba et que vous réussissez à le tuer en lui infligeant {ATK_carl} d'ATK ! \f\fVous terminez la première manche !"
                                print(phrase_37)

                        if PV_bartaba_2 > 0:
                            défense_4 = input(
                                "\fLe deuxième bartaba malgrè sa faible énérgie, lance sa bouteille empoisonnée\fPour essayer de l'esquiver entrez 2, sinon entrez un autre chiffre :  ")
                            défense_4 = int(défense_4)
                            esquive_ch = random.randint(1, 3)
                            ATK_bartaba_2 = random.randint(1, 5)
                            if défense_4 == 2 and esquive_ch == 3:
                                print(
                                    "\fVous réussissez à esquiver l'attaque !")
                            else:
                                PV_carl = PV_carl - ATK_bartaba_2
                                phrase_38 = f"\fLe deuxième bartaba réussi à vous toucher, il vous inflige {ATK_bartaba_2} d'ATK, il vous reste {PV_carl} PV ! "
                                print(phrase_38)

                            atq_5 = input(
                                "\fPour attaquer et se venger du bartaba entrez 1, votre capacité ne vous servira pas car il reste un seul bartaba et que cela reviendra au même\fSinon si vous voulez fuir entrez un autre chiffre :  ")
                            atq_5 = int(atq_5)
                            ATK_carl = random.randint(5, 10)
                            if atq_5 == 1:
                                PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                                if PV_bartaba_2 > 0:
                                    phrase_39 = f"\fLe deuxième bartaba est encore vivant mais vous lui avez infligé {ATK_carl} d'ATK, il lui reste {PV_bartaba_2} PV "
                                    print(phrase_39)
                                elif PV_bartaba_2 <= 0:
                                    phrase_40 = f"\fVous réussissez à tuer le deuxième bartaba en lui infligeant {ATK_carl} d'ATK ! \f\fVous avez terminé la première manche !"
                                    print(phrase_40)

                                if PV_bartaba_2 > 0:
                                    défense_5 = input(
                                        "\fLe deuxième bartaba qui réussit encore à s'en sortir vous contre-attaque en relançant une bouteille empoisonnée \fpour essayer de l'esquiver entrez 2 sinon entrez un autre chiffre : ")
                                    défense_5 = int(défense_5)
                                    esquive_ch = random.randint(1, 3)
                                    ATK_bartaba_2 = random.randint(1, 5)
                                    if défense_5 == 2 and esquive_ch == 3:
                                        print(
                                            "\fVous réussissez à esquiver l'attaque !")
                                    else:
                                        PV_carl = PV_carl - ATK_bartaba_2
                                        phrase_41 = f"\fLe bartaba réussi à vous toucher et vous inflige {ATK_bartaba_2} d'ATK, il vous reste {PV_carl} PV"
                                        print(phrase_41)

                                    atq_6 = input(
                                        "\fPour achever le deuxième bartaba en l'attaquant entrez 1, sinon pour fuir entrez un autre chiffre : ")
                                    atq_6 = int(atq_6)
                                    ATK_carl = random.randint(5, 10)
                                    if atq_6 == 1:
                                        PV_bartaba_2 = PV_bartaba_2 - ATK_carl
                                        phrase_42 = f"\fVous réussissez enfin à tuer le deuxième bartaba en lui infligeant {ATK_carl} d'ATK !\f\fVous terminez enfin la manche 1 !"
                                        print(phrase_42)

                                    else:
                                        print(
                                            "\f\fVous fuyez et abandonnez la partie...")

                            else:
                                print(
                                    "\f\fVous fuyez et abandonnez la partie...")

                    else:
                        print("\f\fVous fuyez et abandonnez la partie...")

            else:
                print("\f\fVous fuyez et abandonnez la partie...")

        else:
            print("\f\fVous fuyez et abandonnez la partie...")

    else:
        print("\f\fVous fuyez et abandonnez la partie...")


else:
    print("Vous avez du vous tromper quand vous avez entrer le nombre")
