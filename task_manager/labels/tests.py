from django.test import TransactionTestCase, Client
from task_manager.users.models import User
from django.urls import reverse

from task_manager.labels.models import Label


class LabelsTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='username',
            first_name='first_name',
            last_name='last_name',
            password='password',
        )
        self.client.login(username='username', password='password')
        self.label = Label.objects.create(
            name='name',
        )

    def test_create_label(self):
        form_data = {'name': 'old_name', }
        create_url = reverse('create_label')

        response = self.client.post(create_url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('labels'))
        self.assertEqual(Label.objects.count(), 2)

    def test_edit_label(self):
        edit_url = reverse('edit_label', args=[1])

        response = self.client.get(edit_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/update.html')

        new_form_data = {
            'name': 'new_name',
        }

        response = self.client.post(edit_url, new_form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('labels'))

        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'new_name')

    def test_delete_label(self):
        delete_url = reverse('delete_label', args=[1])

        response = self.client.get(delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/label_confirm_delete.html')

        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('labels'))

        with self.assertRaises(Label.DoesNotExist):
            self.label.refresh_from_db()
