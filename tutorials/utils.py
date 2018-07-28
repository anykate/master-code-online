from django.utils.text import slugify


def unique_slug_generator(model_instance, title):
    """

    :param model_instance:
    :param title:
    :return:
    """
    slug = slugify(title)
    model_class = model_instance.__class__
    num = 1

    while model_class._default_manager.filter(slug=slug).exists():
        slug = slugify(title)
        slug = f'{slug}-{num}'
        num += 1

    return slug
