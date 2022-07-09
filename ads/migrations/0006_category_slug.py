
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
    ]
