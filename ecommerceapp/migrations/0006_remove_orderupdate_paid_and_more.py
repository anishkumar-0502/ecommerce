# Generated by Django 4.2.3 on 2023-07-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0005_orderupdate_razorpay_signature"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderupdate",
            name="paid",
        ),
        migrations.RemoveField(
            model_name="orderupdate",
            name="razorpay_payment_id",
        ),
        migrations.RemoveField(
            model_name="orderupdate",
            name="razorpay_signature",
        ),
        migrations.AddField(
            model_name="orders",
            name="paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="orders",
            name="razorpay_payment_id",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="orders",
            name="razorpay_signature",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]