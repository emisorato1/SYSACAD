import unittest
import os
from flask import current_app
from app import create_app
from app.models.plan import Plan

class PlanTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_plan_creation(self):
        plan= Plan()
        plan.nombre = "Plan A"
        plan.fecha_inicio = "2023-01-01"
        plan.fecha_fin = "2023-12-31"
        plan.observacion = "Observacion de prueba"
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.nombre)
        self.assertEqual(plan.nombre, "Plan A")
        self.assertEqual(plan.fecha_inicio, "2023-01-01")
        self.assertEqual(plan.fecha_fin, "2023-12-31")