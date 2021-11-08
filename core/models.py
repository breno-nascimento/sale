from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )

    class Meta:
        managed = True
        abstract = True


class State(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    Abbreviation = models.CharField(
        db_column='tx_Abbreviation',
        null=False,
        max_length=2
    )

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.name


class City(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False
    )

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.name


class District(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    city = models.ForeignKey(
        to='City',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )

    zone = models.ForeignKey(
        to='Zone',
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
        null=False
    )

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.name


class Zone(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )

    class Meta:
        db_table = 'zone'

    def __str__(self):
        return self.name


class Branch(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )

    class Meta:
        db_table = 'branch'

    def __str__(self):
        return self.name


class Customer(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )
    marital_status = models.ForeignKey(
        to='Marital_status',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )
    income = models.DecimalField(
        db_column='nb_income',
        null=False,
        default=0.00,
        max_digits=16,
        decimal_places=2
    )
    gender = models.CharField(
        db_column='tx_gender',
        null=False,
        max_length=1
    )

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name


class Marital_status(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )

    class Meta:
        db_table = 'marital_status'

    def __str__(self):
        return self.name


class Department(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.name


class Supplier(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    legal_document = models.CharField(
        db_column='tx_legal_document',
        max_length=20,
        null=False

    )

    class Meta:
        db_table = 'supplier'

    def __str__(self):
        return self.name


class Product_group(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    commission_percentage = models.DecimalField(
        db_column='nb_commission_percentage',
        null=False,
        default=0.00,
        max_digits=5,
        decimal_places=2
    )
    gain_percentage = models.DecimalField(
        db_column='nb_gain_percentage',
        null=False,
        default=0.00,
        max_digits=5,
        decimal_places=2
    )

    class Meta:
        db_table = 'product_group'

    def __str__(self):
        return self.name


class Product(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    product_group = models.ForeignKey(
        to='Product_group',
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
        null=False
    )
    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
        null=False
    )
    cost_price = models.DecimalField(
        db_column='nb_cost_price',
        null=False,
        default=0.00,
        max_digits=16,
        decimal_places=2
    )
    sale_price = models.DecimalField(
        db_column='nb_sale_price',
        null=False,
        default=0.00,
        max_digits=16,
        decimal_places=2
    )

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    date = models.DateField(
        db_column='dt_date',
        null=False,
        auto_now_add=True
    )
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        null=False
    )
    branch = models.ForeignKey(
        to='Branch',
        on_delete=models.DO_NOTHING,
        db_column='id_branch',
        null=False
    )
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False
    )

    class Meta:
        db_table = 'sale'

    def __str__(self):
        return self.name


class Sale_item(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False
    )

    class Meta:
        db_table = 'sale_item'


class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )
    marital_status = models.ForeignKey(
        to='Marital_status',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )
    salary = models.DecimalField(
        db_column='nb_salary',
        null=False,
        default=0.00,
        max_digits=16,
        decimal_places=3
    )
    admission_date = models.DateField(
        db_column='dt_admission_date',
        null=False,
    )
    birth_date = models.DateField(
        db_column='dt_birth_date',
        null=False,
    )
    gender = models.CharField(
        db_column='tx_gender',
        null=False,
        max_length=1
    )

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name
