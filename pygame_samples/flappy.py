import pygame, random, math

BELA = (255, 255, 255)
PLAVA = (0, 0, 255)
ZELENA = (0, 255, 0)

pygame.init()

# Podrazumevano, kada se pritisne taster tastature, generise se samo jedan dogadjaj KEY_DOWN, a dogadjaj
# KEY_UP se generise nakon otpustanja tastera. Narednim pozivom menjamo to podrazumevano ponasanje.
# Prilikom duzeg drzanja tastera generisace se vise dogadjaja KEY_DOWN, a nakon otpustanja tastera generisace
# se dogadjaj KEY_UP. Prvi dogadjaj KEY_DOWN se generise cim je pritisnut taster. Nakon toga se ceka broj
# milisekundi zadat prvim parametrom funckije set_repeat (ovom slucaju 10), a zatim se naredni dogadjaji
# KEY_DOWN generisnu u pravilnim vremenskim intervalima odredjenim drugim parametrom funckije key_repeat
# (u ovom slucaju ce se dogadjaji KEY_DOWN generisati na svakih 10 milisekundi, sve dok je taster pritisnut).
pygame.key.set_repeat(10, 10)

# sat koji odredjuje ucestalost iscrtavanja (i time i brzinu kretanja prepreka)
sat = pygame.time.Clock()

# dimenzija ekrana
dim = (sirina, visina) = (800, 400)
ekran = pygame.display.set_mode(dim)

# parametri ptice koja prolazi kroz prepreke - ona je kruznog oblika
ptica_x = sirina // 2
ptica_y = visina // 2
ptica_r = 30

# parametri prepreka koje se pojavljuju
sirina_prepreke = 60
visina_otvora = 130

# funkcija generise dva pravougaonika koji zajedno predstavljaju prepreku kroz koju ptica prolazi
# pravougaonici su odredjeni koordinatama gornjeg levog temena, sirinom i visinom 
def napravi_prepreku():
    vrh_otvora = random.randint(0, visina - visina_otvora)
    return [[sirina, 0, sirina_prepreke, vrh_otvora],
                 [sirina, vrh_otvora + visina_otvora, sirina_prepreke, visina - vrh_otvora - visina_otvora]]

# funkcija kojom se odredjuje predjeni put tekuce prepreke nakon kojeg se pojavljuje nova prepreka
def odredi_rastojanje_nove_prepreke():
    # najbrze sto moze, nova prepreka se pojavljuje nakon sto je tekuca presla trecinu sirine ekrana
    # a najredje sto moze, nova prepreka se pojavljuje nakon sto je tekuca prepreka presla ceo ekran
    return random.randint(sirina // 3, sirina)

# provera da li krug sa datim centrom (cx, cy) i poluprecnikom r sece horizontalnu duz (x0, y) (x1, y)
def krug_sece_horizontalnu_duz(cx, cy, r, x0, x1, y):
    if cy - r <= y and y <= cy + r:
        d = math.sqrt(r**2 - (cy - y)**2)
        if x0 - d <= cx and cx <= x1 + d:
            return True

# provera da li krug sa datim centrom i poluprecnikom sece vertikalnu duz (x, y0) (x, y1)
def krug_sece_vertikalnu_duz(cx, cy, r, x, y0, y1):
    if cx - r <= x and x <= cx + r:
        d = math.sqrt(r**2 - (cx - x)**2)
        if y0 - d <= cy and cy <= y1 + d:
            return True

# provera da li krug sa datim centrom i poluprecnikom sece pravougaonik zadat koordinatama
# gornjeg levog temena, sirinom i visinom
def krug_sece_pravougaonik(krug, pravougaonik):
    (cx, cy, r) = krug
    (x0, y0, w, h) = pravougaonik

    # provera sudara sa prednjom ivicom
    if krug_sece_vertikalnu_duz(cx, cy, r, x0, y0, y0 + h):
        return True

    # provera sudara sa donjom ivicom
    if krug_sece_horizontalnu_duz(cx, cy, r, x0, x0 + w, y0 + h):
        return True

    # provera sudara sa gornjom ivicom
    if krug_sece_horizontalnu_duz(cx, cy, r, x0, x0 + w, y0):
        return True

    # proveru preseka sa desnom ivicom preskacemo, jer u igri to nije moguce
    return False

# krecemo sa jednom pocetnom preprekom
prepreke = napravi_prepreku()
# odredjujemo kada treba da se pojavi naredna prepreka
rastojanje_nove_prepreke = odredi_rastojanje_nove_prepreke()

# glavna petlja
kraj = False
while not kraj:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            kraj = True
        if dogadjaj.type == pygame.KEYDOWN:
            # strelicom na gore ili razamkom podizemo pticu
            if dogadjaj.key == pygame.K_UP or dogadjaj.key == pygame.K_SPACE:
                ptica_y -= 8

    # Crtamo scenu
    ekran.fill(BELA)
    # Crtamo pticu
    pygame.draw.circle(ekran, PLAVA, (ptica_x, ptica_y), ptica_r)
    # Crtamo prepreke
    for pravougaonik in prepreke:
        pygame.draw.rect(ekran, ZELENA, pravougaonik)
    pygame.display.flip()

    # Ptica pada
    ptica_y += 3

    # Prepreke se pomeraju nalevo
    for pravougaonik in prepreke:
        pravougaonik[0] -= 3

    # Proveravamo da li se poslednja prepreka dovoljno pomerila da bi se ubacila nova prepreka
    if prepreke[-1][0] + prepreke[-1][2] + rastojanje_nove_prepreke < sirina:
        # ubacujemo novu prepreku
        prepreke = prepreke + napravi_prepreku()
        # odredjujemo kada treba da se pojavi naredna prepreka
        rastojanje_nove_prepreke = odredi_rastojanje_nove_prepreke()

    # Izbacujemo prepreke koje su ispale sa levog dela ekrana
    while prepreke[0][0] + prepreke[0][2] < 0:
       prepreke.pop(0)

    # Proveravamo da li je ptica pala na zemlju
    if ptica_y + ptica_r > visina:
        kraj = True

    # Proveravamo da li je ptica udarila u neku prepreku
    for pravougaonik in prepreke:
        if krug_sece_pravougaonik((ptica_x, ptica_y, ptica_r), pravougaonik):
            kraj = True

    # ogranicavamo brzinu na 50 fps
    sat.tick(50)

pygame.quit()
