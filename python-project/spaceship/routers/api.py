from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/name')
def get_student() -> dict:
    return {'name': 'Pavlo'}
