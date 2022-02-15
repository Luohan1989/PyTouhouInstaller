import requests
import os.path
from os import path
import list as info
import os as o
local_filename ='joe mama'
version = 'v0.3'

def main():
    if path.exists("7za.exe"):
        clear()
        o.system('color 2')
        print(f"Wuhan's Very Good Touhou Installer {version}")
        print()
        print('if possible pls turn off your antivirus, it may interfere with this operation')
        o.system('color 9')
        print(info.Menu)
        print()
        print('Input your games corresponding number')
        install(input('>'))
    else:
        print('7za.exe is missing and must be included for proper usage')
        input('press enter to dismiss')
    

def download_file(url):
    global local_filename
#    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename
    
def install(number):
    global local_filename
    if number == '6':
        
        print('Your Game is now downloading please wait warmly until I respond.')
        local_filename = (info.touhou6['file_name'])
        download_file(info.touhou6['url'])
        dl_finish()
        return local_filename
        
    elif number == '7':

        print('Your Game is now downloading please wait warmly until I respond.')
        local_filename = (info.touhou7['file_name'])
        download_file(info.touhou7['url'])
        dl_finish()
        return local_filename

    elif number == '8':

        print('Your Game is now downloading please wait warmly until I respond.')
        local_filename = (info.touhou8['file_name'])
        download_file(info.touhou8['url'])
        dl_finish()
        return local_filename

    else:
        print('That choice simply doesnt exist')
        print('Your input: ' + number)
        input('click enter to dismiss.')
        main()

def dl_finish():
        print()
        print('Your Game has finished downloading.')
        extract()

def extract():
    print('Your game is now being extracted automatically.')
    print()
    print('Please wait warmly until I respond.')
    o.system('sleep 5')
    o.system(f'7za.exe x {local_filename}')
    clear()
    print('Extracting has finished.')
    try:
        print()
        print('Attempting to delete the zip.')
        o.system('sleep 5')
        o.system(f'del {local_filename}')
    except:
        print('something has went wrong with deleting the file (probably the antivirus).')
        print()
        print('please delete the zip yourself.')
    print('Check folder and run the app with the games name (i.e.: Touhou06).')
    print()
    print("If you are experiencing trouble please read the instructions in the game's folder.")
    print()
    input('click enter to dismiss')
def clear():
    o.system('cls')
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'GAH!!! THE PROGRAM HAS CRASHED: {e}')