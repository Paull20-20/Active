# Generated by Django 3.2 on 2022-06-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(db_column='AlbumId', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=160)),
            ],
            options={
                'db_table': 'albums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(db_column='ArtistId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(db_column='CustomerId', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='FirstName', max_length=40)),
                ('last_name', models.CharField(db_column='LastName', max_length=20)),
                ('email', models.EmailField(db_column='Email', error_messages={'unique': 'O email cadastrado já existe, por favor, cadastre outro!'}, max_length=180, unique=True)),
                ('year', models.IntegerField(blank=True, db_column='Year', max_length=4, null=True)),
                ('company', models.CharField(blank=True, db_column='Company', max_length=80, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=70, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=40, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=40, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=40, null=True)),
                ('postal_code', models.CharField(blank=True, db_column='PostalCode', max_length=10, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', error_messages={'unique': 'O telefone cadastrado já existe, por favor, cadastre outro!'}, max_length=24, null=True, unique=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=24, null=True)),
                ('support_rep_id', models.IntegerField(blank=True, db_column='SupportRepId', null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(db_column='GenreId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(db_column='MediaTypeId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'media_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(db_column='PlaylistId', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=120, null=True)),
            ],
            options={
                'db_table': 'playlists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(db_column='TrackId', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('composer', models.CharField(blank=True, db_column='Composer', max_length=220, null=True)),
                ('milliseconds', models.IntegerField(db_column='Milliseconds')),
                ('bytes', models.IntegerField(blank=True, db_column='Bytes', null=True)),
                ('unitprice', models.DecimalField(db_column='UnitPrice', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
    ]
