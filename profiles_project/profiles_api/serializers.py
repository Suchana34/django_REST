from rest_framework import serializers

class helloserializers(serializers.Serializer):
    #serialises a name field for testing our apiview

    name = serializers.CharField(max_length = 20)
