from django.db.models import Sum, Count
from django.test import TestCase

# Create your tests here.
from app1.models import Car
from core.models import Brand


class CarTest(TestCase):

    def setUp(self) -> None:
        self.new_brand = Brand.objects.create(name='New brand', country='Iran')
        self.new_brand2 = Brand.objects.create(name='New brand2', country='Germany')
        Car.objects.create(brand=self.new_brand, acceleration=10, color='RED')
        Car.objects.create(brand=self.new_brand, acceleration=11, color='BLU')
        Car.objects.create(brand=self.new_brand, acceleration=12, color='BLU')
        Car.objects.create(brand=self.new_brand, acceleration=13, color='GRN')
        Car.objects.create(brand=self.new_brand2, acceleration=13, color='GRN')
        Car.objects.create(brand=self.new_brand2, acceleration=14, color='GRN')
        Car.objects.create(brand=self.new_brand2, acceleration=15, color='GRN')

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

    def test_ordering(self):
        print(*Car.objects.order_by('id'), sep='\n')

    def test_is_delete(self):
        print('Before delete last:', len(Car.objects.filter(is_delete=False)))
        Car.objects.last().delete()
        print('After delete last:', len(Car.objects.filter(is_delete=False)))


class CarSerializerTest(TestCase):

    def setUp(self) -> None:
        brand = Brand.objects.create(name='Test', country='Test')
        Car.objects.create(brand=brand, acceleration=10, color='BLU')
        Car.objects.create(brand=brand, acceleration=11, color='BLK')
        Car.objects.create(brand=brand, acceleration=12, color='RED')

    def test1(self):
        # Serialize: (Model Instance -> JSON)
        from app1.serializers import CarSerializer
        car_instance = Car.objects.first()
        car_serializer = CarSerializer(instance=car_instance)

        print(car_serializer.data)

    def test2(self):
        # Serialize (Many): (Model Instance -> JSON)
        from app1.serializers import CarSerializer
        car_serializer = CarSerializer(instance=Car.objects.all(), many=True)

        print(car_serializer.data)

    def test3(self):
        # DeSerialize: (JSON -> Model instance)
        from app1.serializers import CarSerializer
        car_info = {  # Valid data!
            'brand': 1,
            'color': 'BLU',
            'acceleration': 30
        }
        car_serializer = CarSerializer(data=car_info)
        if car_serializer.is_valid():
            car = car_serializer.save()
            print(car)
        else:
            print(car_serializer.errors)

    def test4_invalid(self):
        # DeSerialize: (JSON -> Model instance)
        from app1.serializers import CarSerializer
        car_info = {  # Valid data!
            'brand': 5,
            'color': 'BLU',
        }
        car_serializer = CarSerializer(data=car_info)
        if car_serializer.is_valid():
            car = car_serializer.save()
            print('Instance:', car)
        else:
            print('Errors:', car_serializer.errors)



