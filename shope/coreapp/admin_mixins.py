class TextMixin:
    extra = 0
    fields = ('position', 'title', 'data')
    # После разработки убрать position из fields
    can_delete = False


class ImageMixin:
    fields = ('position', 'title', 'data', 'image_tag')
    # После разработки убрать position из fields
    readonly_fields = ('image_tag', )
    extra = 0
    can_delete = False


class HeaderMixin:
    extra = 0
    fields = ('position', 'title', 'type', 'data')
    # После разработки убрать position из fields
    can_delete = False


class ButtonMixin:
    extra = 0
    fields = ('position', 'title', 'data')
    # После разработки убрать position из fields
    can_delete = False


class SectionMixin:
    list_display = ('id', 'title')
