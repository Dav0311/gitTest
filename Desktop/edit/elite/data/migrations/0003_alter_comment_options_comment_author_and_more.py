# Generated by Django 4.0.5 on 2023-05-14 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_book_payment_alter_book_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=300),
        ),
    ]
