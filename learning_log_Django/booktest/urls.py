
from django.conf.urls import include, url
from booktest import views


urlpatterns = [
   url(r'^index$',views.index),
   url(r'^create$',views.create),
   url(r'^delete(\d+)$',views.delete),
   url(r'^error$',views.error),
   url(r'^shownum(\d+)$', views.show_num),#捕获url参数,位置参数
   url(r'^shownamenum(?P<num>\d+)$', views.show_namenum),#捕获url参数,位置参数
   url(r'^login$',views.login),#显示登陆页面
   url(r'^login_check',views.login_check),
   url(r'^test_ajax$', views.ajax_test),
   url(r'^ajax_handle',views.ajax_handle),


]
