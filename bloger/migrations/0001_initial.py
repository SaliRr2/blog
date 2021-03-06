# Generated by Django 2.1.5 on 2019-02-17 13:30

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
            name='Anothergame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anothergame_title', models.CharField(max_length=30, verbose_name='Заголовок статьи')),
                ('anothergame_date', models.DateTimeField(auto_now=True)),
                ('anothergame_body', models.TextField(verbose_name='Описание программы')),
                ('anothergame_cheatlink', models.CharField(max_length=50, verbose_name='Ссылка на чит')),
                ('anothergame_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments_anothergame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='комментарий')),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('comment_anothergame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.Anothergame')),
                ('comment_anothergame_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments_anothergame',
            },
        ),
        migrations.CreateModel(
            name='Comments_csgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='комментарий')),
                ('comment_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comments_csgo',
            },
        ),
        migrations.CreateModel(
            name='Comments_fortnite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='комментарий')),
                ('comment_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comments_fortnite',
            },
        ),
        migrations.CreateModel(
            name='Comments_rust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='комментарий')),
                ('comment_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comments_rust',
            },
        ),
        migrations.CreateModel(
            name='Comments_soft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='комментарий')),
                ('comment_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comments_soft',
            },
        ),
        migrations.CreateModel(
            name='Comments_warface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='комментарий')),
                ('comment_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comments_warface',
            },
        ),
        migrations.CreateModel(
            name='Csgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csgo_title', models.CharField(max_length=30, verbose_name='Заголовок статьи')),
                ('csgo_date', models.DateTimeField(auto_now=True)),
                ('csgo_body', models.TextField(verbose_name='Описание программы')),
                ('csgo_cheatlink', models.CharField(max_length=50, verbose_name='Ссылка на чит')),
                ('csgo_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fortnite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fortnite_title', models.CharField(max_length=30, verbose_name='Заголовок статьи')),
                ('fortnite_date', models.DateTimeField(auto_now=True)),
                ('fortnite_body', models.TextField(verbose_name='Описание программы')),
                ('fortnite_cheatlink', models.CharField(max_length=50, verbose_name='Ссылка на чит')),
                ('fortnite_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rust_title', models.CharField(max_length=30, verbose_name='Заголовок статьи')),
                ('rust_date', models.DateTimeField(auto_now=True)),
                ('rust_body', models.TextField(verbose_name='Описание программы')),
                ('rust_cheatlink', models.CharField(max_length=50, verbose_name='Ссылка на чит')),
                ('rust_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_title', models.CharField(max_length=30, verbose_name='Заголовок статьи')),
                ('soft_date', models.DateTimeField(auto_now=True)),
                ('soft_body', models.TextField(verbose_name='Описание программы')),
                ('soft_cheatlink', models.CharField(max_length=50, verbose_name='Ссылка на чит')),
                ('soft_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warface_title', models.CharField(max_length=30, verbose_name='Заголовок статьи')),
                ('warface_date', models.DateTimeField(auto_now=True)),
                ('warface_body', models.TextField(verbose_name='Описание программы')),
                ('warface_cheatlink', models.CharField(max_length=50, verbose_name='Ссылка на чит')),
                ('warface_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments_warface',
            name='comment_warface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.Warface'),
        ),
        migrations.AddField(
            model_name='comments_warface',
            name='comment_warface_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments_soft',
            name='comment_soft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.Soft'),
        ),
        migrations.AddField(
            model_name='comments_soft',
            name='comment_soft_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments_rust',
            name='comment_rust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.Rust'),
        ),
        migrations.AddField(
            model_name='comments_rust',
            name='comment_rust_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments_fortnite',
            name='comment_fortnite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.Fortnite'),
        ),
        migrations.AddField(
            model_name='comments_fortnite',
            name='comment_fortnite_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments_csgo',
            name='comment_csgo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.Csgo'),
        ),
        migrations.AddField(
            model_name='comments_csgo',
            name='comment_csgo_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
