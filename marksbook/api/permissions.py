from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """ Only Author can use Unsafe methods"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class OwnerOnly(permissions.BasePermission):
    """ If we want to hide our Bookmarks from others """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
