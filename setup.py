import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='instaclon',  
     version='0.1',
     scripts=['instaclon','calar'] ,
     author="ABIR HOSSAIN",
     author_email="abirhossain200019@gmail.com",
     description="this is Instagram cloner",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ABIRHOSSAIN10/Instagram-Cloner",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
     ],
 )
