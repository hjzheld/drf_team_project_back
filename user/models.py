from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, profile, mbti, blog, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not nickname:
            raise ValueError('Users must have an email nickname')

        user = self.model(
            email=self.normalize_email(email),
            nickname = nickname,
            mbti = mbti,
            blog = blog,
            profile = profile
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, profile, mbti, blog, password=None):
        user = self.create_user(
            email,
            nickname,
            mbti,
            blog,
            profile,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers', blank=True)
    last_login = models.DateTimeField(
        auto_now=True, blank=True, null=True, verbose_name='last login')
    nickname = models.CharField(max_length=100, unique=True)
    mbti = models.CharField(max_length=100, null=True, blank=True)
    blog = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ImageField(blank=True, upload_to='%Y/%m/')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    tag_ids = models.ManyToManyField('tag.Tag', related_name='user_tag', blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'profile', 'mbti', 'blog']


    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin