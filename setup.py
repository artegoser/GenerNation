from setuptools import setup, find_packages
 
setup(name='GenerNation',
      version='0.0.8',
      url='https://github.com/artegoser/GenerNation',
      license='MIT',
      author='artegoser',
      author_email='artegoser@gmail.com',
      description='Tool for generating various characters',
      packages=['GenerNation'],
      long_description_content_type='text/markdown',
      long_description=open('README.md').read(),
      zip_safe=False)