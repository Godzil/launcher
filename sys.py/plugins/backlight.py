from .plugin import Plugin
import time
import config


class Backlight(Plugin):
    def __init__(self):
        self.current_brightness = -1
        self.last_even = 0

    def event_handler(self):
        pass

    def tick(self):
        global everytime_keydown, last_brt

        cur_time = time.time()

        if cur_time - everytime_keydown > 40:
            print("timeout, dim screen %d" % int(cur_time - everytime_keydown))

            try:
                f = open(config.BackLight, "r+")
            except IOError:
                pass
            else:
                with f:
                    content = f.readlines()
                    content = [x.strip() for x in content]
                    brt = int(content[0])
                    if brt > 1:
                        last_brt = brt  ## remember brt for restore
                        brt = 1
                        f.seek(0)
                        f.write(str(brt))
                        f.truncate()
                        f.close()

                        main_screen._TitleBar._InLowBackLight = 0

            everytime_keydown = cur_time

def RestoreLastBackLightBrightness(main_screen):
    global last_brt

    if last_brt == -1:
        return

    try:
        with open(config.BackLight, "r+") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            brt = int(content[0])
            if brt < last_brt:
                f.seek(0)
                f.write(str(last_brt))
                f.truncate()
                f.close()
                last_brt = -1
                main_screen._TitleBar._InLowBackLight = -1

    except IOError:
        print("RestoreLastBackLightBrightness open %s failed, try to adjust brightness in Settings" % config.BackLight)


def tick(main_screen):
    return True