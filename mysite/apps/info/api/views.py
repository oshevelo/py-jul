from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.info.api.serializers import AboutSerializer, MCTBundlesSerializer
from apps.info import release_metadata
#from apps.info import mct_install
#from project.defs import MCTPlatform


class AboutDetails(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated, )

    serializer_class = AboutSerializer

    def get_object(self):
        return dict(
            release_version=release_metadata.release_version(),
            release_date=release_metadata.release_date(),
            build_version=release_metadata.build_version(),
            minor_build_version=1
        )


class MCTInstallDetails(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = MCTBundlesSerializer

    def get_object(self):
        return dict(
            #windows=mct_install.bundle_info(MCTPlatform.windows),
            #mac=mct_install.bundle_info(MCTPlatform.mac),
            #linux=mct_install.bundle_info(MCTPlatform.linux)
        )
