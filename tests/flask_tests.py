from main import app


def test_index():
    with app.test_client() as c:
        rv = c.get("/")
        assert rv.data == b'Hello'
        assert rv.status_code == 200


def test_post_route_success():
    data = {
        'currentURL': 'https://docs.python.org/3.9/'
    }
    with app.test_client() as c:
        rv = c.post("/request", json=data)
        assert rv.content_type == 'application/json'
        assert rv.status_code == 200


def test_post_route_server_error():
    data = {
        'testingURL': 'https://docs.python.org/3.9/'
    }
    with app.test_client() as c:
        rv = c.post("/request", json=data)
        assert rv.status_code == 500


def test_post_route_data():
    data = {
        'currentURL': 'https://docs.python.org/3.9/'
    }
    with app.test_client() as c:
        rv = c.post("/request", json=data)
        json_data = rv.get_json()
        assert 'currentURL' in json_data
        assert rv.status_code == 200


def test_get_route():
    with app.test_client() as c:
        rv = c.get("/request")
        assert rv.status_code == 405
