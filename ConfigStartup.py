import os

def ConfigCondaEnvVars(filepath):
    os.chdir("$CONDA_PREFIX")
    # Setup the activate file
    os.system("mkdir -p ./etc/conda/activate.d")
    os.system("touch ./etc/conda/activate.d/env_vars.sh")
    env_var = open("./etc/conda/activate.d/env_vars.sh")
    env_var.write("#!/bin/sh\nexport MY_FILE=%s", filepath)
    # Setup the deactivate file
    os.system("mkdir -p ./etc/conda/deactivate.d")
    os.system("touch ./etc/conda/deactivate.d/env_vars.sh")
    env_var = open("./etc/conda/activate.d/env_vars.sh")
    env_var.write("#!/bin/sh\nunset %s", filepath)

def MakeStartup(filename):
    ConfigCondaEnvVars( ("/usr/bin/"+filename) )
    os.chdir("/usr/bin/")
    f = open("startup.sh","w+")
    f.write("#!/bin/bash\n"+
        "%s/etc/conda/activate.d/%s" % filename)
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
    os.system("ln /lib/systemd/%s.service %s.service", filename, filename)
    SetConfig(filename)
    
def SetConfig(filename):
    os.system("systemctl daemon-reload")
    os.system("systemctl start %s.service", filename)
    os.system("systemctl enable %s.service", filename)

MakeStartup("startup")
