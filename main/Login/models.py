from django.db import models

# Create your models here.
# Create your models here.
class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')

    class Meta:
        db_table = 'avatar'

class Userinfo(models.Model):
    username = models.CharField(null=True,blank=True,max_length=16,verbose_name="用户姓名")
    password=models.CharField(null=True,blank=True,max_length=16,verbose_name="密码")
    nickname = models.CharField(null=True,blank=True,max_length=16,verbose_name="用户微信名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(null=True, blank=True, max_length=6, choices=(("1", u"男"), ("0", "女")), default="1",
                              verbose_name="性别")
    age = models.IntegerField(null=True,blank=True,verbose_name="年龄")
    school_number = models.CharField(null=True,blank=True,unique=True,max_length=30,verbose_name="学号")
    human_height = models.IntegerField(null=True,blank=True,verbose_name="身高")
    school = models.CharField(null=True,blank=True,max_length=60,default="上海财经大学",verbose_name="学校")
    home = models.CharField(null=True,blank=True,max_length=50,verbose_name="家乡")
    profession = models.CharField(null=True,blank=True,max_length=60,verbose_name="专业")
    location_house = models.CharField(null=True,blank=True,max_length=100,verbose_name="宿舍楼")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话", unique=True)
    unionId = models.CharField(null=True, blank=True, max_length=50, verbose_name="unionId")
    open_id = models.CharField(null=True, blank=True, max_length=50, verbose_name="openid")
    session_key = models.CharField(null=True, blank=True, max_length=50, verbose_name="session_key")
    info = models.CharField(null=True, blank=True, max_length=50, verbose_name="个人简介")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    collect_time = models.IntegerField(default=0)
    Avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='User_avatar'
    )
    image = models.TextField(null=True,blank=True,verbose_name="图片")
    # user_image = models.TextField(null=True,blank=True,verbose_name="用户上传图片")
    # user_interest = models.TextField(null=True,blank=True,verbose_name="用户兴趣")
    # user_daily = models.TextField(null=True,blank=True,verbose_name="用户日常")
    is_showinfo = models.BooleanField(default=True,verbose_name="是否显示资料")
    wx_location = models.CharField(null=True,blank=True,max_length=100,verbose_name="微信位置")


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username