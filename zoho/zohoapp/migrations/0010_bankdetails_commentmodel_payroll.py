# Generated by Django 3.2.18 on 2023-08-01 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_method_payment_made'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('joindate', models.DateField()),
                ('salary_type', models.CharField(default='Fixed', max_length=100)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('emp_number', models.IntegerField(blank=True, null=True)),
                ('designation', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('blood', models.CharField(max_length=10)),
                ('parent', models.CharField(max_length=100)),
                ('spouse_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('Phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255, null=True)),
                ('ITN', models.IntegerField(null=True)),
                ('Aadhar', models.IntegerField(null=True)),
                ('UAN', models.IntegerField(null=True)),
                ('PFN', models.IntegerField(null=True)),
                ('PRAN', models.IntegerField(null=True)),
                ('status', models.CharField(default='Active', max_length=200)),
                ('isTDS', models.CharField(max_length=200, null=True)),
                ('TDS', models.IntegerField(default=0, null=True)),
                ('attachment', models.FileField(default='', null=True, upload_to='doc/')),
            ],
        ),
        migrations.CreateModel(
            name='Commentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
        ),
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.IntegerField()),
                ('IFSC', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=100)),
                ('payroll', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
        ),
    ]
