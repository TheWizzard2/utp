from django.test import TestCase

from vivero.models import Productor

# Pruebas para el modelo Productor
class ProductorModelTest(TestCase):

    def setUp(self):
        self.productor = Productor.objects.create(
            documento_identidad="123456789",
            nombre="Juan",
            apellido="Pérez",
            telefono="3001234567",
            correo="juan.perez@example.com"
        )

    def test_crear_productor(self):
        """Verifica que se puede crear un Productor correctamente"""
        self.assertEqual(self.productor.nombre, "Juan")
        self.assertEqual(self.productor.apellido, "Pérez")

    def test_documento_unico(self):
        """Verifica que el documento de identidad es único"""
        with self.assertRaises(Exception):
            Productor.objects.create(
                documento_identidad="123456789",  # Mismo documento
                nombre="Ana",
                apellido="Gómez",
                telefono="3109876543",
                correo="ana.gomez@example.com"
            )

    def test_string_representation(self):
        """Verifica la representación en string del Productor"""
        self.assertEqual(str(self.productor), "Juan Pérez")