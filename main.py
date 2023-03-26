from tkinter import *
import time
import webbrowser
url1 = 'https://www.win-rar.com/predownload.html?&L=0'
url2 = 'https://drive.google.com/file/d/1fy6DbTbsUHwYWCvtvhyb9IAW4T-i07zI/view?usp=share_link'
url3 = 'https://drive.google.com/file/d/1Iowtk_Jwt7rxwdue5EKzSI4SoDKOWiXV/view?usp=share_link'
url4 = 'https://www.internetdownloadmanager.com/download.html'
url5 = 'https://drive.google.com/file/d/1UhY5xem8MWOS7z8UTlZZXC7Nm4phS8xm/view?usp=share_link'
url6 = 'https://crystalidea.com/uninstall-tool/download '
url7 = 'https://drive.google.com/file/d/1vfBypCHfuSVAR0LVn2-A6EFUAQEgVOV6/view?usp=share_link'
url8 = 'https://drive.google.com/file/d/1P4oA3nFVX4D6hQRxA8Quh7rBV5tV0dCK/view?usp=share_link'
url9 = 'https://drive.google.com/file/d/1Tf13v8ZG6fH80TKqQFyWF3SJRl48p9ps/view?usp=share_link'
url10 = 'https://ninite.com/'



main = Tk()
main.geometry('600x600')
main.minsize(width=600, height=600)
main.maxsize(width=600, height=600)
main.resizable(width=False, height=False)
main.title('NMKVIETNAM - After Windows Setup Apps Downloader Tool')

def winrardown():
    webbrowser.open(url1)
    time.sleep(3)
    print('url1 -> Opened')
def winrarcrack():
    webbrowser.open(url2)
    time.sleep(3)
    print('url2 -> Opened')
def hwidgendown():
    webbrowser.open(url3)
    time.sleep(3)
    print('url3 -> Opened')
def idmdown():
    webbrowser.open(url4)
    time.sleep(3)
    print('url4 -> Opened')
def idmcrack():
    webbrowser.open(url5)
    time.sleep(3)
    print('url5 -> Opened')
def utdown():
    webbrowser.open(url6)
    time.sleep(3)
    print('url6 -> Opened')
def utcrack():
    webbrowser.open(url7)
    time.sleep(3)
    print('url7 -> Opened')
def aior():
    webbrowser.open(url8)
    time.sleep(3)
    print('url8 -> Opened')
def dbdown():
    webbrowser.open(url9)
    time.sleep(3)
    print('url9 -> Opened')
def ninite():
    webbrowser.open(url10)
    time.sleep(3)
    print('url10 -> Opened')
def quit():
    main.destroy()


passwordofall = Label(main, text='Password: nmkvietnam').grid(row=0, column=0)

aoi = Label(main, text='All In One Runtimes').grid(row=1, column=0)
Button(main, text='Download', command=aior).grid(row=1, column=1)

aoi = Label(main, text='Drivers Booster Portable').grid(row=2, column=0)
Button(main, text='Download', command=dbdown).grid(row=2, column=1)

Hwidgen = Label(main, text='Hwidgen').grid(row=3, column=0)
Button(main, text='Download', command=hwidgendown).grid(row=3, column=1)

idm = Label(main, text='Internet Download Manager').grid(row=4, column=0)
Button(main, text='Download', command=idmdown).grid(row=4, column=1)
Button(main, text='Crack', command=idmcrack).grid(row=4, column=2)

ninitelink = Label(main, text='Ninite').grid(row=5, column=0)
Button(main, text='Go to link', command=ninite).grid(row=5, column=1)

ut = Label(main, text='Uninstall Tool').grid(row=6, column=0)
Button(main, text='Download', command=utdown).grid(row=6, column=1)
Button(main, text='Crack', command=utcrack).grid(row=6, column=2)

winrar = Label(main, text='Winrar').grid(row=7, column=0)
Button(main, text='Download', command=winrardown).grid(row=7, column=1)
Button(main, text='Crack', command=winrarcrack).grid(row=7, column=2)

exit = Label(main, text='Exit').grid(row=8, column=0)
Button(main, text='Click Me', command=quit).grid(row=8, column=1)










main.mainloop()