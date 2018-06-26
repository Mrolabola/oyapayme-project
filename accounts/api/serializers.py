from rest_framework import serializers

from ..models import Agent, Admin, User


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    agents = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='agent-detail')
    id = serializers.ReadOnlyField(source='user.id')
    phone_number = serializers.ReadOnlyField(source='user.phone_number')
    fullname = serializers.ReadOnlyField(source='user.fullname')

    class Meta:
        model = Admin
        fields = ('id', 'url', 'phone_number', 'fullname', 'business_name', 'agents')


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    phone_number = serializers.ReadOnlyField(source='user.phone_number')
    fullname = serializers.ReadOnlyField(source='user.fullname')
    admin = serializers.ReadOnlyField(source='admin.user.fullname')

    class Meta:
        model = Agent
        fields = ('id', 'url', 'phone_number', 'fullname', 'admin')
