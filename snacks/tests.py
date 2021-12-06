from django.test import TestCase
from django.urls import reverse


class SnackTest(TestCase):

    def test_snack_list_page_status(self):
        url = reverse('snackList')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)

    def test_snack_list_used_template(self):
        url = reverse('snackList')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'snack_list.html')
        self.assertTemplateUsed(res,'_base.html')