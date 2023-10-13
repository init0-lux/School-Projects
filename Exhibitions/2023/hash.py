from hashlib import md5

def hashfunc(orig,  dest,  id = "Car 1",  rc = "JH01BB3922"):
    orig = md5(str(orig).encode('utf-8')).hexdigest()
    dest = md5(str(dest).encode('utf-8')).hexdigest()
    id = md5(id.encode('utf-8')).hexdigest()
    rc = md5(rc.encode('utf-8')).hexdigest()


    with open("blockchain",  'a') as f:
        strs = " | "orig +  " | " +  dest +  " | " +  id +  " | " +  rc  + " |\n"
        f.write(strs)

hashfunc(orig,  dest)
