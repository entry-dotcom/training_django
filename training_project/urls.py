from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('muscle_app.urls')),   #(App_Folder)はご自身で作成したアプリケーションフォルダがあればその名前を記載
]
