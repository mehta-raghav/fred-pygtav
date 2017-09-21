import pip
def install(package):
    pip.main(['install', '--upgrade', package])

if __name__ == '__main__':
    install('numpy')
    install('opencv-python')
    install('pypiwin32')

exit()
