

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=8)),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ads.category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads/'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('member', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], default='member', max_length=9)),
                ('age', models.PositiveIntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ads.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
