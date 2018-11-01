from django.db import models

# Create your models here.

class PaperType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Paper(models.Model):
    chinese_title = models.CharField('论文标题', max_length=100)
    paper_type = models.ForeignKey(PaperType, on_delete=models.DO_NOTHING)
    author = models.CharField('作者', max_length=30)
    publisher = models.CharField('出版社', max_length=50)
    ISSN = models.CharField('ISSN', max_length=50)
    publish_year = models.CharField('年份', max_length=50)
    keywords = models.CharField('关键字', max_length=50)
    paper_url = models.CharField('原文地址', max_length=50)

    def __str__(self):
        return "<paper：%s>" % self.chinese_title