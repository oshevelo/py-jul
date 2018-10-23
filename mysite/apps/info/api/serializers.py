from rest_framework import serializers


class AboutSerializer(serializers.Serializer):

    release_version = serializers.CharField(read_only=True)
    release_date = serializers.DateTimeField(read_only=True)
    build_version = serializers.IntegerField(read_only=True)
    minor_build_version = serializers.IntegerField(read_only=True)


class MCTPlatformInstallSerializer(serializers.Serializer):
    url = serializers.CharField(read_only=True)
    size = serializers.IntegerField(read_only=True)
    version = serializers.CharField(read_only=True)


class MCTBundlesSerializer(serializers.Serializer):
    windows = MCTPlatformInstallSerializer(read_only=True)
    mac = MCTPlatformInstallSerializer(read_only=True)
    linux = MCTPlatformInstallSerializer(read_only=True)

