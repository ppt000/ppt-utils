'''
Created on 5 Oct 2017

Simple class and instance to keep at hand some values related to the
application. The same functionalities might be found elsewhere in the standard
library, but I have not found a definitive answer anywhere.

@author: PierPaolo
'''

class _appInfo:
    '''
    Currently only holds the app name and its absolute path.
    Other fields could be added.
    '''

    def __init__(self, appname= '', apppath= ''):
        '''
        @param appname: the name of the current application, usually the first
        part of the launcher script file, without the extension.
        @param apppath: the absolute path of the launcher script file.
        '''
        self.set_name(appname)
        self.set_path(apppath)
    
    def set_name(self, name):
        self._name = name
        
    def name(self):
        return self._name

    def set_path(self, path):
        self._path = path
        
    def path(self):
        return self._path
    
'''
The unique instance of the _appInfo class that should be accessible across the application.
'''
appinfo = _appInfo()