
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from spotofoweb.views import PlayHistoryView, PlayHistoryCsvView
from spotofoweb.views import CurrentlyPlayingView
from spotofoweb.views import DeviceSelectView
from spotofoweb.views import AuthorizeUserView, AuthorizeResponseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CurrentlyPlayingView.as_view()),
    url(r'^history$', login_required(PlayHistoryView.as_view())),
    url(r'^history/(?P<page>[0-9]+)$', login_required(PlayHistoryView.as_view())),
    url(r'^history/csv$', login_required(PlayHistoryCsvView.as_view())),
    url(r'^devices$', login_required(DeviceSelectView.as_view())),
    url(r'^authorize$', AuthorizeUserView.as_view()),
    url(r'^authorize/response$', AuthorizeResponseView.as_view()),
]

