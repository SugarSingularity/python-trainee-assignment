import asyncio
from Python_trainee_assignment.FromMatrixToList import prepare_matrix, get_matrix, FromMatrixToList

TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]
PREPARED_MATRIX = [[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120],
                   [130, 140, 150, 160]]

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


def test_prepare_matrix():
    with open("matrix_text.txt") as file:
        assert prepare_matrix(file.read()) == PREPARED_MATRIX

    assert prepare_matrix("") == []
    assert prepare_matrix("+_____+\n| 1 | 3 |\n+_____+") == []


def test_FromMatrixToList():
    output_matrix = []
    FromMatrixToList(PREPARED_MATRIX, output_matrix)
    assert output_matrix == TRAVERSAL


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
