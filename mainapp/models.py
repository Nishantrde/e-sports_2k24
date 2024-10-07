from django.db import models

class BGMI_Team(models.Model):
    team_name = models.CharField(default="", max_length=100)
    player_1 = models.CharField(default="", max_length=100)
    player_2 = models.CharField(default="", max_length=100)
    player_3 = models.CharField(default="", max_length=100)
    player_4 = models.CharField(default="", max_length=100)
    ph_no = models.CharField(default="", max_length=100)
    e_mail = models.EmailField(default="")

    def __str__(self):
        return self.team_name
