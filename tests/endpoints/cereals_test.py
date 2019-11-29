import json
import mock


@mock.patch('app.endpoints.cereals.Cereal')
def test_get_cereals(mock_cereal_model, testapp):
    mock_cereal_model.get_cereals = mock.MagicMock(return_value=[])

    response = testapp.get('/cereals')

    assert response.status_code == 200
    assert json.loads(response.data) == []


def test_get_cereal(testapp):
    NAME = 'All-Bran with Extra Fiber'

    response = testapp.get(f'/cereals/{NAME}')

    assert response.status_code == 200
    assert json.loads(response.data) == {
        'calories': 50.0,
        'carbo': 8.0,
        'fat': 0.0,
        'fiber': 14.0,
        'name': 'All-Bran with Extra Fiber',
        'potass': 330.0,
        'protein': 4.0,
        'sodium': 140.0,
        'sugars': 0.0,
        'vitamins': 25.0
    }


@mock.patch('app.endpoints.cereals.Cereal')
def test_post_cereal(mock_cereal_model, testapp):
    BODY = {
        'calories': 50.0,
        'carbo': 8.0,
        'fat': 0.0,
        'fiber': 14.0,
        'name': 'TEST CEREAL',
        'potass': 330.0,
        'protein': 4.0,
        'sodium': 140.0,
        'sugars': 0.0,
        'vitamins': 25.0
    }
    mock_cereal_model.post_cereal = mock.MagicMock(return_value=BODY)

    response = testapp.post('/cereals',
                            data=json.dumps(BODY),
                            content_type='application/json')

    assert response.status_code == 200
    assert json.loads(response.data) == BODY


def test_put_cereal(testapp):
    NAME = 'TEST CEREAL'
    BODY = {
        'calories': 55.0,
        'carbo': 88.0,
        'fat': 0.0,
        'fiber': 16.0,
        'name': 'TEST CEREAL',
        'potass': 333.0,
        'protein': 4.0,
        'sodium': 140.0,
        'sugars': 0.0,
        'vitamins': 30.0
    }

    response = testapp.put(f'/cereals/{NAME}',
                           data=json.dumps(BODY),
                           content_type='application/json')

    assert response.status_code == 200
    assert json.loads(response.data) == BODY


def test_delete_cereal(testapp):
    NAME = 'TEST CEREAL'
    response = testapp.delete(f'/cereals/{NAME}')

    assert response.status_code == 200
    assert json.loads(response.data) == {}
