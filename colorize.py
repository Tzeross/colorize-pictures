import requests
import os

# get your API KEY from <https://deepai.org>
# you need to make a free account
MY_API_KEY = 'put-your-API-key-here'

# path where you keep your pictures
# can be a folder of folders of pictures, or just a folder of pictures
# make sure to end it in /
mypath = "/path/to/the/folder/with/your/pictures/"

# create list of all folders in "mypath"
(_, folders, _) = next(os.walk(mypath))

# if list of folders is empty
if not folders:
    folders = [""] 

for myfolder in folders:

    # create list of all files in "myfolder"
    (_, _, files) = next(os.walk(mypath + myfolder + "/"))

    for myfile in files:

        # colorize
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={
                'image': open(mypath + myfolder + "/" + myfile, 'rb'),
            },
            headers={'api-key': MY_API_KEY}
        )

        # download file produced by colorize website
        try:
            dl = requests.get(r.json()['output_url'])
        except:
            print("Error with file: " + myfolder + "/" + myfile)

        # make folder "colorized" if it doesn't exist
        if not os.path.exists(mypath + 'colorized'):
            os.makedirs(mypath + 'colorized')

        # make folder "myfolder" if it doesn't exist
        if not os.path.exists(mypath + 'colorized/' + myfolder):
            os.makedirs(mypath + 'colorized/' + myfolder)

        # save downloaded file to the "colorized/myfolder" folder
        with open(mypath + "colorized/" + myfolder + "/" + myfile, 'wb') as f:
            f.write(dl.content)

    # end files for
# end folders for
