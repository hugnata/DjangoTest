from django.test import TestCase, Client


# Create your tests here.
from django.urls import reverse


class EmployeCreateTest(TestCase):

    def test_employe_usual(self):
        client = Client()
        response = client.post('/employe/create',data={
            'nom':'lambda',
            'entreprise':1
        })
        self.assertEqual(response.status_code,200)


    def test_employe_no_name(self):
        client = Client()
        response = client.post('/employe/create', data={
            'entreprise': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Veuillez remplir tout les champs !")

class EmployeListTest(TestCase):

    def test_no_employe(self):
        client = Client()
        response = client.get('/employe')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Aucun employé')