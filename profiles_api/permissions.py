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

class UpdateOwnStatus(permissions.BasePermission):
    """유저가 자신의 status만 변경가능 """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
