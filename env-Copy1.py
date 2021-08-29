host = "157.230.209.171"
username = "germain_1481"
password = "a6wY6FHOCrC4drBDD6tMPLVwUfmSdVFL"

def get_connection(db, username=username, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'