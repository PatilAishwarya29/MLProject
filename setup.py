#reponsible for creating my machine learning application as a package and that can be installed in any project
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        """
        after reading every line there will be \n present at end of each line 
        so we are replacing \n by space. 
        """
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Aishwarya Patil',
author_email='aishwaryapatil290397@gmail.com',
packages=find_packages(),
'find_package() will look for __init__.py file and that folder will get build as project'
install_requires=get_requirements('requirements.txt')

)

    