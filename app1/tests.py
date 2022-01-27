from django.db.models import Sum, Count
from django.test import TestCase

# Create your tests here.
from app1.models import Car
from core.models import Brand


class CarTest(TestCase):

    def setUp(self) -> None:
        self.new_brand = Brand.objects.create(name='New brand', country='Iran')
        Car.objects.create(brand=self.new_brand, acceleration=10, color='RED')
        Car.objects.create(brand=self.new_brand, acceleration=11, color='BLU')
        Car.objects.create(brand=self.new_brand, acceleration=12, color='BLU')
        Car.objects.create(brand=self.new_brand, acceleration=13, color='GRN')

    def test1_create_car(self):
        new_car = Car.objects.create(brand=self.new_brand, acceleration=10, color='RED')
        print('New car:', new_car)

    def test2_initsave_car(self):
        new_car = Car(brand=self.new_brand, acceleration=10, color='RED')
        new_car.save()
        print('New car:', new_car)

    def test3_get_car(self):
        print(Car.objects.get(color='BLU', acceleration=12))
        print(Car.objects.get(color='BLU'))  # ERROR!!
        print(Car.objects.get(color='AKBAR'))  # ERROR!!

    def test4_filter_car(self):
        print(Car.objects.filter(acceleration=12))
        print(Car.objects.filter(color='BLU'))

        print(Car.objects.filter(color__in=['BLU', 'RED']))
        print(Car.objects.filter(brand__country__startswith='I'))

        qs = Car.objects.all() \
            .order_by('-id') \
            .exclude(acceleration=10) \
            .last()

        print(Car.objects.all()[::2])

    def test_aggregate(self):
        from django.db.models import Avg, Sum
        print(Car.objects.aggregate(
            idsum=Sum('id')
        ))
