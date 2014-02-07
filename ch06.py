import zipfile
import urllib
import tempfile
import re
import os
from globals import pych_url


def download_and_extract():
    # get the zip resource from the web
    web_res = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

    #save to file
    b = web_res.read()
    f = tempfile.TemporaryFile()
    f.write(b)

    #load to zip file
    zf = zipfile.ZipFile(f)

    #create a temporary folder, and extract all
    d = tempfile.mkdtemp(prefix='pych')
    zf.extractall(path=d)

    zf.close()
    f.close()

    print 'zip files folder: {d}'.format(d=d)

    return d


def main():
    """http://www.pythonchallenge.com/pc/def/channel.html"""

    #download the zip file, and extract into folder
    #d = download_and_extract()
    d = r'C:\Users\uri\AppData\Local\Temp\pychbhentw'

    #open the readme file, and get the start
    with open(os.path.join(d, 'readme.txt'), 'r') as readme_file:
        readme = readme_file.read()
        nothing = re.search('hint1: start from (\d+)', readme).group(1)
        print 'start: {start}'.format(start=nothing)
        readme_file.close()

    nothings = []
    while nothing:
        nothings.append(nothing)
        fname = nothing + '.txt'
        with open(os.path.join(d, fname)) as f:
            content = f.read()
            print '{0}: {1}'.format(fname, content)
            result = re.search('nothing is (\d+)$', content)
            if result:
                nothing = result.group(1)
            else:
                nothing = 0


if __name__ == '__main__':
    main()
