import os.path


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/..'
rel = lambda p: os.path.join(PROJECT_ROOT, p)
