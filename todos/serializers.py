from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(read_only=True)
    priority_display = serializers.CharField(read_only=True)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status_display'] = instance.get_status_display()
        data['priority_display'] = instance.get_priority_display()
        return data
    
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'status',
            'status_display',
            'priority',
            'priority_display',
            'due_date',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'status_display', 'priority_display']
