# Generated by Django 4.2.7 on 2023-11-10 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_alter_order_client_id_alter_order_employee_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='order_id',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='orders.order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
