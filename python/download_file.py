import requests

def DownloadFile(url, headers={}, filename=None, proxies=None):
    """ Break a file in to chunks (evrery chunk at most 1024M)
        Download every chunk to
        and then write them to
        filename (str) : 	absolute file name
                            default to the fi
    """
    local_filename = url.split('/')[-1] if not filename else filename
    temp_file = requests.get(url, headers=headers, stream=True, proxies=proxies)
    with open(local_filename, 'wb') as f:
        for chunk in temp_file.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return temp_file.status_code == requests.codes.ok
