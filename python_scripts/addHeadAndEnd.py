import os

file = open('../include/heading.html', 'r')
heading = file.read()
file.close()

file = open('../include/ending.html', 'r')
ending = file.read()
file.close()

for fileName in os.listdir('../base/'):
    file = open('../base/' + fileName, 'r')
    content = file.read()
    file.close()
    
    content = content.replace('<heading.html>', heading)
    content = content.replace('<ending.html>', ending)
    
    content = content.replace('<li><a href="' + fileName + '">', '<li class="active"><a href="#">')

    if os.path.exists('../' + fileName):
        os.remove('../' + fileName)

    file = open('../' + fileName, 'w')
    file.write(content)
    file.close()
