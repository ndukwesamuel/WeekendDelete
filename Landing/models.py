from django.db import models

# Create your models here.


class UserDetails(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    Age = models.IntegerField()
    profile_pic = models.ImageField(upload_to='media/images/', default="images/one.jpg")
    description = models.TextField()


    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
