from catalog.models import Course


def get_all_cources():
    return Course.objects.all()


def get_filtered_by_name_cources(name):

    # icontains not work with unicode symbols in sqlite3!
    return Course.objects.filter(name__icontains=name)


def get_course_by_id(id):
    return Course.objects.get(pk=id)