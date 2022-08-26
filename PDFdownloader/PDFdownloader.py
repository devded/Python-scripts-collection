
import urllib.request

def download(tutorialName):
    url = f'https://www.tutorialspoint.com/{tutorialName}/{tutorialName}_tutorial.pdf'

    downloadLocation = '<location>'

    pdf = urllib.request.urlopen(url)
    with open(downloadLocation + tutorialName +  '.pdf', 'wb') as saveFile:
        saveFile.write(pdf.read())

if __name__ == '__main__':
    tutorialName = input('Name of the pdf to be downloaded: ')
    download(tutorialName)