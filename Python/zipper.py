import zipfile
import os


def zipper(folder):
    folder = os.path.abspath(folder)
    number = 1

    while True:
        zipname = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipname):
            break
        number = number + 1

    print('Creating an archive %s...' % zipname)
    backupzip = zipfile.ZipFile(zipname, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        backupzip.write(foldername)

        for filename in filenames:
            newbase = os.path.basename(folder) + '_'
            if filename.startswith(newbase) and filename.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername, filename))

    backupzip.close()
    print('Completed!')


if __name__ == "__main__":
    path = input("Enter full path name: ")
    zipper(path)
