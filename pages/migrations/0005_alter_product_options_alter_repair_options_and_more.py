# Generated by Django 4.2.2 on 2023-07-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_repair_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='repair',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('G', 'Bad'), ('B', 'Good')], default='G', max_length=2, null=True),
        ),
    ]
