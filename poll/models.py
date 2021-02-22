from django.db import models

class Option(models.Model):
    content = models.CharField(
        verbose_name="내용",
        max_length=1000,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name="생성된 날짜",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="수정된 날짜",
        auto_now=True
    )


class Poll(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('t', 'trash')
    )
    title = models.TextField(
        verbose_name="제목",
        max_length=500,
        null=False,
        default="투표"
    )
    options = models.ManyToManyField(
        Option,
        verbose_name="항목",
    )
    status = models.CharField(
        verbose_name='투표 공개 상태',
        max_length=2,
        default='p',
        null=False,
        choices=STATUS_CHOICES
    )
    created_at = models.DateTimeField(
        verbose_name="생성된 날짜",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="수정된 날짜",
        auto_now=True
    )

class Vote(models.Model):
    name = models.CharField(
        verbose_name="이름",
        max_length=10,
        null=True,
    )
    poll = models.ForeignKey(
        Poll,
        verbose_name="참가한 투표",
        on_delete=models.DO_NOTHING,
    )
    option = models.ForeignKey(
        Option,
        verbose_name="선택한 항목",
        on_delete=models.DO_NOTHING,
    )
    created_at = models.DateTimeField(
        verbose_name="생성된 날짜",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="수정된 날짜",
        auto_now=True
    )
