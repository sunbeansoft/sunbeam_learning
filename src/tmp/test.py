f = open("error.txt", "w")
try:
    {}["1"]
except Exception as e:
    print "==="
    print e.__str__()
    f.write(e.__str__())
