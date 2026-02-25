# Generated for LabActivity10 (Carousel) - included to make setup easier.
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Slide",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("caption", models.TextField(blank=True)),
                ("image_url", models.URLField(help_text="Paste a direct image URL (e.g., from picsum.photos)", max_length=500)),
                ("order", models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["order", "id"]},
        ),
    ]
