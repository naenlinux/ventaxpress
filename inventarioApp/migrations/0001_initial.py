# Generated by Django 4.2.3 on 2023-10-29 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mantenedoresApp', '0001_initial'),
        ('empresaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('uniMedida', models.CharField(max_length=20, null=True)),
                ('precioCompra', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('idProducto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mantenedoresApp.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('numeroComprob', models.CharField(max_length=10)),
                ('compraTotal', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('idProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedoresApp.proveedores')),
                ('idTipoComprob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresaApp.tipocomprobantes')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.compras')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedoresApp.productos')),
            ],
        ),
        migrations.CreateModel(
            name='AlmacenPrecioUM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('idAlmacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.almacen')),
                ('idUnidadMed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedoresApp.unidadmedida')),
            ],
        ),
    ]