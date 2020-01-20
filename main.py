# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pandas as pd
import os


directory = 'H:\\WS 19-20\\Mining Software Repositories\\Assignment2'



folders = []

for filename in os.listdir(directory):
    try:
        for subdir in os.listdir(directory + '\\' +filename):
            if subdir == 'pom.xml':
                folders.append(filename)
    except:
        print('Not a folder')

repos = []
versions = []
antler = []
antler_v = []

for subdir in folders:
    repos.append(subdir)
    try:
        tree = ET.parse('H:\WS 19-20\Mining Software Repositories\Assignment2\\' + subdir + '\\pom.xml')
        root = tree.getroot()
        xmlns = '{' + root.tag.split('}')[0].strip('{') + '}'
        callevent=root.find(xmlns + 'dependencies')
        modelversion = root.find(xmlns + 'modelVersion')
        versions.append(modelversion.text)

    except:    
        print("Error occurd!!!")
    
    try:
        moc1=callevent.findall(xmlns +'dependency')

    
        callevent=root.find(xmlns + 'dependencyManagement')
        callevent=callevent.find(xmlns + 'dependencies')
        moc1=callevent.findall(xmlns +'dependency')
    except:
        print("Error occurd!!!")
    
    try:
        a = 0
        
        for moc in moc1:
            for index,node in enumerate(moc):
                if (node.tag == xmlns + 'groupId' and node.text == 'org.antlr'):
                    a += 1
                    temp = moc[index + 2]
                    antler_v.append(temp.text)

        if(a == 0):
            callevent=root.find(xmlns + 'dependencyManagement')
            callevent=callevent.find(xmlns + 'dependencies')
            moc1=callevent.findall(xmlns +'dependency')
            for moc in moc1:
                for index,node in enumerate(moc):
                    if (node.tag == xmlns + 'groupId' and node.text == 'org.antlr'):
                        a += 1
                        temp = moc[index + 2]
                        antler_v.append(temp.text)

        if a != 0 :
            antler.append(1)
        else:
            antler.append(0)
    except:
        antler.append(0)
        print('Error occurd!!!')        
        
        
df = pd.DataFrame(list(zip(repos,versions,antler,antler_v)),columns=['repo_name','maven_version','antler_dependency','a_v'])

print(df)
