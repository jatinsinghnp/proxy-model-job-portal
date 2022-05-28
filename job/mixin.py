
from django.contrib.auth.mixins import LoginRequiredMixin

class CheckUserMixins(LoginRequiredMixin, object):
    def dispatch(self, request, *args, **kwargs):
        
        for usr in  request.user.user_type:
           if usr != 'Company':
                return self.handle_no_permission()
               

        return super(CheckUserMixins, self).dispatch(request, *args, **kwargs)

