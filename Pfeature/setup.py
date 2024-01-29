from setuptools import setup, find_packages

packagedata = {'Pfeature': ['*']}  # This will include all files in the Pfeature package

setup(
    name='Pfeature',
    version='1.0',
    description="Computation of the features of the protein and peptide sequences",
    long_description="Pfeature is a comprehensive package which will allow users to compute most of the protein features that have been discovered over the past decades...",
    author='Raghava Group',
    author_email='raghava@iiitd.ac.in',
    license='GNU General Public License v3.0',
    packages=find_packages(),
    zip_safe=False,
    package_data=packagedata,
    package_dir={'Pfeature': 'Pfeature'},
    scripts=[],
    py_modules=[]
)
