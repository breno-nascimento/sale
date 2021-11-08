from rest_framework import viewsets
from core import models, serializers


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = models.Marital_status.objects.all()
    serializer_class = serializers.MaritalStatusSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.Product_group.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.Sale_item.objects.all()
    serializer_class = serializers.SaleItemSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
