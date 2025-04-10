from django.urls import path
from . import views

urlpatterns = [ 
    path('pedophiles/create', views.create_pedophile, name='createPedophile'), 
    path('pedophiles/update', views.update_pedophile, name='updatePedophile'),
    path('pedophiles/delete', views.delete_pedophile, name='deletePedophile'),
    path('pedophiles/findOne', views.get_pedophile, name='findOnePedophile'),
    path('pedophiles/findAll', views.list_pedophiles, name='findAllPedophiles'),
    path('pedophiles/findBy', views.list_some_pedophiles, name='findByPedophiles'),

    path('baiters/create', views.create_baiter, name='createBaiter'), 
    path('baiters/update', views.update_baiter, name='updateBaiter'),
    path('baiters/delete', views.delete_baiter, name='deleteBaiter'),
    path('baiters/findOne', views.get_baiter, name='findOneBaiter'),
    path('baiters/findAll', views.list_baiters, name='findAllBaiters'),
    path('baiters/findBy', views.list_some_baiters, name='findByBaiters'),
    
    path('conversations/create', views.create_conversation, name='createConversation'), 
    path('conversations/update', views.update_conversation, name='updateConversation'),
    path('conversations/delete', views.delete_conversation, name='deleteConversation'),
    path('conversations/findOne', views.get_conversation, name='findOneConversation'),
    path('conversations/findAll', views.list_conversations, name='findAllConversations'),
    path('conversations/findBy', views.list_some_conversations, name='findByConversations'),
    
    path('messages/create', views.create_message, name='createMessage'), 
    path('messages/update', views.update_message, name='updateMessage'),
    path('messages/delete', views.delete_message, name='deleteMessage'),
    path('messages/findOne', views.get_message, name='findOneMessage'),
    path('messages/findAll', views.list_messages, name='findAllMessages'),
    path('messages/findBy', views.list_some_messages, name='findByMessages'),

    path('socialnetworks/create', views.create_social_network, name='createSocialNetwork'), 
    path('socialnetworks/update', views.update_social_network, name='updateSocialNetwork'),
    path('socialnetworks/delete', views.delete_social_network, name='deleteSocialNetwork'),
    path('socialnetworks/findOne', views.get_social_network, name='findOneSocialNetwork'),
    path('socialnetworks/findAll', views.list_social_networks, name='findAllSocialNetworks'),
    path('socialnetworks/findBy', views.list_some_social_networks, name='findBySocialNetworks'),
    
    path('apis/create', views.create_api, name='apiCreate'), 
    path('apis/update', views.update_api, name='apiUpdate'),
    path('apis/delete', views.delete_api, name='apiDelete'),
    path('apis/findOne', views.get_api, name='apiFindOne'),
    path('apis/findAll', views.list_apis, name='apiFindAll'),
    path('apis/findBy', views.list_some_apis, name='apiFindBy'),
]