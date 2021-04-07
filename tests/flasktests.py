from main import app


def test_get():
    with app.test_client() as c:
        rv = c.get('/request')
        assert rv.status_code == 200
