from django.test import TestCase
from cards.models import Tarot, MajorArcana, MinorArcana, Corte
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.urls import reverse





class TarotModelTest(TestCase):
    def setUp(self):
        # Configurações comuns para todos os testes, como criação de arquivos de imagem fictícios
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

    def test_create_tarot(self):
        tarot = Tarot.objects.create(
            title="The Fool",
            image_tarot=self.test_image,
            text_body="<p>The Fool card represents new beginnings and adventures.</p>"
        )
        self.assertEqual(tarot.title, "The Fool")
        self.assertIn('cards/', tarot.image_tarot.name)  # Verifica se o caminho contém 'cards/'
        self.assertIn('test_image', tarot.image_tarot.name)  # Verifica se o nome contém 'test_image'
        self.assertIn("The Fool card represents new beginnings and adventures.", tarot.text_body)


    def test_str_method(self):
        tarot = Tarot.objects.create(
            title="The Magician",
            image_tarot=self.test_image,
            text_body="<p>The Magician card represents skill, logic, and intellect.</p>"
        )
        self.assertEqual(str(tarot), "The Magician")

    def test_update_tarot(self):
        tarot = Tarot.objects.create(
            title="The High Priestess",
            image_tarot=self.test_image,
            text_body="<p>The High Priestess card represents intuition and mystery.</p>"
        )
        tarot.title = "The Empress"
        tarot.save()
        updated_tarot = Tarot.objects.get(id=tarot.id)
        self.assertEqual(updated_tarot.title, "The Empress")

    def test_delete_tarot(self):
        tarot = Tarot.objects.create(
            title="The Emperor",
            image_tarot=self.test_image,
            text_body="<p>The Emperor card represents authority and control.</p>"
        )
        tarot_id = tarot.id
        tarot.delete()
        with self.assertRaises(Tarot.DoesNotExist):
            Tarot.objects.get(id=tarot_id)

class MajorArcanaModelTest(TestCase):
    def setUp(self):        
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

    def test_create_major_arcana(self):        
        major_arcana = MajorArcana.objects.create(
            name_major_arcana="0 - O Louco",
            slug="o-louco",
            description="<p>The Fool card represents new beginnings and adventures.</p>",
            image_major=self.test_image,
            key_word_major="palavra chave",

        )       
        self.assertEqual(major_arcana.name_major_arcana, "0 - O Louco")
        self.assertEqual(major_arcana.slug, "o-louco")
        self.assertEqual(major_arcana.description, "<p>The Fool card represents new beginnings and adventures.</p>")
        self.assertEqual(major_arcana.key_word_major, "palavra chave")

    def test_major_arcana_str_method(self):        
        major_arcana = MajorArcana.objects.create(
            name_major_arcana="1 - O Mago",
            slug="o-mago",
            description="<p>The Magician card represents manifestation and resourcefulness.</p>",
            image_major=self.test_image,
        )

        self.assertEqual(str(major_arcana), "1 - O Mago")

    def test_major_arcana_absolute_url(self):        
        major_arcana = MajorArcana.objects.create(
            name_major_arcana="2 - A Sacerdotisa",
            slug="a-sacerdotisa",
            description="<p>The High Priestess card represents intuition and mystery.</p>",
            image_major=self.test_image,
        )

        expected_url = reverse('cards:major_arcana_detail', kwargs={'slug': major_arcana.slug})
        self.assertEqual(major_arcana.get_absolute_url(), expected_url)

    def test_major_arcana_indexing(self):
        # Test the Meta.indexes option in the MajorArcana model
        self.assertIn('name_major_arcana', MajorArcana._meta.indexes[0].fields)

    def test_major_arcana_ordering(self):
        # Testa a opção Meta.ordering no modelo MajorArcana
        major_arcana1 = MajorArcana.objects.create(
            name_major_arcana="3 - A Imperatriz",
            slug="a-imperatriz",
            description="<p>A carta da Imperatriz representa criatividade e abundância.</p>",
            image_major=self.test_image,
        )
        major_arcana2 = MajorArcana.objects.create(
            name_major_arcana="0 - O Louco",
            slug="o-louco",
            description="<p>A carta do Louco representa novos começos e aventuras.</p>",
            image_major=self.test_image,
        )

        self.assertLess(major_arcana2.name_major_arcana, major_arcana1.name_major_arcana)

