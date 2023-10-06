language: python
python:
  - "3.8"  # Choose the Python version you're using

# Install any dependencies needed for testing
#install:
#pip install -r requirements.txt

# Run your tests
script:
  - python -m unittest discover tests/
