from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Holder5, Inner5


@override_settings(ROOT_URLCONF='admin_media_regression.urls')
class ModelAdminMediaTests(TestCase):

    def test_inline_media_only_inline(self):
        holder = Holder5(dummy=13)
        holder.save()
        Inner5(dummy=42, holder=holder).save()
        superuser = User.objects.create_superuser(
            username='super', email='super@example.com', password='secret')
        self.client.force_login(superuser)
        change_url = reverse('admin:admin_media_regression_holder5_change', args=(holder.id,))
        response = self.client.get(change_url)
        js = response.context['media']._js
        self.assertIn('test.js', js)
        self.assertIn('admin/js/vendor/jquery/jquery.min.js', js)
        self.assertIn('admin/js/inlines.min.js', js)
        self.assertLess(
            js.index('admin/js/vendor/jquery/jquery.min.js'),
            js.index('admin/js/inlines.min.js'),
        )
