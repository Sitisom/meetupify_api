from django_filters.rest_framework import FilterSet, BooleanFilter, BaseInFilter


class GroupFilterSet(FilterSet):
    user = BaseInFilter('users')
    is_active = BooleanFilter()
