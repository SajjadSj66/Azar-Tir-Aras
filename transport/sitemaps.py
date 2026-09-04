from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    i18n = True  # خودکار نسخه‌ی fa و en هر صفحه رو با hreflang می‌سازه
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            'index',
            'contact',
            'aboutus',
        ]

    def location(self, item):
        return reverse(item)


class ServicesSitemap(Sitemap):
    i18n = True
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return [
            'tarkibi',
            'ship',
            'truck',
            'train',
            'airplane',
            'hamle_asli',
            'international',
            'roads',
            'service_import',
            'service_export',
            'service_new',
            'service_tarkhis',
            'service_umurgomroki',
        ]

    def location(self, item):
        return reverse(item)