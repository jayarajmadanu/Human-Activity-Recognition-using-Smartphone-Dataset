from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path) -> List[str]:
    '''
    This function will return required packeges in a list
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='HumanActivityRecognitionusingSmartphoneDataset',
    version='0.0.1',
    author='Jayaraj Madanu',
    author_email='Jayarajmadany@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)