from django.db import models
from django.core import validators
import uuid


id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)         

validators=[validators.RegexValidator(regex='^.+en$', message='Wrong')]


class Category(models.Model):
    name = models.CharField(max_length= 60, default='Имя')
    image = models.ImageField(upload_to='static/image')
    def __str__(self):
        return self.name
    
   
TYPES = (
        ('white', 'white'),
        ('red','red'),
        ('green','green'), 
        ('yellow','yellow'),
        ('blue','blue')       

        )

class Product(models.Model):
    name = models.CharField( max_length=100, blank=False,verbose_name='Назввание') 
    img = models.ImageField(upload_to='static/image', null=True)
    category = models.ForeignKey(Category , null=True,
                              on_delete = models.CASCADE,  
                              verbose_name='Категория')    
                   
    brand = models.CharField(max_length=20 )
    #year = models.IntegerField(verbose_name='Год')
    color = models.CharField(max_length=80, verbose_name='Цвет',
    choices=TYPES, default='a')
    speed = models.IntegerField(verbose_name='Скорость')
    #mileage = models.IntegerField(verbose_name='Пробег')
    #owners = models.IntegerField(verbose_name='Владельцев')
    price = models.IntegerField(verbose_name='Цена')


    def __str__(self) -> str:
       return (
            '<p>'f'ID: {self.id}\n'
            + f'name: {self.name}\n'
            + f'category: {self.category}\n'
            + f'brand: {self.brand}\n'
            #+ f'year: {self.year}\n'
            + f'color: {self.color}\n'
            + f'speed: {self.speed}\n'
            #+ f'mileage: {self.mileage}\n'
            #+ f'owners: {self.owners}\n'
            + f'price: {self.price}\n'
                )

                

    def get_to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'category':self.category,
            'brand': self.brand,
            #'year': self.year,
            'color': self.color,
            'speed': self.speed,      
            #'mileage': self.mileage,
            #'owners': self.owners,
            'price': self.price
            }     
    
class Ordering(models.Model):
    почта = models.EmailField(max_length=100)
    номер_телефона =models.CharField(max_length=100)    
   