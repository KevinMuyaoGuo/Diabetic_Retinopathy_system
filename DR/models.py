# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.html import format_html
import os

from django.utils.safestring import mark_safe


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Case(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='病例号')
    case_name = models.CharField(max_length=45, verbose_name='病例名')
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    patient_name = models.CharField(max_length=45, verbose_name='病人姓名')

    class Meta:
        managed = False
        db_table = 'case'
        verbose_name_plural = '病例管理'


class Diagnosis(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='诊断号')
    photo_id = models.IntegerField(verbose_name='照片号')
    photo_name = models.CharField(max_length=60, verbose_name='照片名')
    result = models.CharField(max_length=45, verbose_name='诊断结果')
    case = models.ForeignKey(Case, models.DO_NOTHING)
    photo = models.ImageField(upload_to='')

    def image_data(self):
        return mark_safe('<img src="/media/%s" width="200" height="200" />' % self.photo)

    image_data.short_description = '照片'

    def __str__(self):
        return '%s' % self.id

    class Meta:
        managed = False
        db_table = 'diagnosis'
        verbose_name_plural = '诊断信息'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Patient(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='身份证号')
    name = models.CharField(max_length=45, verbose_name='姓名')
    phone = models.CharField(max_length=15, verbose_name='手机号')
    sex = models.CharField(max_length=8, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'patient'
        verbose_name_plural = '病人管理'


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename)  # 系统路径分隔符差异，增强代码重用性


class Photo(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='照片号')
    photo_name = models.CharField(max_length=60, verbose_name='照片名')
    photo_diagnosis = models.CharField(max_length=45, blank=True, null=True,
                                       verbose_name='诊断标签')
    photo = models.ImageField(upload_to='')

    def image_data(self):
        # return format_html(
        #     # '{% for i in img %} <img src="{{ MEDIA_URL }}{{ i.image }}" { % endfor %} width="100px"/>',
        #     # """<div οnclick='$(".my_set_image_img").hide();$(this).next().show();'><img src='{}' style='width:50px;height:50px;' >放大</div><div class='my_set_image_img' οnclick="$('.my_set_image_img').hide()" style="z-index:9999;position:fixed; left: 100px; top:100px;display:none;"><img src='{}' style='width:500px; height:500px;'></div>""",
        #     obj.photo.url, obj.photo.url
        # )
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.photo)

    image_data.short_description = '照片'

    class Meta:
        managed = False
        db_table = 'photo'
        verbose_name_plural = '照片管理'

# class Image(models.Model):
#     media = models.ImageField(u'图片', upload_to='media/')
#
#     def image_data(self):
#         return format_html(
#             '<img src="{}" width="100px"/>',
#             self.media.url,
#         )
#
#     image_data.short_description = u'图片'
