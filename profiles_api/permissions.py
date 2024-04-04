from rest_framework import permissions

# 본인만 정보를 수정할 수 있겠금.
class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own profile """
    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            #get 요청일 경우 모두 True
            return True

        return obj.id == request.user.id
