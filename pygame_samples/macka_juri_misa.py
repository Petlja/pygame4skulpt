import pygame, random, math

# funkcija rotira sliku image oko njenog centra za dati ugao u stepenima image
def rot_center(image, angle):
    loc = image.get_rect().center
    rot_image = pygame.transform.rotate(image, angle)
    rot_image.get_rect().center = loc
    return rot_image

# inicijalizacija biblioteke pygame
pygame.init()

# sat koji kontrolise brzinu igre
sat = pygame.time.Clock()

# boje i fontovi koje se koriste
BELA = (255, 255, 255)
CRNA = (0, 0, 0)
font = pygame.font.SysFont("Arial", 72)

# ukljucujemo pomeranje likova duzim drzanjem tastera na tastaturi
pygame.key.set_repeat(50, 50)

# kreiramo ekran
(sirina, visina) = (400, 300)
ekran = pygame.display.set_mode((sirina, visina))

# ucitavamo slike misa i macke i postavljamo nijansu providnosti
macka = pygame.image.load('cat.png').convert()
macka.set_colorkey(BELA)
mis = pygame.image.load('mouse.png').convert()
mis.set_colorkey(BELA)

# mis je inicijalno postavljen u centar ekrana i okrenut nadesno
mis_x = sirina // 2 - mis.get_width() // 2
mis_y = visina // 2 - mis.get_height() // 2
mis_ugao = 0

# macka je inicijalno postavljena u gornji levi ugao ekrana
macka_x = 0
macka_y = 0

kraj_igre = False

kraj = False
while not kraj:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            kraj = True
        if dogadjaj.type == pygame.KEYDOWN:
            # tasterima na tastaturi pomeramo macku
            macka_brzina = 5
            if dogadjaj.key == pygame.K_LEFT:
                macka_x -= macka_brzina
            elif dogadjaj.key == pygame.K_RIGHT:
                macka_x += macka_brzina
            elif dogadjaj.key == pygame.K_UP:
                macka_y -= macka_brzina
            elif dogadjaj.key == pygame.K_DOWN:
                macka_y += macka_brzina

    if not kraj_igre:
        # pomeramo misa za 5 koraka u smeru u kojem je okrenut
        mis_brzina = 5
        mis_x += int(mis_brzina * math.cos(math.radians(mis_ugao)))
        mis_y -= int(mis_brzina * math.sin(math.radians(mis_ugao)))
        mis_rot = rot_center(mis, mis_ugao)
        # u 10% slucajeva mis menja svoj smer kretanja za +- 20 stepeni
        if (random.randint(1, 100) <= 10):
            mis_ugao += random.randint(-20, -20)

        # proveravamo da li je mis ispao iz ekrana - ako jeste, okrecemo ga
        if mis_x < 0 or mis_x + mis_rot.get_width() > sirina:
            mis_ugao = 180 - mis_ugao
        if mis_y < 0 or mis_y + mis_rot.get_height() > visina:
            mis_ugao = mis_ugao + 180

        # iscrtavamo misa i macku
        ekran.fill(BELA)
        ekran.blit(mis_rot, (mis_x, mis_y))
        ekran.blit(macka, (macka_x, macka_y))
        pygame.display.flip()

        # proveravamo da li je macka dosla do misa tako sto
        # proveravamo da li se njihovi pravougaonici seku
        macka_rect = pygame.Rect(macka_x, macka_y, macka.get_width(), macka.get_height())
        mis_rect = pygame.Rect(mis_x, mis_y, mis_rot.get_width(), mis_rot.get_height())
        if macka_rect.colliderect(mis_rect):
            # ako jeste, proglasava se kraj igre
            kraj_igre = True
    else:
        # Na centru ekrana se prikazuje poruka da je igra zavrsena 
        ekran.fill(BELA)
        tekst = font.render("Kraj!!!", True, CRNA)
        tekst_x = sirina // 2 - tekst.get_width() // 2
        tekst_y = visina // 2 - tekst.get_height() // 2
        ekran.blit(tekst, (tekst_x, tekst_y))
        pygame.display.flip()

    # ogranicavamo brzinu na 24 slike u sekundi
    sat.tick(24)

# iskljucujemo biblioteku pygame
pygame.quit()
