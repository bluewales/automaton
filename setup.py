"""
Script to setup your Python 3 environment to run things from fwutils.
It is intended that this should work on windows, linux, and osx computers.
"""
from subprocess import call
from sys import platform
import os

# Example
if __name__ == '__main__':
    pip = 'pip3'
    if platform == 'win32':
        pip = 'pip'

    # Misc
    call(pip + ' install pylint', shell=True)

    # For QA Tests
    call(pip + ' install fluent-logger', shell=True)
    call(pip + ' install pyga', shell=True)
    call(pip + ' install wheel', shell=True)

    if platform == 'win32':
        call(pip + ' install reqs\mysqlclient-1.3.9-cp35-cp35m-win_amd64.whl', shell=True)
        call(pip + ' install reqs\mysqlclient-1.3.9-cp35-cp35m-win32.whl', shell=True)
    else:
        call(pip + ' install mysqlclient', shell=True)

    call(pip + ' install versions', shell=True)
    call(pip + ' install pySerial', shell=True)
    call(pip + ' install pyTest', shell=True)
    call(pip + ' install numpy', shell=True)
    call(pip + ' install pandas', shell=True)

    call(pip + ' install neat-python')
    call(pip + ' install graphviz')
    call(pip + ' install --upgrade tensorflow')
    call(pip + ' install matplotlib')

    call(pip + ' install --upgrade tensorflow')
    call(pip + ' install requests')

    call(pip + ' install flask')
    if platform == 'win32':
        local_dir = os.path.dirname(__file__)
        msi_path = os.path.join(local_dir, "reqs\graphviz-2.38.msi")
        print(msi_path)
        os.startfile(os.path.normpath(msi_path))

