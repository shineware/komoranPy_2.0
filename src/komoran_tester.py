'''
Created on 2014. 12. 24.

@author: shin285
'''
from komoran import KomoranClass

def main():
    komoran = KomoranClass(modelPath="modelsasdf")
    print(komoran.analyze("감기는 자주 걸리는 병이다"))
    print('hello')


if __name__ == '__main__':
    main()