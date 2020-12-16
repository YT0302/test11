# Generated by Django 2.0.6 on 2020-12-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=80, verbose_name='图片标题')),
                ('img', models.ImageField(max_length=256, upload_to='banner', verbose_name='轮播图')),
                ('link', models.CharField(max_length=256, verbose_name='图片链接')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'edu_banner',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=80, verbose_name='导航标题')),
                ('link', models.CharField(max_length=256, verbose_name='导航链接')),
                ('is_site', models.BooleanField(default=False, verbose_name='是否是外部链接')),
                ('is_position', models.IntegerField(choices=[(1, '顶部导航'), (2, '底部导航')], default=1, verbose_name='导航栏位置')),
            ],
            options={
                'verbose_name': '导航栏',
                'verbose_name_plural': '导航栏',
                'db_table': 'edu_nav',
            },
        ),
    ]