class MinorArcanaModelTest(TestCase):
    def setUp(self):
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg',
            
        )
    def test_create_minor_arcana(self):        
        minor_arcana = MinorArcana.objects.create(
            icone="Paus",
            name_minor_arcana="Às de Paus",
            slug="as-de-paus",
            description="Representa",
            image_minor=self.test_image,
            key_word_minor="palavra chave",

        )       
        self.assertEqual(minor_arcana.icone, "Paus")
        self.assertEqual(minor_arcana.name_minor_arcana, "Às de Paus")
        self.assertEqual(minor_arcana.slug, "as-de-paus")
        self.assertEqual(minor_arcana.description, "Representa")
        self.assertEqual(minor_arcana.key_word_minor, "palavra chave")

    def test_minor_arcana_str_method(self):
        minor_arcana = MinorArcana.objects.create(
            name_minor_arcana="Às de Paus",
            slug="as-de-paus",
            description="<p>Representa força</p>",
            image_minor=self.test_image,
            key_word_minor="palavra chave",

        )       
        self.assertEqual(str(minor_arcana),"Às de Paus")

    def test_minor_arcana_absolute_url(self):
        minor_arcana = MinorArcana.objects.create(            
            name_minor_arcana="Às de Paus",
            slug="as-de-paus",
            description="<p>Representa força</p>",
            image_minor=self.test_image,
            key_word_minor="palavra chave",

        )       
        expected_url = reverse('cards:enumerators_detail', kwargs={'slug': minor_arcana.slug})
        self.assertEqual(minor_arcana.get_absolute_url(), expected_url)

    def test_minor_arcana_indexing(self):        
        self.assertIn('name_minor_arcana', MinorArcana._meta.indexes[0].fields)


    def test_minor_arcana_ordering(self):        
        minor_arcana_names = [
            "Às de Paus",
            "Dois de Paus",
            "Três de Paus",
            "Quatro de Paus",
            "Cinco de Paus"
        ]
        for name in minor_arcana_names:
            MinorArcana.objects.create(
                name_minor_arcana=name,
                slug=name.lower().replace(' ', '-'),
                description=f"<p>{name}</p>",
                image_minor=self.test_image,
                key_word_minor="palavra chave",
            )

        # Chamar a função order
        ordered_minor_arcana = MinorArcana().order()

        # Verificar se a ordem está correta
        expected_order = [
            'Às de Paus',
            'Dois de Paus',
            'Três de Paus',
            'Quatro de Paus',
            'Cinco de Paus'
        ]

        result_order = [arcana.name_minor_arcana for arcana in ordered_minor_arcana]

        self.assertEqual(result_order, expected_order)

class CorteModelTest(TestCase):
    def setUp(self):
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg',            
        )
         
    def test_create_corte(self):        
        corte = Corte.objects.create(
            icone="Paus",
            name_corte="Cavaleiro de Paus",
            slug="cavaleiro-de-paus",
            description="Representa",
            image_corte=self.test_image,
            key_word_minor="palavra chave",

        )       
        self.assertEqual(corte.icone, "Paus")
        self.assertEqual(corte.name_corte, "Cavaleiro de Paus")
        self.assertEqual(corte.slug, "cavaleiro-de-paus")
        self.assertEqual(corte.description, "Representa")
        self.assertEqual(corte.key_word_minor, "palavra chave")

    def test_corte_str_method(self):
        corte = Corte.objects.create(
            icone="Paus",
            name_corte="Cavaleiro de Paus",
            slug="cavaleiro-de-paus",
            description="Representa",
            image_corte=self.test_image,
            key_word_minor="palavra chave",

        )       
   
        self.assertEqual(str(corte),"Cavaleiro de Paus")

    def test_corte_absolute_url(self):
        corte = Corte.objects.create(
            icone="Paus",
            name_corte="Cavaleiro de Paus",
            slug="cavaleiro-de-paus",
            description="Representa",
            image_corte=self.test_image,
            key_word_minor="palavra chave",

        )    

        expected_url = reverse('cards:corte_detail', kwargs={'slug': corte.slug})
        self.assertEqual(corte.get_absolute_url(), expected_url)

    def test_minor_arcana_ordering(self):        
        minor_arcana_names = [
            "Pajem de Paus",
            "Cavaleiro de Paus",
            "Rainha de Paus",
            "Rei de Paus",
        ]
        for name in minor_arcana_names:
            Corte.objects.create(
                icone="Paus",
                name_corte=name,
                slug=name.lower().replace(' ', '-'),
                description=f"<p>{name}</p>",
                image_corte=self.test_image,
                key_word_minor="palavra chave",
            )
       
        ordered_minor_arcana = Corte().order()

        
        expected_order = [
            "Pajem de Paus",
            "Cavaleiro de Paus",
            "Rainha de Paus",
            "Rei de Paus",
        ]
        result_order = [arcana.name_corte for arcana in ordered_minor_arcana]
        self.assertEqual(result_order, expected_order)