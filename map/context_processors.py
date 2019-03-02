from git import Repo

from django.conf import settings


def get_git_version():
    """
    Get the git version of the site.
    """
    try:
        repo = Repo(settings.BASE_DIR)
        commit = repo.head.commit.hexsha
        name = commit[:7]
        return {'name': name, 'url': u'{}/commit/{}'.format(settings.APP['site']['repository']['url'], commit)}
    except (KeyError, TypeError):
        return {'name': '', 'url': ''}


def git_version(request):
    """
    A context processor to include the git version on all pages.
    """
    return {'git_version': get_git_version()}


def app_settings(request):
    """
    A context processor with all APP settings.
    """
    return {
        'app': settings.APP,
    }
