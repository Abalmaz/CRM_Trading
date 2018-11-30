from django.core.exceptions import PermissionDenied


class GroupRequiredMixin(object):
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            user_groups = request.user.get_current_groups(request.company)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
