# Generated by Django 4.0.4 on 2022-07-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0010_alter_comment_writer_alter_memo_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='box',
            field=models.CharField(default='멋쟁이사자', max_length=512, null=True),
        ),
    ]
