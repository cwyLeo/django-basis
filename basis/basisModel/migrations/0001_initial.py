# Generated by Django 4.2 on 2023-04-16 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Base",
            fields=[
                (
                    "base",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
            options={"db_table": "base", "managed": True,},
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("price", models.IntegerField(blank=True, null=True)),
                ("brand", models.CharField(blank=True, max_length=5, null=True)),
                ("size", models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={"db_table": "car", "managed": True,},
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.CharField(
                        db_column="ID", max_length=5, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                ("sex", models.CharField(blank=True, max_length=6, null=True)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("salary", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "customer", "managed": True,},
        ),
        migrations.CreateModel(
            name="Industry",
            fields=[
                (
                    "id",
                    models.CharField(
                        db_column="ID", max_length=5, primary_key=True, serialize=False
                    ),
                ),
                ("profit", models.IntegerField(blank=True, null=True)),
                ("car_in", models.IntegerField(blank=True, null=True)),
                ("car_remain", models.IntegerField(blank=True, null=True)),
                ("car_out", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "industry", "managed": True,},
        ),
        migrations.CreateModel(
            name="Sizes",
            fields=[
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=5, primary_key=True, serialize=False
                    ),
                ),
                ("weight", models.IntegerField(blank=True, null=True)),
                ("height", models.IntegerField(blank=True, null=True)),
                ("width", models.IntegerField(blank=True, null=True)),
                ("wheel_num", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "sizes", "managed": True,},
        ),
        migrations.CreateModel(
            name="Buy",
            fields=[
                (
                    "car_name",
                    models.OneToOneField(
                        db_column="car_name",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="basisModel.car",
                    ),
                ),
                ("amount", models.IntegerField(blank=True, null=True)),
                ("date", models.DateField()),
                (
                    "customer",
                    models.ForeignKey(
                        db_column="customer",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="basisModel.customer",
                    ),
                ),
                (
                    "industry",
                    models.ForeignKey(
                        db_column="industry",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="basisModel.industry",
                    ),
                ),
            ],
            options={
                "db_table": "buy",
                "managed": True,
                "unique_together": {("car_name", "customer", "industry", "date")},
            },
        ),
        migrations.CreateModel(
            name="Build",
            fields=[
                (
                    "car_name",
                    models.OneToOneField(
                        db_column="car_name",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="basisModel.car",
                    ),
                ),
                ("amount", models.IntegerField(blank=True, null=True)),
                ("date", models.DateField()),
                (
                    "industry",
                    models.ForeignKey(
                        db_column="industry",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="basisModel.industry",
                    ),
                ),
            ],
            options={
                "db_table": "build",
                "managed": True,
                "unique_together": {("car_name", "industry", "date")},
            },
        ),
    ]