from django.urls import path
from orchestrator.views import *

urlpatterns = [ 
    path('pedophiles/create', create_pedophile, name='createPedophile'), 
    path('pedophiles/update', update_pedophile, name='updatePedophile'),
    path('pedophiles/delete', delete_pedophile, name='deletePedophile'),
    path('pedophiles/findOne', find_one_pedophile, name='findOnePedophile'),
    path('pedophiles/findAll', find_all_pedophiles, name='findAllPedophiles'),
    path('pedophiles/findBy', find_by_pedophiles, name='findByPedophiles'),

    path('baiters/create', create_baiter, name='createBaiter'), 
    path('baiters/update', update_baiter, name='updateBaiter'),
    path('baiters/delete', delete_baiter, name='deleteBaiter'),
    path('baiters/findOne', find_one_baiter, name='findOneBaiter'),
    path('baiters/findAll', find_all_baiters, name='findAllBaiters'),
    path('baiters/findBy', find_by_baiters, name='findByBaiters'),
    
    path('conversations/create', create_conversation, name='createConversation'), 
    path('conversations/update', update_conversation, name='updateConversation'),
    path('conversations/delete', delete_conversation, name='deleteConversation'),
    path('conversations/findOne', find_one_conversation, name='findOneConversation'),
    path('conversations/findAll', find_all_conversations, name='findAllConversations'),
    path('conversations/findBy', find_by_conversations, name='findByConversations'),
    
    #path('messages/create', create_message, name='createMessage'),
    path('messages/initFirstMessage', find_by_messages, name='initFirstMessage'),
    path('messages/create/ai', create_ai_message, name='create_ai_message'), 
    path('messages/create/pedophile', create_pedophile_message, name='create_pedophile_message'), 
    path('messages/update', update_message, name='updateMessage'),
    path('messages/delete', delete_message, name='deleteMessage'),
    path('messages/findOne', find_one_message, name='findOneMessage'),
    path('messages/findAll', find_all_messages, name='findAllMessages'),
    path('messages/findBy', find_by_messages, name='findByMessages'),

    path('socialnetworks/create', create_social_network, name='createSocialNetwork'), 
    path('socialnetworks/update', update_social_network, name='updateSocialNetwork'),
    path('socialnetworks/delete', delete_social_network, name='deleteSocialNetwork'),
    path('socialnetworks/findOne', find_one_social_network, name='findOneSocialNetwork'),
    path('socialnetworks/findAll', find_all_social_networks, name='findAllSocialNetworks'),
    path('socialnetworks/findBy', find_by_social_networks, name='findBySocialNetworks'),
]