from django.urls import path
# viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引き用に名前を付ける
app_name = 'accounts'

# URLパターンを登録いるための変数
urlpatterns = [
    # サインアップページのビュー呼び出し
    # viewsモジュールのSignUpViewをインスタンス化
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # サインアップ完了ページのビュー呼び出し
    # viewsモジュールのSignUpとuccessViewをインスタンス化
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    # ログインページの表示
    # django.contrib.auth.views.LoginViewをインスタンス化
    # ログインページを表示
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    # ログアウトを実行
    # django.contrib.auth.views.logoutViewをインスタンス化
    # ログアウト
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),    
    ]