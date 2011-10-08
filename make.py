import os

def make_dist():
    os.chdir('src')
    os.system('zip -r ../selenium-ide-gocept-selenium-format.xpi *')
    os.chdir('..')

if __name__ == '__main__':
    make_dist()