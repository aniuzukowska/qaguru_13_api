from pytest_voluptuous import S
from requests import Response
from schemas.reqres import SchemaListUsers, SchemaCreateUser, SchemaUpdateUser, SchemaLoginUnsuccessful


def test_get_list_users(reqres_session):
    page_number = 2

    result: Response = reqres_session.get(
        url='/api/users',
        params={'page': page_number}
    )

    assert result.status_code == 200
    assert result.json()['page'] == page_number
    assert result.json() == S(SchemaListUsers)


def test_create_user(reqres_session):
    name = 'anna'
    job = 'qa'

    result: Response = reqres_session.post(
        url='/api/users',
        json=
        {
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(SchemaCreateUser)


def test_update_patch_user(reqres_session):
    name = 'anna'
    job = 'qa'
    id = 2

    result: Response = reqres_session.patch(
        url=f'/api/users/{id}',
        json=
        {
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(SchemaUpdateUser)


def test_delete_user(reqres_session):
    id = 2
    result: Response = reqres_session.delete(f'/api/users/{id}')
    assert result.status_code == 204


def test_login_unsuccessful(reqres_session):
    email = 'peter@klaven'

    result: Response = reqres_session.post(
        url='/api/login',
        json={
            "email": email
        }
    )

    assert result.status_code == 400
    assert result.json() == S(SchemaLoginUnsuccessful)
    assert result.json()['error'] == 'Missing password'




