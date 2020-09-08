from django.db import models

# Create your models here.
class Producto(models.Model):
    COLOR_CHOICES = (
        
        ('0', 'BLACK'),
        ('1', 'BROWN'),
        ('2', 'BLUE'),
        ('3', 'GREEN'),
        ('4', 'ORANGE'),
        ('5', 'GOLD'),
        ('6', 'SILVER')
    )
    SIZE_CHOICES = (
        ('0', '31'),
        ('1', '32'),
        ('2', '33'),
        ('3', '34'),
        ('4', '35'),
        ('5', '36'),
        ('6', '37'),
        ('7', '38'),
        ('8', '39'),
        ('9', '40'),
        ('10', '41'),
        ('11', '42'),
        ('12', '43'),
        ('13', '44'),
        ('14', '45')
        
    )
    nombre  = models.CharField('nombre', max_length=50)
    description = models.TextField('Descripcion producto',blank=True)
    man = models.BooleanField('Para Hombre', default=True)
    woman = models.BooleanField('Para Mujer', default=True)
    marca = models.CharField('marca', max_length=50)
    color = models.CharField("color", max_length=50, choices=COLOR_CHOICES)
    talla = models.CharField("talla", max_length=50, choices=SIZE_CHOICES)
    precio = models.DecimalField('Precio de Venta',max_digits=10, decimal_places=2)
    avatar = models.ImageField("foto", upload_to='producto',blank=True, null=True)
    stock = models.PositiveIntegerField('Stock', default=0)
    
    
    class Meta:
        ordering =['marca']