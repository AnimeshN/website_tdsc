# Generated by Django 3.0.5 on 2020-05-04 18:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('background', wagtail.core.fields.RichTextField(null=True)),
                ('CTARA_response', wagtail.core.fields.RichTextField(null=True)),
                ('proposal', wagtail.core.fields.RichTextField(null=True)),
                ('business_model', wagtail.core.fields.RichTextField(null=True)),
            ],
            options={
                'verbose_name': 'About Us Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
