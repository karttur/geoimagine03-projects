'''
Created on 2 Mar 2021

@author: thomasgumbricht
'''

# Standard library imports

from os.path import join

# Package application imports

from geoimagine.projects import SetupProcesses

if __name__ == "__main__":
    
    prodDB = 'geoimagine'   
        
    projPath = join ('doc','CopernicusDEM')
    
    projFN ='CopDEM_mosaic_arctic-hydro-regions.txt'
      
    procLL = SetupProcesses(projPath, projFN, prodDB)