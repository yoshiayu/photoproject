from django.db import models
# accountsアプリのomdelsモジュールからCostomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
         Returns(str):カテゴリ名
         '''
        return self.title

class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    # CustomUserモデル(user_id)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係になる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データも全て削除する
        on_delete=models.CASCADE
        )
    # Categoryモデル（title）とPhotoPostモデルを
    # 1対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係になる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    
    comment = models.TextField(
        verbose_name='コメント',
        )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'photos',  # MEDIA_ROOT以下のphotosにファイルを保存        
        )
     # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to = 'photos',  # MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,            # フィールド値の設定は必須出ない
        null=True              # データーベースにnullが保存されることを許容
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True  # 日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
    
    
    
    
    
    
    
    
