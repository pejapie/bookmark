from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 랜더링할 템플릿 파일이 지정이 되어있습니다.
    # bookmark/bookmark_list.html

class BookmarkDetailView(DetailView):
    model = Bookmark

from django.urls import reverse_lazy
class BookmarkCreateView(CreateView):
    model = Bookmark
    # 입력화면에 출력된 form tag를 자동으로 만들어줌. 입력하지 않으면 default 값으로 _form을 입력함.
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name', 'url']
    # 성공 페이지를 보여줘야 함. 없으면 get_absolute_url 자동 호출함
    success_url = reverse_lazy('list')


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name_suffix = '_update'
    fields = ['site_name', 'url']

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')