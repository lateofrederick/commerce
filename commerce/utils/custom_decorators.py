from django.contrib.auth.decorators import user_passes_test

from commerce.models.user_profile import UserProfile


def _is_user_belong_to_group(user, group_names):
    return bool(user.groups.filter(name__in=group_names))


def user_in_groups(group_names):
    def is_in_group(user):
        return _is_user_belong_to_group(user, group_names)

    return user_passes_test(is_in_group)


def is_seller():
    return user_in_groups([UserProfile.SELLER])


def is_buyer():
    return user_in_groups([UserProfile.BUYER])
