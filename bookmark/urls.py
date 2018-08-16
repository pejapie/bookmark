from django.urls import path, re_path
from .views import *

app_name = 'bookmark'

urlpatterns = [
    # 함수형 뷰 : 함수 이름만 넣는다
    # 클래스형 뷰 : 클래스형 뷰.as_view()
    path('', BookmarkListView.as_view(), name='list'),
    path('write/', BookmarkCreateView.as_view(), name='write'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    # re_path(regexp, ,),
]