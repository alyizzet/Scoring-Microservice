@pytest.fixture
def app():
  db_fd, db_path = tempfile.mkstemp()
  app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
  })
  with app.app_context():
        init_db()
  yield app
  os.close(db_fd)
  os.unlink(db_path)