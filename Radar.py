import requests as rq
import os, sys
import time
import subprocess as sp

def getRadarSite():
    NWS_Sites = ["ALASKA","CARIB","CENTGRLAKES","CONUS-LARGE","CONUS","GUAM","HAWAII","KABR","KABX","KAKQ","KAMA","KAMX","KAPX","KARX","KATX","KBBX","KBGM","KBHX","KBIS","KBLX","KBMX","KBOX","KBRO","KBUF","KBYX","KCAE","KCBW","KCBX","KCCX","KCLE","KCLX","KCRP","KCXX","KCYS","KDAX","KDDC","KDFX","KDGX","KDIX","KDLH","KDMX","KDOX","KDTX","KDVN","KDYX","KEAX","KEMX","KENX","KEOX","KEPZ","KESX","KEVX","KEWX","KEYX","KFCX","KFDR","KFDX","KFFC","KFSD","KFSX","KFTG","KFWS","KGGW","KGJX","KGLD","KGRB","KGRK","KGRR","KGSP","KGWX","KGYX","KHDC","KHDX","KHGX","KHNX","KHPX","KHTX","KICT","KICX","KILN","KILX","KIND","KINX","KIWA","KIWX","KJAX","KJGX","KJKL","KLBB","KLCH","KLGX","KLNX","KLOT","KLRX","KLSX","KLTX","KLVX","KLWX","KLZK","KMAF","KMAX","KMBX","KMHX","KMKX","KMLB","KMOB","KMPX","KMQT","KMRX","KMSX","KMTX","KMUX","KMVX","KMXX","KNKX","KNQA","KOAX","KOHX","KOKX","KOTX","KPAH","KPBZ","KPDT","KPOE","KPUX","KRAX","KRGX","KRIW","KRLX","KRTX","KSFX","KSGF","KSHV","KSJT","KSOX","KSRX","KTBW","KTFX","KTLH","KTLX","KTWX","KTYX","KUDX","KUEX","KVAX","KVBX","KVNX","KVTX","KVWX","KYUX","NORTHEAST","NORTHROCKIES","PABC","PACG","PACNORTHWEST","PACSOUTHWEST","PAEC","PAHG","PAIH","PAKC","PAPD","PGUA","PHKI","PHKM","PHMO","PHWA","SOUTHEAST","SOUTHMISSVLY","SOUTHPLAINS","SOUTHROCKIES","TJUA","UPPERMISSVLY"]
    while True:
        w88b = input('Enter the radar site to observe: ')

        for site in NWS_Sites:
            if w88b.upper().strip() == site:
                #VALID SITE FOUND!
                return w88b.upper().strip()
            else:
                continue
        # NOT IN LIST REJECT
        print('Invalid NWS W88B site, please select a proper site.')


def getRadarScan(site):
    while True:
        
        URL = 'https://radar.weather.gov/ridge/standard/' + site.upper().strip() + '_0.gif'
        currentRadar = rq.get(URL)

        if currentRadar.status_code != 200:
            print('Network issue, retrying...')
            time.sleep(10)
            continue
        else:
            break

    with open('/tmp/currRadar.gif', 'wb') as f: 
        f.write(currentRadar.content)

def readRadarScan():
    viewer = sp.Popen(['/usr/bin/xdg-open', '/tmp/currRadar.gif'])
    return viewer
    
def cleanup(viewer):
    viewer.kill()
    os.remove('/tmp/currRadar.gif')


def mainLoop():

    selRadar = getRadarSite()

    while True:
        getRadarScan(selRadar)

        print('Scan fetched...')

        viewerProccess = readRadarScan()

        time.sleep(300)

        print('Next scan most likely finshed, fetching...')

        cleanup(viewerProccess)


        


if __name__ == "__main__":
    mainLoop()

