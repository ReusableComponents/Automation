#
#	Automated setup script for python server associated
#	with RokuStreak
#	@author: Hayden McParlane
#	@creation-date: 6.15.2016
import subprocess

PIP = r"pip3"
APTITUDE = r"apt-get"
GIT = r"git"

class Dependency(object):
    def __init__(self, manager, name):
        self.manager = manager
        self.name = name
        
class PackageCollection(object):
    def __init__(self, package_manager, packages):
        self.manager = package_manager
        self.packages = packages
        
    def install(self):
        raise NotImplementedError()
        
class AptitudeCollection(PackageCollection):
    def __init__(self, packages):
        PackageCollection.__init__(self, APTITUDE, packages)
        
    def install(self):
        for package in self.packages:
            return_code = subprocess.call(["sudo", self.manager, "install", package])
               
class PipCollection(PackageCollection):
    def __init__(self, packages):
        PackageCollection.__init__(self, PIP, packages)
        
    def install(self):
        for package in self.packages:
            return_code = subprocess.call(["sudo", self.manager, "install", package])
        
class GitCollection(PackageCollection):
    def __init__(self, repositories):
        PackageCollection.__init__(self, GIT, repositories)
        
    def install(self):
        
        # TODO: Before install, ensure git CLI is installed
        
        for package in self.packages:
            return_code = subprocess.call([self.manager, "clone", package])
    
def run_install(colls):
    for collection in colls:
        collection.install()
    
def main():
    # TODO: Ensure script is run using root priv
    
    # TODO: Implement usage
    
    apt_packages = ( r"python3-pip",
                 r"python-dev" ,
                 r"mongodb",
                 r"gir1.2-webkit-3.0")
    
    pip_packages = ( r"flask",
                 r"enum34",
                 r"requests",
                 r"grequests",
                 r"pymongo")
    
    git_repos = ( r"https://github.com/HaydenMcParlane/DesignPatterns",
                  r"https://github.com/ReusableComponents/Authentication")
    
    collections = ( AptitudeCollection(apt_packages),
                    PipCollection(pip_packages),
                    GitCollection(git_repos) )
    
    run_install(collections)    
    
    # TODO: After install modify environment
    
    # TODO: Add ...../Authentication/py/scram/ to PYTHONPATH
    
    # TODO: Add ...../DesignPatterns/pypatterns/ to PYTHONPATH
    
    # TODO: Add ...../Streak/python to PYTHONPATH
    
    # TODO: Create necessary directory for package pymongo (/data/db)
    
if __name__== "__main__":
    main()
