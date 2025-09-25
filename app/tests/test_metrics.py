def test_metrics_shape():
    data = {"uptime": "100 hours", "users": 42}
    assert "uptime" in data and "users" in data
