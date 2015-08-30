import os, time

#--------------------------------------------------------

###
# @param string : photoDir
# @return string
def photoString(photoDir):
    string = ''
    for photoName in os.listdir(photoDir):
        if photoName == '.DS_Store' or photoName == 'small' :
            continue
        
        newPhoto = singlePhoto.replace('<replacePhotoPath>', photoDir.replace('../', '') + '/' + photoName)
        newPhoto = newPhoto.replace('<replacePhotoPathSmall>', photoDir.replace('../', '') + '/small/' + photoName)
        newPhoto = newPhoto.replace('<replacePhotoName>', photoName.split('.')[0].replace('_', ' '))
        string = string + newPhoto
    
    return string

#--------------------------------------------------------

def getLinksHtmlString(dirs):
    stringLinks = ''
    for dir in dirs:
        if os.path.getctime('../images/photos/' + dir) == highest :
            stringLinks = '<a class="btn btn-link" role="button" href="photos.html">' + dir + '</a> ' + stringLinks
        else:
            stringLinks = '<a class="btn btn-link" role="button" href="' + dir + 'photos.html">' + dir + '</a> ' + stringLinks
    return stringLinks

#--------------------------------------------------------

def getSmallScreenNavBarHtml(dir):
    htmlString = '<div class="dropdown hidden-md hidden-lg hidden-sm noNewLine">\
                                     <button class="btn btn-link dropdown-toggle" type="button" id="menu1" data-toggle="dropdown">Photos<span class="caret"></span></button>\
                                     <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">'
    
    for photoSectionDir in os.listdir('../images/photos/' + dir):
        if photoSectionDir == '.DS_Store':
            continue
        htmlString = htmlString + '<li role="presentation"><a role="menuitem" tabindex="-1" href="#' + photoSectionDir + '">' + photoSectionDir.replace('_', ' ') + '</a></li>'
    htmlString = htmlString + '</ul></div>'
    return htmlString

#--------------------------------------------------------

def getRightHandNavBarHtml(dir):
    htmlString = '<div class="list-group nv_width pull-right hidden-xs"> <a href="#" class="list-group-item disabled"><strong>Photos</strong></a>'
    for photoSectionDir in os.listdir('../images/photos/' + dir):
        if photoSectionDir == '.DS_Store':
            continue
        htmlString = htmlString + '<a href="#' + photoSectionDir + '" class="list-group-item">' + photoSectionDir.replace('_', ' ') + '</a>'
    htmlString = htmlString + '</div>'
    return htmlString

#--------------------------------------------------------

def getPhotoSection(dir, photoSection):
    htmlString = ''
    for photoSectionDir in os.listdir('../images/photos/' + dir):
        if photoSectionDir == '.DS_Store':
            continue
        
        newPhotoSection = photoSection.replace('<replaceIdName>', photoSectionDir)
        newPhotoSection = newPhotoSection.replace('<replacePanelTitle>', photoSectionDir.replace('_', ' '))
        newPhotoSection = newPhotoSection.replace('<replaceWithPhotos>', photoString('../images/photos/' + dir + '/' + photoSectionDir))
        
        htmlString = htmlString + newPhotoSection
    return htmlString

#--------------------------------------------------------

dirs = os.listdir('../images/photos')
highest = 0

dirs.remove('.DS_Store')

for dir in dirs:
    if (os.path.getctime('../images/photos/' + dir) < highest) :
        highest = os.path.getctime('../images/photos/' + dir) # highest is the latest, which should be the main photos page


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
    
    # get links to photo pages (eg. 2014, 2015)
    stringToWrite = stringToWrite + '<div class="posLeft">' + getLinksHtmlString(dirs)#sm_width  pull-left

    # navigation bar for small screens
    stringToWrite = stringToWrite + getSmallScreenNavBarHtml(dir)

    # the right hand nav bar
    stringToWrite = stringToWrite + getRightHandNavBarHtml(dir)

    # the photo sections
    stringToWrite = stringToWrite + getPhotoSection(dir, photoSection)

    # add the slide show
    stringToWrite = stringToWrite + photoSlideShow
    
    stringToWrite = stringToWrite + '</div><ending.html>'

    # write photo.html page
    if os.path.getctime('../images/photos/' + dir) == highest :
        fileToWrite = open('../base/photos.html', 'w')
    else:
        fileToWrite = open('../base/' + dir + 'photos.html', 'w')
    fileToWrite.write(stringToWrite)
    fileToWrite.close()










