from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import imsUser,Payment
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class customTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(customTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'user_type': self.user.user_type})
        return data


class adminTokenObtainPairSerializer(TokenObtainPairSerializer):
    # only admin can get the token 
    default_error_message = {
        'not_admin': ("You don't have permission to login!!!")
    }

    @classmethod
    def get_token(cls, adminUser):
        # if adminUser.user_type == 'AD':
        token = super(adminTokenObtainPairSerializer, cls).get_token(adminUser)
        token['username'] = adminUser.username
        return token

    def validate(self, attrs):
        data = super(adminTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        return data


class registerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=imsUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = imsUser
        fields = ('username', 'password',
                  'password2', 'email',
                  'name', 'Landline_number',
                  'mobile_number', 'address',
                  'user_type', 'pay', 'profile_pic',
                  )
        extra_kwargs = {
            'name': {'required': True},
            'address': {'required': True},
            'Landline_number': {'required': False},
            'mobile_number': {'required': False},
            'user_type': {'required': True},
            'pay': {'required': False},
            'profile_pic': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match!"})

        return attrs

    def create(self, validated_data):
        user = imsUser.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            Landline_number=validated_data.get('Landline_number', '000000000'),
            mobile_number=validated_data.get('mobile_number', '000000000'),
            address=validated_data.get('address'),
            user_type=validated_data.get('user_type'),
        )
        if 'pay' in validated_data.keys():
            user.pay = validated_data['pay']

        user.set_password(validated_data['password'])
        user.save()

        return user


class changePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = imsUser
        fields = ('old_password', 'new_password', 'new_password2')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError(
                {"new_password": "Password fields didn't match"})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password not correct!"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance

class staffPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('staff','paid_at')
    
    def create(self,validated_data):
        print(datetime.today().month)
        if len(Payment.objects.filter(staff=validated_data['staff']).filter(paid_at__month=datetime.today().month)) == 0:
            instance = Payment.objects.create(staff=validated_data['staff'],paid_money = validated_data['staff'].pay)
            return instance
        else:
            raise serializers.ValidationError({'error':'Cannot Pay ! already paid for the month'})

    def update(self,instance,validated_data):
        instance.paid_money = validated_data.get('paid_money',instance.paid_money)
        instance.save()
        return instance


class updateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = imsUser
        fields = (
                  'name', 'Landline_number',
                  'mobile_number', 'address',
                  'user_type','pay'
                  )

        extra_kwargs = {
            'name': {'required': True},
            'address': {'required': True},
            'Landline_number': {'required': False},
            'mobile_number': {'required': False},
        }


    def update(self, instance, validated_data):
        user = self.context['request'].user
        # realUser = imsUser.objects.get()
        print(instance.username)
        if user.pk == instance.pk or user.user_type == "AD":
            instance.username = validated_data.get('username',instance.username)
            instance.email = validated_data.get('email',instance.email)
            instance.name = validated_data.get('name')
            instance.pay = validated_data.get('pay')
            instance.Landline_number = validated_data.get(
                'Landline_number', '+000000000')
            instance.mobile_number = validated_data.get(
                'mobile_number', '+9999999999')
            instance.address = validated_data.get('address')
            instance.is_employee = validated_data.get('is_employee')
            instance.is_customer = validated_data.get('is_customer')

            instance.save()

            return instance

        else:      
            raise serializers.ValidationError(
                {"authorize": "You don't have permission to update profile for this user!"})


class logoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')

class staffPaymentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('staff','paid_money', 'paid_at') 

# Staff management:
class staffManagementSerializer(serializers.ModelSerializer):
    payment_set = staffPaymentDataSerializer(many=True,read_only=True)
    class Meta:
        model = imsUser
        fields = (
            'id', 'username', 'email',
                'name', 'Landline_number',
                'mobile_number', 'address',
                'pay',
                'user_type',
                'created_at',
                'payment_set'
                )



# Customer management:
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = imsUser
        fields = ('id', 'username', 'email',
                'name', 'mobile_number', 'address',
                'user_type',
                'created_at',
                )

        

        



