from django.urls import path
from .views import AuthorView, CategoryView, PublisherView, BookView, MemberView, BorrowBooksView, PenaltyView, ReviewView 

urlpatterns =[
    path("add_post_author/", AuthorView.as_view(), name='add-post-author'),
    path("upd_del_author/<int:pk>/", AuthorView.as_view(), name ='upd-del-author'),
    path("add_post_cate/", CategoryView.as_view(), name='add-post-cate'),
    path("upd_del_cate/<int:pk>/", CategoryView.as_view(), name='add-del-author'),
    path("add_post_publisher/", PublisherView.as_view(), name='add-post-publisher'),
    path("upd_del_publisher/<int:pk>/", PublisherView.as_view(), name='add-del-publisher'),
    path("add_post_book/", BookView.as_view(), name='add-post-book'),
    path("upd_del_book/<int:pk>/", BookView.as_view(), name='add-del-book'),
    path("add_post_member/", MemberView.as_view(), name='add-post-member'),
    path("upd_del_member/<int:pk>/", MemberView.as_view(), name='add-del-member'),
    path("add_post_borrow/", BorrowBooksView.as_view(), name='add-post-borrow'),
    path("upd_del_borrow/<int:pk>/", BorrowBooksView.as_view(), name='add-del-borrow'),
    path("add_post_penalty/", PenaltyView.as_view(), name='add-post-penalty'),
    path("upd_del_penalty/<int:pk>/", PenaltyView.as_view(), name='add-del-penalty'),
    path("add_post_review/", ReviewView.as_view(), name='add-post-review'),
    path("upd_del_review/<int:pk>/", ReviewView.as_view(), name='add-del-review'),
]