from api.serializers import TroubleSerializer, ExtendedTroubleSerializer

class TroubleSerializerFactory:
    MODE_SIMPLE = 'simple'
    MODE_EXTENDED = 'extended'
    MODE_TYPES = [MODE_SIMPLE, MODE_EXTENDED]
    DEFAULT_MODE = MODE_SIMPLE

    def __init__(self, mode=DEFAULT_MODE):
        self.mode = mode if mode in self.MODE_TYPES else self.DEFAULT_MODE

    def getSerializer(self, instance, many=False):
        if self.mode == self.MODE_EXTENDED:
            return ExtendedTroubleSerializer(instance, many=many)
        else:
            return TroubleSerializer(instance, many=many)
