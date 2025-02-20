from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(
        verbose_name="Содержимое", help_text="Чем хотите поделиться?"
    )
    preview = models.ImageField(
        upload_to="catalog/img",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью (необязательно)",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    view_counter = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
