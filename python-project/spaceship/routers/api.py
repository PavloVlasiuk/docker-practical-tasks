from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/name')
def get_student() -> dict:
    return {'name': 'Pavlo'}


@router.get('/matrices')
def get_multiplied_matrices() -> dict:
    matrix_a = np.random.randint(0, 10, (10, 10)).tolist()
    matrix_b = np.random.randint(0, 10, (10, 10)).tolist()
    product = np.dot(matrix_a, matrix_b).tolist()
    response = {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product
    }
    return response
