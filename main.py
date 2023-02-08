import keyboard, pygame
from func import opencsv, updateoverlay, updateenv
from btpygame import pygameimage, collide, showtext

pygame.init()
screen = pygame.display.set_mode((1042, 335))
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('AllPortalsSsgTracker by DraquoDrass')
clock = pygame.time.Clock()

env = {}
file = open("settings.txt", mode="r")
the_settings = file.readlines()
for i in the_settings:
    if i[0] == "#":
        pass
    else:
        setting = i.split("=")
        setting[1] = setting[1].replace("\n", "")
        env[setting[0]] = setting[1]
file.close()

data = opencsv("assets/route.csv")
running = True
isusedasovere = False
insettings = False
waitinginput = (False, None)

nb_portal = 1
btn_add = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/add.png"), (80, 80)), (20, 230)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/add_t.png"), (80, 80)), (20, 230))
}
btn_sub = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/sub.png"), (80, 80)), (120, 230)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/sub_t.png"), (80, 80)), (120, 230))
}
btn_res = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/res.png"), (80, 80)), (220, 230)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/res_t.png"), (80, 80)), (220, 230))
}
btn_obs = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/obs.png"), (80, 80)), (942, 230)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/obs_t.png"), (80, 80)), (942, 230))
}
btn_set = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/set.png"), (80, 80)), (842, 230)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/set_t.png"), (80, 80)), (842, 230))
}

txt_height = showtext(screen, "test", "assets/Montserrat-Bold.ttf", 30, (20, 20), (255, 255, 255), "topleft")[1]
size = (txt_height, txt_height)
btn_change1 = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/change.png"), size), (0, 0)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/change_t.png"), size), (0, 0))
}
btn_change2 = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/change.png"), size), (0, 0)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/change_t.png"), size), (0, 0))
}
btn_change3 = {
    "away": pygameimage(pygame.transform.scale(pygame.image.load("assets/change.png"), size), (0, 0)),
    "target": pygameimage(pygame.transform.scale(pygame.image.load("assets/change_t.png"), size), (0, 0))
}
background = pygameimage(pygame.image.load("assets/background.png"), (0, -150))
cross = pygameimage(pygame.transform.scale(pygame.image.load("assets/not.png"), (80, 80)), (942, 230))

