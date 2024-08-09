from django.db import models

EQUIPMENT_CHOICES = (
    ('1', 'Barra'),
    ('2', 'Haltere'),
    ('3', 'Kettlebell'),
    ('4', 'Máquina'),
    ('5', 'Polia'),
    ('6', 'Peso Corporal'),
    ('7', 'Banco'),
)

MUSCLES_CHOICES = (
    ('1', 'Quadríceps'),
    ('2', 'Posterior'),
    ('3', 'Glúteos'),
    ('4', 'Panturrilha'),
    ('5', 'Bíceps'),
    ('6', 'Tríceps'),
    ('7', 'Peito'),
    ('8', 'Costas'),
    ('9', 'Ombros'),
    ('10', 'Abdômen'),
)

class Equipamento(models.Model):
    name = models.CharField(max_length=20, choices=EQUIPMENT_CHOICES)

    def __str__(self):
        return self.get_name_display()

class Musculo(models.Model):
    name = models.CharField(max_length=20, choices=MUSCLES_CHOICES)

    def __str__(self):
        return self.get_name_display()

class Exercicio(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    gif_url = models.URLField(max_length=200)
    equipment = models.ForeignKey("Equipamento", on_delete=models.CASCADE)
    musculo = models.ManyToManyField(Musculo, related_name='musculos')

    def __str__(self):
        return self.name

