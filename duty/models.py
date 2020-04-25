from django.db import models

# Create your models here.
class duty(models.Model):
    Duty_statu =[
        ("P","pasif"),
        ("A","aktif")
    ]
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length=20,verbose_name="başlık")
    #content = models.CharField(max_length=30,verbose_name="açıklama", null=True, blank=True)
    statu = models.CharField(choices=Duty_statu, default="A", max_length=1)
    created_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']