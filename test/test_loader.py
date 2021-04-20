from envdiff.loader import Loader

file_loader = Loader()

print(file_loader.read_file_contents('./.env-dev'))

def test_case():
    assert(3 != 3)

def test_case_two():
    assert(3 == 3)