import os
import tempfile
import unittest
import app as skillpath_app

class SkillPathTests(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)
        self.temp_db.close()
        skillpath_app.DB_PATH = skillpath_app.Path(self.temp_db.name)
        skillpath_app.app.config["TESTING"] = True
        self.client = skillpath_app.app.test_client()
        skillpath_app.init_db()

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except OSError:
            pass

    def test_dashboard_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"SkillPath", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "ok")

    def test_profile_save(self):
        response = self.client.post("/save-profile", data={
            "student_name": "Test Student",
            "year": "3",
            "goal": "Data Science"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Student", response.data)
        self.assertIn(b"3rd year roadmap", response.data)

if __name__ == "__main__":
    unittest.main()
