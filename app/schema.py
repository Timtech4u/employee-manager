"""Give DRF's generated nested serializers stable, distinct OpenAPI names."""
from drf_spectacular.openapi import AutoSchema


class ModelAutoSchema(AutoSchema):
    def get_serializer_name(self, serializer, direction):
        if serializer.__class__.__name__ == 'NestedSerializer':
            return '{}_depth{}'.format(
                serializer.Meta.model._meta.label_lower.replace('.', '_'),
                serializer.Meta.depth,
            )
        return super().get_serializer_name(serializer, direction)

    def get_serializer_identity(self, serializer, direction):
        if serializer.__class__.__name__ == 'NestedSerializer':
            return (serializer.Meta.model, serializer.Meta.depth)
        return super().get_serializer_identity(serializer, direction)
