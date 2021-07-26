# Generated by Django 3.2.4 on 2021-07-21 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('objective', models.TextField(max_length=200)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='template', to='resume.choosetemplate')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_link', models.CharField(max_length=100)),
                ('technology', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('responsibilities', models.TextField(max_length=1000)),
                ('logo', models.ImageField(upload_to='images/logos/')),
                ('date', models.DateField()),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=300)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeUserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(blank=True, max_length=255)),
                ('competency', models.IntegerField(blank=True, choices=[('', '-----'), (1, 'Below Average'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], null=True)),
                ('resume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'verbose_name_plural': 'Experience',
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=100)),
                ('year_of_passing', models.CharField(max_length=100)),
                ('percentage_or_grade', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=300)),
                ('date_obtained', models.DateField(blank=True, null=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievements', models.CharField(max_length=300)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
    ]