from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.

# ユーザー作成モデル
class CustomUserManager(UserManager):
    # ユーザーマネージャー（データベースアクセスを行う際のユーザー管理を行なうツール）
    use_in_migrations: bool = True
    
    # UserManagerのメソッドをオーバーライド
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError("The given username must be set")
        
        # 変数「user」に「username」「email」をセット
        user = self.model(username=username, email=email, **extra_fields)
        # set_password()・・・引数の文字列をハッシュ化させる
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    