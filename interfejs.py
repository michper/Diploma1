import test as test
import visualise as vis
import numpy as np

points = [(553, 82), (552, 116), (462, 116), (462, 238), (642, 239), (642, 117), (688, 114), (688, 211), (723, 213), (734, 202), (726, 134), (743, 117), (793, 118), (817, 193), (845, 109), (799, 285), (846, 184), (863, 252), (861, 282), (887, 291), (896, 158), (888, 139), (910, 98), (932, 84), (963, 84), (970, 58), (1023, 46), (1077, 70), (1069, 132), (1055, 211), (1030, 229), (1023, 265), (1021, 329), (1001, 347), (982, 326), (995, 302), (978, 268), (981, 242), (1004, 161), (962, 138), (942, 186), (919, 194), (925, 244), (921, 270), (942, 243), (887, 308), (908, 311), (920, 327), (918, 342), (906, 374), (859, 451), (885, 476), (901, 548), (923, 555), (938, 559), (953, 559), (954, 527), (970, 417), (988, 402), (1028, 431), (1030, 510), (1013, 562), (998, 562), (953, 586), (842, 627), (945, 598), (823, 597), (814, 535), (771, 538), (747, 520), (731, 533), (729, 479), (756, 459), (794, 430), (831, 439), (836, 489), (793, 411), (865, 326), (852, 305), (782, 323), (811, 388), (744, 384), (722, 378), (721, 413), (691, 450), (702, 431), (686, 415), (644, 423), (689, 551), (689, 580), (733, 577), (729, 549), (562, 438), (566, 478), (487, 447), (494, 508), (501, 420), (532, 428), (569, 422), (588, 404), (592, 383), (568, 359), (643, 352), (516, 356), (486, 375), (476, 397), (462, 357), (462, 409), (443, 447), (409, 458), (394, 486), (387, 528), (365, 551), (309, 581), (260, 534), (203, 533), (146, 637), (213, 636), (287, 616), (398, 240), (417, 365), (400, 312), (376, 117), (339, 119), (337, 160), (312, 120), (305, 140), (389, 190), (553, 82), (688, 240), (1002, 122), (462, 177), (552, 239), (552, 280), (602, 429), (174, 582), (644, 300), (730, 506), (690, 500)]

chosenList = []
# chosenList = [6,9,8,31]
# route = test.getRoute(chosenList)
# vis.plotTSP([route],points,1)



# chosenList=np.append(chosenList,x)


choice = None
while True:
    print("""
            0 - Zamknij
            1 - Zwierzęta do odwiedzenia
            2 - Generuj trase

            """)
    try:
        choice = int(input("""
        :"""))
        if choice == 0:
            print("""koniec""")
            break
        elif choice == 1:
            choice = None
            while True:
                print("""
                        0 - Wroc
                        1 - Dodaj punkt
                        2 - Usuń punkt
                        """)
                try:
                    choice = int(input("""
                    :"""))
                    if choice == 0:
                        print("""
                        powrot
                        """)
                        break
                    elif choice == 1:
                        print("""wybrane punkty:
                        """, chosenList)
                        a = int(input("""podaj nr zwierzęta/punktu:"""))
                        chosenList = np.append(chosenList, a)
                    elif choice == 2:
                        print("""wybrane punkty:"""
                              ,chosenList)
                        b = int(input("""podaj nr zwierzęta/punktu do Usunięcia:"""))
                        chosenList = chosenList.remove(b)
                        print(""""wybrane punkty""")
                except ValueError as e:
                    print("to moj blad", e)


        elif choice == 2:
            route = test.getRoute(chosenList)
            vis.plotTSP([route], points, 1)

    except ValueError as e:
        print("error", e)

print(G)
