#! /usr/bin/python
# -*- coding: utf-8 -*

import os

def GetListForBackup(PathForBackup):
    ListForBackup = []

    PathForBackup = os.path.realpath(PathForBackup)

    for file in os.listdir(PathForBackup):

        try:
            path = os.path.join(PathForBackup, file)
        except:
            continue
        if not os.path.isdir(path) or os.path.islink(path):
            ListForBackup.append(path)
        else:
            try:
                ListForBackup += GetListForBackup(path)
            except:
                continue
    return ListForBackup


filePath = input('Укажите путь: ')

print(GetListForBackup(filePath))

f = open('text.txt', 'w')


for file in GetListForBackup(filePath):
    f.write(file + '\n')

f.close()

