from rest_framework.permissions import BasePermission

class adminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'AD'


class staffPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'ST'

class StaffOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == 'ST' or request.user.user_type == 'AD')


class customerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'CU'
