from locust import HttpUser, task, between
import random

class RecochappUser(HttpUser):
    wait_time = between(1, 3)
    token = None

    def on_start(self):
        """Se ejecuta al iniciar cada usuario simulado: Registro y Login"""
        email = f"user_{random.randint(1, 100000)}@stress.com"
        password = "password123"
        
        # Intentar registrar
        self.client.post("/api/v1/users/", json={
            "email": email,
            "password": password,
            "full_name": "Stress User"
        })

        # Login
        response = self.client.post("/api/v1/login/access-token", data={
            "username": email,
            "password": password
        })
        
        if response.status_code == 200:
            self.token = response.json()["access_token"]

    @task(3)
    def view_matches(self):
        """Tarea frecuente: Ver partidos disponibles"""
        if self.token:
            self.client.get("/api/v1/matches/", headers={"Authorization": f"Bearer {self.token}"})

    @task(1)
    def create_match(self):
        """Tarea menos frecuente: Crear un partido"""
        if self.token:
            self.client.post("/api/v1/matches/", json={
                "title": "Stress Match",
                "location_name": "Load Test Arena",
                "date": "2025-01-01T10:00:00",
                "price_per_person": 10000,
                "players_total": 10
            }, headers={"Authorization": f"Bearer {self.token}"})
