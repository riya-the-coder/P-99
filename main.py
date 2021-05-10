import os
import shutil
import time
 
def main():
    deletedFoldersCount=0
    deletedFilesCount=0
    path="\Standard_deviation-master"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folders,files in os.walk(path):
            if seconds>=getAge(rootFolder):
                removeFolders(rootFolder)
                deletedFoldersCount+=1
                break
            else:
                for folder in folders:
                    folderPath=os.path.join(rootFolder,folder)
                    if seconds>=getAge(folderPath):
                        removeFolders(folderPath)
                        deletedFoldersCount+=1
                
                for file in files:
                    filePath=os.path.join(rootFolder,file)
                    if seconds>=getAge(filePath):
                        removeFiles(filePath)
                        deletedFilesCount+=1
            
    else:
        print("path not found")
        deletedFilesCount+=1
    print("Total folders deleted",deletedFoldersCount)
    print("Total files deleted",deletedFilesCount)

def removeFiles(path):
    if not os.remove(path):
        print("path removed successfully")
    else:
        print("unable to delete the path")

def getAge(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__=="__main__":
    main()
                   



