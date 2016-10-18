def get_all_files(srchpath):
    """Get the names of all the files in a directory, recursively, 
    including path, name and size."""
    allfiles = []

    for root, dirs, files in os.walk(srchpath):
        for file in files:
            try:
                pathname = os.path.join(root, file)
                filesize = os.path.getsize(pathname)
                allfiles.append([file, pathname, filesize])
            except FileNotFoundError:
                pass
    return allfiles
