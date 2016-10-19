# updates the copyright information for all .cs files
# usage: call recursive_traversal, with the following parameters
# parent directory, old copyright text content, new copyright text content

import os


# be sure to include double \\ for exclude to correctly match strings, has potential to loop through array for 
# multiple dirs.
excludedir = [".\\test"]

def update_source(filename, oldcopyright, copyright):
    utfstr = chr(0xef)+chr(0xbb)+chr(0xbf)
    fdata = file(filename,"r+").read()
    isUTF = False
    if (fdata.startswith(utfstr)):
        isUTF = True
        fdata = fdata[3:]
    if (oldcopyright != None):
        if (fdata.startswith(oldcopyright)):
            fdata = fdata[len(oldcopyright):]
    if not (fdata.startswith(copyright)):
        print "updating "+filename
        fdata = copyright + fdata
        if (isUTF):
            file(filename,"w").write(utfstr+fdata)
        else:
            file(filename,"w").write(fdata)

def recursive_traversal(dir,  oldcopyright, copyright):
    global excludedir
    fns = os.listdir(dir)
    print "listing "+dir
    for fn in fns:
        fullfn = os.path.join(dir,fn)
        if (fullfn in excludedir):
            print "++++++++++++++++++++++++++++++++++++++++++" #A checking point to be sure excluded dir is correct
            continue
        if (os.path.isdir(fullfn)):
            recursive_traversal(fullfn, oldcopyright, copyright)
        else:
            if (fullfn.endswith(".js") or fullfn.endswith(".css")):
                update_source(fullfn, oldcopyright, copyright)
            elif (fullfn.endswith(".html")):
                update_source(fullfn, oldcopyright, file("copyrightTextHtml.txt","r+").read())    


#call def's 
oldcright = file("oldcr.txt","r+").read()
cright = file("copyrightTextJsCss.txt","r+").read()
recursive_traversal(".", oldcright, cright)
exit()


