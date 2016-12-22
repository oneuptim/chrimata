from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^auth$', views.login_and_reg),
    url(r'^add_user$', views.add_user),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^markets$', views.markets),
    url(r'^stocks$', views.stocks),
    url(r'^bonds$', views.bonds),
    url(r'^commodities$', views.commodities),
    url(r'^cryptocurrencies$', views.cryptocurrencies),
    url(r'^crypto$', views.crypto),
    url(r'^real_estate$', views.real_estate),
    url(r'^apple$', views.apple),
    url(r'^google$', views.google),
    url(r'^berkshire$', views.berkshire),
    url(r'^gold$', views.gold),
    url(r'^natural_gas$', views.natural_gas),
    url(r'^corn$', views.corn),
    url(r'^bitcoin$', views.bitcoin),
    url(r'^ethereum$', views.ethereum),
    url(r'^monero$', views.monero),
    url(r'^gold_detail_view$', views.gold_detail_view),
    url(r'^supersecret$', views.supersecret),
    url(r'^add_investment$', views.add_investment),
    url(r'^dashboard$', views.dashboard),
    url(r'^add_favorite/(?P<id>\d+)$', views.add_favorite),
    url(r'^remove_favorite/(?P<id>\d+)$', views.remove_favorite),


]
