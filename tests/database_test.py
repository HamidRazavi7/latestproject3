def test_upload_csvfile(client):
    file = "./uploads/music_copy.csv"
    data = { 'file': (open(file, 'rb'), file) }

    # I should copy the logging code here once login test works.
    res = client.get("/login")
    assert res.status_code == 200
    # response = client.post('/songs/upload', data=data)
