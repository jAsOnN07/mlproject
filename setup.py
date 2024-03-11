from setuptools import find_packages,setup
from typing import List

hyphan_dot='-e .'
def get_packages(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n','') for req in requirements]

        if hyphan_dot in requirements:
            requirements.remove(hyphan_dot)
    
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Jason Gonsalves',
    author_email='jasongonsalves077@gmail.com',
    packages=find_packages(),
    install_requires=get_packages('requirements.txt'),
)