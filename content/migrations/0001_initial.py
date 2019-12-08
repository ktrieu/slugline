# Generated by Django 2.2.7 on 2019-11-30 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateField(null=True)),
                ('issue_num', models.IntegerField()),
                ('volume_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WordpressArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('author', models.CharField(blank=True, max_length=255)),
                ('content_html', models.TextField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Issue')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]