from rest_framework import serializers
from app.models import Tasks

class TaskSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tasks
		fields = ('task_id',
					'title',
					'module',
					'description',
					'st_date',
					'ed_date',
					'status')