while running:

    if not isusedasovere:
        screen.blit(background.image, background.pos)
    else:
        hexc = "#0015ff".replace("#", "")
        screen.fill(tuple(int(hexc[i:i+2], 16) for i in (0, 2, 4)))

    if not collide(btn_set["away"], pygame.mouse.get_pos()):
        screen.blit(btn_set["away"].image, btn_set["away"].pos)
    else:
        screen.blit(btn_set["target"].image, btn_set["target"].pos)

    if not collide(btn_obs["away"], pygame.mouse.get_pos()):
        screen.blit(btn_obs["away"].image, btn_obs["away"].pos)
    else:
        screen.blit(btn_obs["target"].image, btn_obs["target"].pos)

    if not isusedasovere:
        screen.blit(cross.image, cross.pos)

    if not insettings:

        if not collide(btn_add["away"], pygame.mouse.get_pos()):
            screen.blit(btn_add["away"].image, btn_add["away"].pos)
        else:
            screen.blit(btn_add["target"].image, btn_add["target"].pos)

        if not collide(btn_sub["away"], pygame.mouse.get_pos()):
            screen.blit(btn_sub["away"].image, btn_sub["away"].pos)
        else:
            screen.blit(btn_sub["target"].image, btn_sub["target"].pos)

        if not collide(btn_res["away"], pygame.mouse.get_pos()):
            screen.blit(btn_res["away"].image, btn_res["away"].pos)
        else:
            screen.blit(btn_res["target"].image, btn_res["target"].pos)

        showtext(screen, f"Portal {nb_portal}/128", "assets/Montserrat-Bold.ttf", 30, (20, 20), (255, 255, 255), "topleft")
        showtext(screen, f"OW Coords: {data[nb_portal][2]}", "assets/Montserrat-Bold.ttf", 30, (20, 60), (255, 255, 255), "topleft")
        showtext(screen, f"NE Coords: {data[nb_portal][3]}", "assets/Montserrat-Bold.ttf", 30, (20, 100), (255, 255, 255), "topleft")
        if data[nb_portal][1] != "":
            showtext(screen, f"Angle to follow: {data[nb_portal][1]}", "assets/Montserrat-Bold.ttf", 30, (20, 140), (255, 255, 255), "topleft")
        if data[nb_portal][5] != "":
            showtext(screen, f"Note: {data[nb_portal][5]}", "assets/Montserrat-Bold.ttf", 30, (20, 180), (255, 255, 255), "topleft")
    else:
        showtext(screen, "Settings:", "assets/Montserrat-Bold.ttf", 30, (20, 20), (255, 255, 255), "topleft")
        next_len = showtext(screen, f"   Next portal: {pygame.key.name(int(env['NEXT_PORTAL']))}", "assets/Montserrat-Bold.ttf", 30, (20, 60), (255, 255, 255), "topleft")
        prev_len = showtext(screen, f"   Previous portal: {pygame.key.name(int(env['PREV_PORTAL']))}", "assets/Montserrat-Bold.ttf", 30, (20, 100), (255, 255, 255), "topleft")
        reset_len = showtext(screen, f"   Reset advancement: {pygame.key.name(int(env['RESET_ADV']))}", "assets/Montserrat-Bold.ttf", 30, (20, 140), (255, 255, 255), "topleft")
        btn_change1["away"].pos = (20+next_len[0]+13, 60)
        btn_change1["target"].pos = (20+next_len[0]+13, 60)
        if not collide(btn_change1["away"], pygame.mouse.get_pos()):
            screen.blit(btn_change1["away"].image, btn_change1["away"].pos)
        else:
            screen.blit(btn_change1["target"].image, btn_change1["target"].pos)

        btn_change2["away"].pos = (33 + prev_len[0], 100)
        btn_change2["target"].pos = (33 + prev_len[0], 100)
        if not collide(btn_change2["away"], pygame.mouse.get_pos()):
            screen.blit(btn_change2["away"].image, btn_change2["away"].pos)
        else:
            screen.blit(btn_change2["target"].image, btn_change2["target"].pos)

        btn_change3["away"].pos = (33 + reset_len[0], 140)
        btn_change3["target"].pos = (33 + reset_len[0], 140)
        if not collide(btn_change3["away"], pygame.mouse.get_pos()):
            screen.blit(btn_change3["away"].image, btn_change3["away"].pos)
        else:
            screen.blit(btn_change3["target"].image, btn_change3["target"].pos)

        if waitinginput[0]:
            showtext(screen, "Waiting for an input ...", "assets/Montserrat-Bold.ttf", 55, (20, 240), (255, 255, 255), "topleft")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if waitinginput[0]:
                if event.key != 27:
                    env[waitinginput[1]] = event.key
                else:
                    env[waitinginput[1]] = 0
                waitinginput = (False, None)
                updateenv(env)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if not insettings:
                    if collide(btn_add["target"], event.pos) and nb_portal < 128:
                        nb_portal += 1
                        updateoverlay(nb_portal)
                    elif collide(btn_sub["target"], event.pos) and nb_portal > 1:
                        nb_portal -= 1
                        updateoverlay(nb_portal)
                    elif collide(btn_res["target"], event.pos):
                        nb_portal = 1
                        updateoverlay(nb_portal)
                if collide(btn_set["target"], event.pos):
                    insettings = not insettings
                elif collide(btn_obs["target"], event.pos):
                    isusedasovere = not isusedasovere
                elif collide(btn_change1["target"], event.pos) and not waitinginput[0]:
                    waitinginput = (True, "NEXT_PORTAL")
                elif collide(btn_change2["target"], event.pos) and not waitinginput[0]:
                    waitinginput = (True, "PREV_PORTAL")
                elif collide(btn_change3["target"], event.pos) and not waitinginput[0]:
                    waitinginput = (True, "RESET_ADV")

    pygame.display.flip()
    clock.tick(60)

    if keyboard.is_pressed(env["NEXT_PORTAL"]) and nb_portal < 128:
        nb_portal += 1
        updateoverlay(nb_portal)
    elif keyboard.is_pressed(env["PREV_PORTAL"]) and nb_portal > 1:
        nb_portal -= 1
        updateoverlay(nb_portal)
    elif keyboard.is_pressed(env["RESET_ADV"]):
        nb_portal = 1
        updateoverlay(nb_portal)

pygame.quit()