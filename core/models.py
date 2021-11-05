from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=64
    )

    class Meta:
        managed = True
        abstract = True


class State(ModelBase):
    Abbreviation = models.CharField(
        db_column='tx_Abbreviation',
        null=False,
        max_length=2
    )

    class Meta:
        db_table = 'state'


class City(ModelBase):
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False
    )

    class Meta:
        db_table = 'city'


class District(ModelBase):
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


class Zone(ModelBase):
    class Meta:
        db_table = 'zone'
