# Generated by Django 3.2.8 on 2021-11-08 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
            ],
            options={
                'db_table': 'branch',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('income', models.DecimalField(db_column='nb_income', decimal_places=2, default=0.0, max_digits=16)),
                ('gender', models.CharField(db_column='tx_gender', max_length=1)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('city', models.ForeignKey(db_column='id_city', on_delete=django.db.models.deletion.DO_NOTHING, to='core.city')),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('salary', models.DecimalField(db_column='nb_salary', decimal_places=3, default=0.0, max_digits=16)),
                ('admission_date', models.DateField(db_column='dt_admission_date')),
                ('birth_date', models.DateField(db_column='dt_birth_date')),
                ('gender', models.CharField(db_column='tx_gender', max_length=1)),
                ('department', models.ForeignKey(db_column='id_department', on_delete=django.db.models.deletion.DO_NOTHING, to='core.department')),
                ('district', models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Marital_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
            ],
            options={
                'db_table': 'marital_status',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('cost_price', models.DecimalField(db_column='nb_cost_price', decimal_places=2, default=0.0, max_digits=16)),
                ('sale_price', models.DecimalField(db_column='nb_sale_price', decimal_places=2, default=0.0, max_digits=16)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Product_group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('commission_percentage', models.DecimalField(db_column='nb_commission_percentage', decimal_places=2, default=0.0, max_digits=5)),
                ('gain_percentage', models.DecimalField(db_column='nb_gain_percentage', decimal_places=2, default=0.0, max_digits=5)),
            ],
            options={
                'db_table': 'product_group',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True, db_column='dt_date')),
                ('branch', models.ForeignKey(db_column='id_branch', on_delete=django.db.models.deletion.DO_NOTHING, to='core.branch')),
                ('customer', models.ForeignKey(db_column='id_customer', on_delete=django.db.models.deletion.DO_NOTHING, to='core.customer')),
                ('employee', models.ForeignKey(db_column='id_employee', on_delete=django.db.models.deletion.DO_NOTHING, to='core.employee')),
            ],
            options={
                'db_table': 'sale',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('Abbreviation', models.CharField(db_column='tx_Abbreviation', max_length=2)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('legal_document', models.CharField(db_column='tx_legal_document', max_length=20)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
            ],
            options={
                'db_table': 'zone',
            },
        ),
        migrations.CreateModel(
            name='Sale_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(db_column='id_product', on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
                ('sale', models.ForeignKey(db_column='id_sale', on_delete=django.db.models.deletion.DO_NOTHING, to='core.sale')),
            ],
            options={
                'db_table': 'sale_item',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(db_column='id_product_group', on_delete=django.db.models.deletion.DO_NOTHING, to='core.product_group'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(db_column='id_supplier', on_delete=django.db.models.deletion.DO_NOTHING, to='core.supplier'),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.ForeignKey(db_column='id_marital_status', on_delete=django.db.models.deletion.DO_NOTHING, to='core.marital_status'),
        ),
        migrations.AddField(
            model_name='district',
            name='zone',
            field=models.ForeignKey(db_column='id_zone', on_delete=django.db.models.deletion.DO_NOTHING, to='core.zone'),
        ),
        migrations.AddField(
            model_name='customer',
            name='district',
            field=models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district'),
        ),
        migrations.AddField(
            model_name='customer',
            name='marital_status',
            field=models.ForeignKey(db_column='id_marital_status', on_delete=django.db.models.deletion.DO_NOTHING, to='core.marital_status'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.DO_NOTHING, to='core.state'),
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district'),
        ),
    ]
