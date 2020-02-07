from rest_framework import exceptions, serializers
from django.contrib.auth.models import User
from .models import info


class UserregisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={"input_type": "password"})
	class Meta():
		model = info
		fields = ('lastName',)

class UserregisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
	class Meta():
		model = User
		fields = ('username','password','email','first_name','last_name')

	def create(self, validated_data):
		# print(validated_data)
		album = User.objects.create(**validated_data)
		# print(album,album.id,album.pk)
		tracks_data = {
			"lastName" : validated_data['last_name'],
			"reader_id":album.pk
			}
		# for track_data in tracks_data:
		info.objects.create(**tracks_data)


		return album