#######################################################
# Model Name: download.py
# Usage     : to download files from the internet by providing url as an argument
# Date      : 10-Dec-2022
# Author    : Arati Junghare
########################################################
import os
import sys
import requests


def main():
    if 3 != len(sys.argv):
        print('Please pass url and output directory\nex. download.py url out_dir')
        sys.exit()
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',}

    first_input = sys.argv[1].strip()
    out_dir = sys.argv[2].strip()
    if os.path.isfile(first_input):
        with open(first_input, 'r') as f:
            urls = f.readlines()
    else:
        urls = [first_input]
    print("Total URLs to Download {}".format(len(urls)))
    for url in urls:
        url = url.strip()
        if 1 == len(url.split("://")):
            url = "http://" + url
        file_path = os.path.join(out_dir, url.split("://")[-1].split('/')[-1].strip())
        try:
            response = requests.get(url, stream=True, headers=user_agent, timeout=2)
            if response.status_code >= 200 and response.status_code <= 399:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=2048):
                        f.write(chunk)
                print(("File downloaded successfully {}".format(file_path)))
            else:
                print(("Cannot download file, server return with response code: " + str(response.status_code)))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
