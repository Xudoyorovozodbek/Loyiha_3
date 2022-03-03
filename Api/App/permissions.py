from rest_framework import permissions
from datetime import datetime, timezone


# class CheckUsers(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         if request.user == 'admin':
#             return True
#         else:
#             return True


class CheckUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.muallif == request.user



        # permissions.IsAuthenticatedOrReadOnly.has_permission(self, request, view)
        # if permissions.IsAuthenticated.has_permission(self, request, view):
        #     if request.method == 'OPTIONS':
        #         return True
        #     else:
        #         return False
        #



