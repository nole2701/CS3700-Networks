def get_credentials(param):
    param1 = param.split('ftps://')[1]
    username = param1.split(':')[0]
    param2 = param.split("ftps://" + username + ":")[1]
    password = param2.split("@")[0]
    return username, password

print(get_credentials('ftps://lertsumitkuln:CkAXZKzhoiagnYxIG1HD@ftp.3700.network/')[0])