
from ftplib import FTP


URL = "" #FTP URL
USER = "" #FTP username
PASS = "" #FTP password

def run():
    ftp = FTP(URL, USER, PASS)
    try:
        ftp.login()
    except:
        try:
            ftp.voidcmd("NOOP")
        except:
            print("Login failed")
            return
    ftp.retrlines('LIST')
    ftp.cwd("public_html")
    ftp.cwd("movie_stuff")
    print("\n\n")
    ftp.retrlines('LIST')

    
    file = open('movies.txt','rb')                  # file to send
    ftp.storbinary('STOR movies.txt', file)     # send the file
    file.close()                                    # close file and FTP

    file = open('movies_changes.txt','rb')
    ftp.storbinary('STOR movies_changes.txt', file)
    file.close()

    file = open('tvshows.txt','rb')
    ftp.storbinary('STOR tvshows.txt', file)
    file.close()

    file = open('tvshows_changes.txt','rb')
    ftp.storbinary('STOR tvshows_changes.txt', file)
    file.close()


    ftp.quit()
run()
