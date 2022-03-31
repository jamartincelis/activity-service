from rest_framework import serializers
from activity.models import Activity

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'

    def to_internal_value(self, data):

        data['user'] = self.context.get("request").parser_context["kwargs"]["user"]
        data['project'] = self.context.get("request").parser_context["kwargs"]["project"]
        
        return super().to_internal_value(data)
