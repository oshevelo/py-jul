from django.conf.urls import url

# /api/info/...
from apps.info.api.views import AboutDetails, MCTInstallDetails

urlpatterns = [
    url(r'^about/$',
        AboutDetails.as_view(), name='api_info_about_details'),
    url(r'^mct-install/$',
        MCTInstallDetails.as_view(), name='api_info_mct_install_details')
]
