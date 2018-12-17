# coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.test import TestCase

from model_mommy import mommy

from core.models import Project


class ProjectTestCase(TestCase):
    """
    Classe que testa o modelo Project
    """

    def setUp(self):
        """Método Inicial"""

        self.project = mommy.make(Project, name='Teste', url_git='http://teste.git', description='Um projeto Teste')

    def tearDown(self):
        self.project.delete()

    def test_existe_campos(self):
        """testa se existe no modelo usuario os campos corretos"""

        campos = ['name', 'url_git', 'description']

        for campo in campos:
            self.assertTrue(campo in dir(Project), 'Classe Project não tem o campo {}'.format(campo))

    def test_string_representation(self):
        self.assertEqual(str(self.project), self.project.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.project._meta.verbose_name_plural), "Projects")

    def test_existe_jogador(self):
        """testa se esta criando usuario corretamente"""

        self.assertEquals(Project.objects.count(), 1)
        self.assertEquals(Project.objects.all()[0].name, self.project.name)
