# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.conf import settings
from django.test import TestCase

from model_mommy import mommy

from lario_user.models import User




class UserTestCase(TestCase):
    """
    Classe que testa o modelo Usuario
    """

    def setUp(self):
        """Método Inicial"""

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.username = 'teste'
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_existe_campos(self):
        """testa se existe no modelo usuario os campos corretos"""

        campos = ['username', 'name', 'email', 'is_staff', 'is_active', 'date_joined']

        for campo in campos:
            self.assertTrue(campo in dir(User), 'Classe User não tem o campo {}'.format(campo))


    def test_existe_jogador(self):
        """testa se esta criando usuario corretamente"""

        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(User.objects.all()[0].name, self.user.name)