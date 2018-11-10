def make_album(singer,album,number=''):
    singer_message={
        'singer':singer,
        'album':album,
        }
    if number:
        singer_message['number']=number
    return singer_message
promat_singer='please enter your favorite singer:'
promat_singer+="\n(enter 'q' at any time to quit)"
promat_album='please enter your favorite album name:'
promat_number='please enter your favorite number of songs'
promat_number+='\n(if you can not decide a number,do not enter)'
while True:
    name=input(promat_singer)
    if name=='q':
        break
    album=input(promat_album)
    number=input(promat_number)
    singer_message=make_album(name,album,number)
    print(singer_message)
  