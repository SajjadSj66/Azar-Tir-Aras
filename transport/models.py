from django.db import models

# Create your models here.
class ContactUs(models.Model):
    full_name = models.CharField(max_length=250, verbose_name="نام و نام‌خانوادگی")
    email = models.EmailField(max_length=250, verbose_name="ایمیل")
    phone = models.CharField(max_length=15, verbose_name="شماره موبایل")
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس ها"

    def __str__(self):
        return self.full_name
    
