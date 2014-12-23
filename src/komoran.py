'''
Created on 2014. 12. 24.

@author: shin285
'''
import jpype

class KomoranClass():
    def __init__(self, modelPath):
        classpath = ('../lib/komoran-2.4-e.jar:'
                 '../lib/shineware-ds-1.0.jar:'
                '../lib/shineware-common-2.0.jar')   
        jpype.startJVM(jpype.getDefaultJVMPath(),"-Dfile.encoding=UTF-8","-Djava.class.path=%s" % (classpath))
        
        komoranPkg = jpype.JPackage('kr').co.shineware.nlp.komoran.core.analyzer  # get the package
        Komoran = komoranPkg.Komoran
        self.komoran = Komoran("/Users/shin285/Documents/workspace_shineware/KOMORAN_2.0_beta/models")  # create an instance of the class
#         self.komoran.setUserDic("/Users/shin285/Documents/workspace_shineware/KOMORAN_2.0_beta/user_data/dic.user")
#         s = k.analyze('제이디에프 바람과 함께 사라지다를 봤습니다.')
#         print(s)
    def setUserDic(self,userDic):
        self.komoran.setUserDic(userDic)

    def analyze(self,inStr):
        return self.komoran.analyze(inStr,2)
        
        