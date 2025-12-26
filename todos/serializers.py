from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True
    )
    
    priority_display = serializers.CharField(
        source='get_priority_display',
        read_only=True
    )
    
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
