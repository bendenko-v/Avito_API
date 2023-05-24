from rest_framework import serializers

from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False, many=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'role', 'age', 'birth_date', 'location'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False, many=True)
    password = serializers.CharField(write_only=True, max_length=120)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'role', 'age', 'birth_date', 'location', 'password'
        )

    def create(self, validated_data):
        location_data = validated_data.pop('location', [])
        user = User.objects.create(**validated_data)
        if location_data:
            for location in location_data:
                location_obj, _ = Location.objects.get_or_create(**location)
                user.location.add(location_obj)
        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False, many=True)
    password = serializers.CharField(write_only=True, max_length=120)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'role', 'age', 'birth_date', 'location', 'password'
        )

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location', [])
        if location_data:
            instance.location.clear()
            for location in location_data:
                location_obj, _ = Location.objects.get_or_create(**location)
                instance.location.add(location_obj)

        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        instance = super().update(instance, validated_data)
        return instance