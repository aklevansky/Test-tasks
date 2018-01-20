from django.contrib.auth.models import (
    Group,
    Permission,
    User)
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from loans.models import (
    Application,
    Questionnaire,
    Submission)


class Command(BaseCommand):

    def handle(self, *args, **options):
        superusers = Group.objects.get_or_create(name='Суперпользователи')[0]
        partners = Group.objects.get_or_create(name='Партнёры')[0]
        banks = Group.objects.get_or_create(name='Кредитные организации')[0]

        ct_application = ContentType.objects.get_for_model(Application)
        perm_view_application = Permission.objects.get(
            codename='view_application',
            content_type=ct_application)
        perm_add_application = Permission.objects.get(
            codename='add_application',
            content_type=ct_application)
        perm_change_application = Permission.objects.get(
            codename='change_application',
            content_type=ct_application)
        perm_delete_application = Permission.objects.get(
            codename='delete_application',
            content_type=ct_application)

        ct_questionnaire = ContentType.objects.get_for_model(Questionnaire)
        perm_view_questionnaire = Permission.objects.get(
            codename='view_questionnaire',
            content_type=ct_questionnaire)
        perm_add_questionnaire = Permission.objects.get(
            codename='add_questionnaire',
            content_type=ct_questionnaire)
        perm_change_questionnaire = Permission.objects.get(
            codename='change_questionnaire',
            content_type=ct_questionnaire)
        perm_delete_questionnaire = Permission.objects.get(
            codename='delete_questionnaire',
            content_type=ct_questionnaire)

        ct_submission = ContentType.objects.get_for_model(Submission)
        perm_view_submission = Permission.objects.get(
            codename='view_submission',
            content_type=ct_submission)
        perm_add_submission = Permission.objects.get(
            codename='add_submission',
            content_type=ct_submission)
        perm_change_submission = Permission.objects.get(
            codename='change_submission',
            content_type=ct_submission)
        perm_delete_submission = Permission.objects.get(
            codename='delete_submission',
            content_type=ct_submission)

        superusers.permissions.add(perm_view_questionnaire)
        superusers.permissions.add(perm_add_questionnaire)
        superusers.permissions.add(perm_change_questionnaire)
        superusers.permissions.add(perm_delete_questionnaire)
        superusers.permissions.add(perm_add_submission)
        superusers.permissions.add(perm_change_submission)
        superusers.permissions.add(perm_delete_submission)

        partners.permissions.add(perm_view_questionnaire)
        partners.permissions.add(perm_add_questionnaire)
        partners.permissions.add(perm_add_submission)

        banks.permissions.add(perm_view_questionnaire)
        banks.permissions.add(perm_add_questionnaire)
        banks.permissions.add(perm_view_submission)
        banks.permissions.add(perm_add_submission)

        User.objects.filter(username='admin').exists() or \
            User.objects.create_superuser(
                username='admin',
                password='qwer1234',
                email='admin@site.com')

        if not User.objects.filter(username='superuser').exists():
            superuser = User.objects.create_user(
                username='superuser',
                password='qwer1234',
                is_staff=True)
            superusers.user_set.add(superuser)

        if not User.objects.filter(username='partner').exists():
            partner = User.objects.create_user(
                username='partner',
                password='qwer1234',
                is_staff=True)
            partners.user_set.add(partner)

        if not User.objects.filter(username='bank').exists():
            bank = User.objects.create_user(
                username='bank',
                password='qwer1234',
                is_staff=True)
        else:
            bank = User.objects.get(username='bank')
        banks.user_set.add(bank)

        a = Application.objects.create(
            application_name='I need some money',
            score_min=1,
            score_max=2,
            bank=bank)
        q = Questionnaire.objects.create(
            name='Соломон Моисеевич',
            phone='123',
            passport='abc123',
            score=2)
        Submission.objects.create(
            application=a,
            questionnaire=q)