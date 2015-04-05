from social.pipeline.partial import partial
from django.shortcuts import redirect


@partial
def get_email(backend, strategy, request, details, is_new=None, user=None, *args, **kwargs):
    if user and user.email:
        return ''
    elif is_new and backend.name=="twitter":
        if strategy.session_get('saved_email'):
            details['email'] = strategy.session_pop('saved_email')
        else:
            return redirect('/required_email/')

def user_details(strategy, details, is_new=None, user=None, *args, **kwargs):
    """Update user details using data from provider."""
    if user and is_new:
        changed = False  # flag to track changes
        protected = ('username', 'id', 'pk') + \
                    tuple(strategy.setting('PROTECTED_USER_FIELDS', []))

        # Update user model attributes with the new data sent by the current
        # provider. Update on some attributes is disabled by default, for
        # example username and id fields. It's also possible to disable update
        # on fields defined in SOCIAL_AUTH_PROTECTED_FIELDS.
        for name, value in details.items():
            if not hasattr(user, name):
                continue
            current_value = getattr(user, name, None)
            if not current_value or name not in protected:
                changed |= current_value != value
                setattr(user, name, value)

        if changed:
            strategy.storage.user.changed(user)