from django.urls import path
from StoreCommerce.views import (home, fullView,
                                 profile,header,footer,setting,
                                 ProdOrderForm,reviewProduct,commentProduct,view_Product_admin,
                                 adminBoard,delete_place_byAdmin,update_place_byAdmin,messageAdmin,
                                 mobileShow, delete_Mobile_byAdmin, mobile_Product_admin, update_Mobile_byAdmin,
                                 computer_Product_admin, computerShow, delete_Computer_byAdmin, update_Computer_byAdmin,
                                 shoesShow, shoes_Product_admin, delete_Shoes_byAdmin, update_Shoes_byAdmin,
                                 clothShow, cloth_Product_admin, delete_Cloth_byAdmin, update_Cloth_byAdmin,
                                 watchShow, watch_Product_admin, update_Watch_byAdmin, delete_Watch_byAdmin,
                                 tvShow, tv_Product_admin, delete_Tv_byAdmin, update_Tv_byAdmin,
                                 accessShow, access_Product_admin, delete_Access_byAdmin, update_Access_byAdmin,
                                 view_UserByAdmin, add_UserByAdmin, delete_User_byAdmin, update_User_byAdmin,
                                 wishlist, search,
                                 )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home.as_view(), name='home'),
    path('fullView/<str:ProductID>/', fullView.as_view(), name='fullView'),

    path('wishlist/', wishlist.as_view(), name='wishlist'),
    path('search/', search.as_view(), name='search'),

    path('profile/', profile.as_view(), name='profile'),
    path('setting/', setting.as_view(), name='setting'),
    path('header/', header.as_view(), name='header'),
    path('footer/', footer.as_view(), name='footer'),

    path('view_Product_admin/', view_Product_admin.as_view(), name='view_Product_admin'),
    path('ProdOrderForm/', ProdOrderForm.as_view(), name='ProdOrderForm'),
    path('commentProduct/', commentProduct.as_view(), name='commentProduct'),
    path('reviewProduct/', reviewProduct.as_view(), name='reviewProduct'),

    path('messageAdmin/<str:email>/', messageAdmin.as_view(), name='messageAdmin'),
    path('delete_place_byAdmin/', delete_place_byAdmin.as_view(), name='delete_place_byAdmin'),
    path('update_place_byAdmin/', update_place_byAdmin.as_view(), name='update_place_byAdmin'),
    path('adminBoard/', adminBoard.as_view(), name='adminBoard'),

    path('add_UserByAdmin/', add_UserByAdmin.as_view(), name='add_UserByAdmin'),
    path('view_UserByAdmin/', view_UserByAdmin.as_view(), name='view_UserByAdmin'),
    path('delete_User_byAdmin/', delete_User_byAdmin.as_view(), name='delete_User_byAdmin'),
    path('update_User_byAdmin/<str:email>/', update_User_byAdmin.as_view(), name='update_User_byAdmin'),

    path('mobileShow/', mobileShow.as_view(), name='mobileShow'),
    path('delete_Mobile_byAdmin/', delete_Mobile_byAdmin.as_view(), name='delete_Mobile_byAdmin'),
    path('mobile_Product_admin/', mobile_Product_admin.as_view(), name='mobile_Product_admin'),
    path('update_Mobile_byAdmin/<str:ProdID>/', update_Mobile_byAdmin.as_view(), name='update_Mobile_byAdmin'),

    path('computer_Product_admin/', computer_Product_admin.as_view(), name='computer_Product_admin'),
    path('computerShow/', computerShow.as_view(), name='computerShow'),
    path('delete_Computer_byAdmin/', delete_Computer_byAdmin.as_view(), name='delete_Computer_byAdmin'),
    path('update_Computer_byAdmin/<str:ProdID>/', update_Computer_byAdmin.as_view(), name='update_Computer_byAdmin'),

    path('shoes_Product_admin/', shoes_Product_admin.as_view(), name='shoes_Product_admin'),
    path('shoesShow/', shoesShow.as_view(), name='shoesShow'),
    path('delete_Shoes_byAdmin/', delete_Shoes_byAdmin.as_view(), name='delete_Shoes_byAdmin'),
    path('update_Shoes_byAdmin/<str:ProdID>/', update_Shoes_byAdmin.as_view(), name='update_Shoes_byAdmin'),

    path('cloth_Product_admin/', cloth_Product_admin.as_view(), name='cloth_Product_admin'),
    path('clothShow/', clothShow.as_view(), name='clothShow'),
    path('delete_Cloth_byAdmin/', delete_Cloth_byAdmin.as_view(), name='delete_Cloth_byAdmin'),
    path('update_Cloth_byAdmin/<str:ProdID>/', update_Cloth_byAdmin.as_view(), name='update_Cloth_byAdmin'),

    path('watch_Product_admin/', watch_Product_admin.as_view(), name='watch_Product_admin'),
    path('watchShow/', watchShow.as_view(), name='watchShow'),
    path('delete_Watch_byAdmin/', delete_Watch_byAdmin.as_view(), name='delete_Watch_byAdmin'),
    path('update_Watch_byAdmin/<str:ProdID>/', update_Watch_byAdmin.as_view(), name='update_Watch_byAdmin'),

    path('tv_Product_admin/', tv_Product_admin.as_view(), name='tv_Product_admin'),
    path('tvShow/', tvShow.as_view(), name='tvShow'),
    path('delete_Tv_byAdmin/', delete_Tv_byAdmin.as_view(), name='delete_Tv_byAdmin'),
    path('update_Tv_byAdmin/<str:ProdID>/', update_Tv_byAdmin.as_view(), name='update_Tv_byAdmin'),

    path('access_Product_admin/', access_Product_admin.as_view(), name='access_Product_admin'),
    path('accessShow/', accessShow.as_view(), name='accessShow'),
    path('delete_Access_byAdmin/', delete_Access_byAdmin.as_view(), name='delete_Access_byAdmin'),
    path('update_Access_byAdmin/<str:ProdID>/', update_Access_byAdmin.as_view(), name='update_Access_byAdmin'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
