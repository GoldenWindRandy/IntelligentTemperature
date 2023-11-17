from django.db import models
from Login.models import *
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

class ProductImage(models.Model):
    content = models.ImageField(upload_to='productImage/%Y%m%d')

    class Meta:
        db_table = 'productImage'

class Category(models.Model):
    # 作品分类
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名", unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="类别描述", help_text="类别描述")  # to remove
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    class Meta:
        verbose_name = "作品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPE = (
        ('0',"sale"),
        ('1',"rent")
    )
    owner = models.ForeignKey(Userinfo,on_delete=models.CASCADE,related_name="myproduct")
    category = models.ForeignKey(Category,verbose_name="作品类别",on_delete=models.CASCADE,related_name="product_category")
    product_name = models.CharField(max_length=200,verbose_name="作品名称")
    product_type = models.CharField(default='sale', choices=PRODUCT_TYPE, max_length=30, verbose_name="作品类型")
    remark = models.TextField(null=True, blank=True, verbose_name="作品详情")
    delete_flag = models.BooleanField(default=False)
    browsing_volume = models.IntegerField(default=0, verbose_name='浏览次数')
    collecit_volume = models.IntegerField(default=0,verbose_name="collect_time")
    add_like = models.IntegerField(default=0,verbose_name="add_like time")
    product_image = models.ForeignKey(
        ProductImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='ProductImage'
    )
    owner_location = models.CharField(max_length=100,null=True, blank=True, verbose_name="作品所有者位置")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "作品"
        verbose_name_plural = verbose_name