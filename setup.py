from setuptools import setup, find_packages

setup(name="hyperspace_explorer",
      version="0.0.1",
      author="Tomasz Pietruszka",
      author_email="tomek.pietruszka@gmail.com",
      description="Tracking ML/DL experiments, helping define and explore hyper-parameter spaces",
      packages=find_packages(),
      scripts=['hyperspace_explorer/hyperspace_worker.py'],
      python_requires='>=3.7',
      install_requires=[
          'sacred>=0.8.1',
          'pymongo>=3.9.0'
      ],
      tests_require=[
            'pytest',
      ],
      )
