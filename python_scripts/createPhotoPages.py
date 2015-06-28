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
        newPhoto = newPhoto.replace('<replacePhotoName>', photoName.split('.')[0].replace('_', ' '))
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
        stringLinks = '<a class="btn btn-link" role="button" href="photos.html">' + dir + '</a> ' + stringLinks
    else:
        stringLinks = '<a class="btn btn-link" role="button" href="' + dir + 'photos.html">' + dir + '</a> ' + stringLinks


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
    stringToWrite = stringToWrite + '<div class="posLeft">' + stringLinks#sm_width  pull-left



    stringToWrite = stringToWrite + '<div class="dropdown hidden-md hidden-lg hidden-sm noNewLine">\
        <button class="btn btn-link dropdown-toggle" type="button" id="menu1" data-toggle="dropdown">Photos<span class="caret"></span></button>\
        <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">'
            
    for photoSectionDir in os.listdir('../images/photos/' + dir):
        if photoSectionDir == '.DS_Store':
            continue
        stringToWrite = stringToWrite + '<li role="presentation"><a role="menuitem" tabindex="-1" href="#' + photoSectionDir + '">' + photoSectionDir.replace('_', ' ') + '</a></li>'
    stringToWrite = stringToWrite + '</ul></div>'

            

    # the right hand nav bar
    stringToWrite = stringToWrite + '<div class="list-group nv_width pull-right hidden-xs"> <a href="#" class="list-group-item disabled"><strong>Photos</strong></a>'
    for photoSectionDir in os.listdir('../images/photos/' + dir):
        if photoSectionDir == '.DS_Store':
            continue
        stringToWrite = stringToWrite + '<a href="#' + photoSectionDir + '" class="list-group-item">' + photoSectionDir.replace('_', ' ') + '</a>'
    stringToWrite = stringToWrite + '</div>'

    # the photo sections
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










