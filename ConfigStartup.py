import os

def MakeStartup(filename):
    os.chdir("/usr/bin/")
    f = open("startup.sh","w+")
    f.write("#!/bin/bash\n"+
        "/home/%s" % filename)
    f.close()
    os.system("chmod u+x /usr/bin/%s", filename)
    MakeService(filename)

def MakeService(filename):
    f = open("/lib/systemd/%s.service", filename)
    f.write("[Unit]\n"+
        "Description=Startup Script\n"+
        "[Service]\n"+
        "Type=simple\n"+
        "ExecStart=/usr/bin/%s.sh\n"+
        "[Install]\n"+
        "WantedBy=multi-user.target", filename)
    f.close()
    os.chdir("/etc/systemd/system/")
    os.system("ln /lib/systemd/%s.service scriptname.service", filename)
    SetConfig(filename)
    
def SetConfig(filename):
    os.system("systemctl daemon-reload")
    os.system("systemctl start %s.service", filename)
    os.system("systemctl enable %s.service", filename)

MakeStartup("startup")
