from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
  '''
     This function will get the list of packages in the requirments file.
  '''
  requirement= []
  with open(file_path) as file_obj:
    requirement=file_obj.readlines()
    requirement=[req.replace("\n"," ") for req in requirement]
     
    if Hyphen_e_dot in requirement:
      requirement.remove(Hyphen_e_dot)

  return requirement

setup(
name='mlproject',
version='0.0.1',
author='Ankita',
author_email='ankitabohra2000@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)