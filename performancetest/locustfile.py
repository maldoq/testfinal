from locust import HttpUser, task, between

class DjangoPerformanceTest(HttpUser):
    wait_time = between(1, 3)  # Simulate a user waiting between 1 and 3 seconds between tasks

    @task
    def homepage_test(self):
        """Test the homepage (timeline view)."""
        self.client.get("/")

    @task
    def detail_view_test(self):
        """Test the detail view with a sample slug."""
        # Replace the slug below with a valid slug from your app
        slug = "test-publication-123456"
        self.client.get(f"/detail/{slug}/")

    @task
    def cours_view_test(self):
        """Test the cours view."""
        self.client.get("/cours/")

    @task
    def video_view_test(self):
        """Test the video view."""
        self.client.get("/video/")

    @task
    def is_commentaire_test(self):
        """Simulate submitting a comment."""
        self.client.post("/is_commentaire/", data={
            'id': 1,  # Replace with a valid publication ID
            'nom': 'Test User',
            'email': 'testuser@example.com',
            'commentaire': 'This is a test comment.'
        })

    @task
    def is_reponsescommentaires_test(self):
        """Simulate submitting a reply to a comment."""
        self.client.post("/is_reponsescommentaires/", data={
            'id_commentaire': 1,  # Replace with a valid comment ID
            'name': 'Responder',
            'mail': 'responder@example.com',
            'reponsecommentaires': 'Test reply.'
        })
