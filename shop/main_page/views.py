from rest_framework.response import Response
from rest_framework.views import APIView
from main_page.models import *
from django.db.models import Prefetch
from coreapp.utils import create_data_dict
from django.shortcuts import get_object_or_404


class MainPageView(APIView):
    def get(self, request, position, page, format=None):
        position_on_page = position
        if page == 'about':
            position_on_page = Section.objects.filter(page='main').order_by('position').last().position + position
        elif page == 'hip':
            position_on_page = Section.objects.filter(page='about').order_by('position').last().position + position
        elif page == 'leg':
            position_on_page = Section.objects.filter(page='hip').order_by('position').last().position + position
        elif page == 'arm':
            position_on_page = Section.objects.filter(page='leg').order_by('position').last().position + position
        elif page == 'swim':
            position_on_page = Section.objects.filter(page='arm').order_by('position').last().position + position
        elif page == 'sport':
            position_on_page = Section.objects.filter(page='swim').order_by('position').last().position + position
        section = get_object_or_404(
                Section.objects.prefetch_related(
                        Prefetch('textcontent_set'),
                        Prefetch('buttoncontent_set'),
                        Prefetch('headercontent_set'),
                        Prefetch('imagecontent_set'),
                        Prefetch('listrelatedcontent_set'),
                        Prefetch('formcontent_set')
                ),
                page=page, position=position_on_page
        )
        section_data = create_data_dict(position,
                                        text_content=section.textcontent_set.all(),
                                        button_content=section.buttoncontent_set.all(),
                                        header_content=section.headercontent_set.all(),
                                        image_content=section.imagecontent_set.all(),
                                        list_content=section.listrelatedcontent_set.all(),
                                        form_content=section.formcontent_set.all())

        return Response(section_data)


class FooterPageView(APIView):
    def get(self, request):
        section = get_object_or_404(
                Section.objects.prefetch_related(
                        Prefetch('textcontent_set'),
                        Prefetch('buttoncontent_set'),
                        Prefetch('headercontent_set'),
                        Prefetch('imagecontent_set'),
                        Prefetch('listrelatedcontent_set'),
                        Prefetch('formcontent_set')
                ),
                page='footer',
        )
        section_data = create_data_dict(42,
                                        text_content=section.textcontent_set.all(),
                                        button_content=section.buttoncontent_set.all(),
                                        header_content=section.headercontent_set.all(),
                                        image_content=section.imagecontent_set.all(),
                                        list_content=section.listrelatedcontent_set.all(),
                                        form_content=section.formcontent_set.all())

        return Response(section_data)


class ContactsPageView(APIView):
    def get(self, request):
        section = get_object_or_404(
                Section.objects.prefetch_related(
                        Prefetch('textcontent_set'),
                        Prefetch('buttoncontent_set'),
                        Prefetch('headercontent_set'),
                        Prefetch('imagecontent_set'),
                        Prefetch('listrelatedcontent_set'),
                        Prefetch('formcontent_set')
                ),
                page='contacts',
        )
        section_data = create_data_dict(41,
                                        text_content=section.textcontent_set.all(),
                                        button_content=section.buttoncontent_set.all(),
                                        header_content=section.headercontent_set.all(),
                                        image_content=section.imagecontent_set.all(),
                                        list_content=section.listrelatedcontent_set.all(),
                                        form_content=section.formcontent_set.all())

        return Response(section_data)
