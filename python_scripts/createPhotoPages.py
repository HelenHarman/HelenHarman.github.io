import os

#--------------------------------------------------------

###
# @param string : photoDir
# @return string
def photoString(photoDir):
    string = ''
    for photoName in os.listdir(photoDir):
        if photoName == '.DS_Store':
            continue
        
        newPhoto = singlePhoto.replace('<replacePhotoPath>', photoDir.replace('../', '') + '/' + photoName)
        newPhoto = newPhoto.replace('<replacePhotoName>', photoName.split('.')[0])
        string = string + newPhoto
    
    return string

#--------------------------------------------------------

dirs = os.listdir('../images/photos')
highest = 0

dirs.remove('.DS_Store')

for dir in dirs:
    if (int(dir) > highest) :
        highest = int(dir)


stringLinks = ''
for dir in dirs:
    if int(dir) == highest :
        stringLinks = stringLinks + '<a href="photos.html">' + dir + '</a>'
    else:
        stringLinks = stringLinks + '<a href="' + dir + 'photos.html">' + dir + '</a>'


file = open('../include/photoSection.html', 'r')
photoSection = file.read()
file.close

file = open('../include/singlePhoto.html', 'r')
singlePhoto = file.read()
file.close

file = open('../include/photoSlideShow.html', 'r')
photoSlideShow = file.read()
file.close


for dir in dirs:
    
    
    stringToWrite = '<heading.html>'
    stringToWrite = stringToWrite + stringLinks + '<div>'

    for photoSectionDir in os.listdir('../images/photos/' + dir):
        if photoSectionDir == '.DS_Store':
            continue
        
        newPhotoSection = photoSection.replace('<replaceIdName>', photoSectionDir)
        newPhotoSection = newPhotoSection.replace('<replacePanelTitle>', photoSectionDir.replace('_', ' '))
        newPhotoSection = newPhotoSection.replace('<replaceWithPhotos>', photoString('../images/photos/' + dir + '/' + photoSectionDir))
    
        stringToWrite = stringToWrite + newPhotoSection
    

    stringToWrite = stringToWrite + photoSlideShow + '</div>'

    stringToWrite = stringToWrite + '<ending.html>'


    # write photo.html page
    if int(dir) == highest :
        fileToWrite = open('../base/photos.html', 'w')
    else:
        fileToWrite = open('../base/' + dir + 'photos.html', 'w')
    fileToWrite.write(stringToWrite)
    fileToWrite.close()










