# Generated by Django 3.1.13 on 2021-07-13 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='enderecoBairro',
            field=models.CharField(max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='enderecoNum',
            field=models.IntegerField(verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='enderecoRua',
            field=models.CharField(max_length=250, verbose_name='Endereço'),
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('totalPedido', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.produto')),
            ],
        ),
    ]
