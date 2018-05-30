def CheckBatteryStat(self):  ## 100ms check interval
    content = ""
    bat_uevent = {}
    bat_segs = [[0, 6], [7, 15], [16, 20], [21, 30], [31, 50], [51, 60], [61, 80], [81, 90], [91, 100]]

    try:
        f = open(Battery)
    except IOError:
        self._Icons["battery"] = self._Icons["battery_unknown"]
        print("CheckBatteryStat open failed")
        return False
    else:
        with f:
            content = f.readlines()
            content = [x.strip() for x in content]
            f.close()

            for i in content:
                pis = i.split("=")
                if len(pis) > 1:
                    bat_uevent[pis[0]] = pis[1]

            #        print(bat_uevent["POWER_SUPPLY_CAPACITY"])

            """
            power_current = int(bat_uevent["POWER_SUPPLY_CURRENT_NOW"])
            if power_current < 270000:
            self._Icons["battery"] = self._Icons["battery_unknown"]
            return False
            """

            if "POWER_SUPPLY_CAPACITY" in bat_uevent:
                cur_cap = int(bat_uevent["POWER_SUPPLY_CAPACITY"])
            else:
                cur_cap = 0

            cap_ge = 0

            for i, v in enumerate(bat_segs):
                if cur_cap >= v[0] and cur_cap <= v[1]:
                    cap_ge = i
                    break

            if bat_uevent["POWER_SUPPLY_STATUS"] == "Charging":
                self._Icons["battery_charging"]._IconIndex = cap_ge
                self._Icons["battery"] = self._Icons["battery_charging"]

                print("Charging %d" % cap_ge)
            else:
                self._Icons["battery_discharging"]._IconIndex = cap_ge
                self._Icons["battery"] = self._Icons["battery_discharging"]
                print("Discharging %d" % cap_ge)

    return True


def SetBatteryStat(self, bat):
    pass