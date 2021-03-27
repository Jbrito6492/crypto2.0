from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crypto_api.views import CryptoApiView


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('crypto')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__,
                          CryptoApiView.as_view().__name__)
