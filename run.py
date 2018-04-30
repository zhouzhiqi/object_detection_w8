import os

print('current working dir [{0}]'.format(os.getcwd()))
w_d = os.path.dirname(os.path.abspath(__file__))

def show_dir(path):
    for i in os.listdir(path):
        if os.path.isdir(i):
            print('dir',os.path.abspath(i))
            show_dir(i)
        else:
            print('fil',os.path.abspath(i))
            
show_dir(w_d)

print('change wording dir to [{0}]'.format(w_d))
os.chdir(w_d)

"""
def show_dir(path):
    for i in os.listdir(path):
        if os.path.isdir(i):
            print('dir',os.path.abspath(i))
            show_dir(i)
        else:
            print('fil',os.path.abspath(i))
            
show_dir(w_d)
"""

for l in os.popen('/bin/bash -c "cd {0} && source ./run.sh"'.format(w_d)):
    print(l.strip())
