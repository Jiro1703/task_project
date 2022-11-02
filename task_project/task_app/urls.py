from django.urls import path

from .views import (
    index,
    RecordCreateView,
    delete_object,
)

urlpatterns = [
    path('', index, name='index'),
    path('record/', RecordCreateView.as_view(), name='record'),
    path('delete/<int:id_for_del>/', delete_object, name='delete')
]
