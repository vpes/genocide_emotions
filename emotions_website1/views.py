import json

from django.core.paginator import Paginator
from django.middleware.csrf import CsrfViewMiddleware
from django.template import loader

from django.http import HttpResponse
from django.views.generic.base import View,TemplateResponseMixin

from emotions_website1.models import VisitorQuery


class PermissionException(object):
    pass


class HomePageView(TemplateResponseMixin,View):
    http_method_names = ['get', 'post']
    template_name = 'video_1.html'

    def check_csrf(self,request):
        reason = CsrfViewMiddleware().process_view(request, None, (), {})
        if reason:
            # CSRF failed
            raise PermissionException()

    def dispatch(self,request, *args, **kwargs):
        import threading
        from emotions_website1.process_query import do_process_query
        if request.method == 'GET':
            context = {
                'xxx': 0,
            }
            return self.render_to_response(context)
        elif request.method == 'POST':
            try:
                self.check_csrf(request)
                keyword = request.POST.get('keyword')
                name = request.POST.get('name')
                ip = request.META.get('REMOTE_ADDR')
                vq = VisitorQuery.objects.create(keywords=keyword,
                             name=name,
                             ip=ip)
                response = {'valid': True}
                t = threading.Thread(target=do_process_query, args=(vq.id), kwargs={})
                t.setDaemon(True)
                t.start()

            except Exception as ex:
                response = {'valid': False,'error':str(ex)}
            return HttpResponse(json.dumps(response), content_type="application/json")

class SearchListPageView(TemplateResponseMixin,View):
    http_method_names = ['get']
    template_name = 'search_list.html'

    def dispatch(self,request, *args, **kwargs):
        try:
            if request.GET.get('page') is None:
                return self.render_to_response({})
            else:
                sort = next(key for key in request.GET if key.startswith('sorts'))
                if sort:
                    sort = '{}{}'.format('-' if request.GET.get(sort) else '',sort[6:-1])
                else:
                    sort = '-created'
                total_count = VisitorQuery.objects.count()
                records = VisitorQuery.objects.all().order_by(sort)
                # self.check_csrf(request)
                page = int(request.GET.get('page'))
                paginator = Paginator(records, int(request.GET.get('pageSize','10')))
                response = {"queryRecordCount": total_count,
                            "totalRecordCount": total_count,
                            "records":[{'created':'{:%d/%m/%Y %H:%M}'.format(x.created),
                             'keywords':x.keywords,
                             'name':x.name,
                             'country':x.country.name if x.country else '',
                             'results':self.get_results(x)} for x in paginator.page(page)]}
        except Exception as ex:
            response = {'valid': False, 'error': str(ex)}
        return HttpResponse(json.dumps(response), content_type="application/json")

    def get_results(self,query):
        return query.visitorqueryresult_set.count() or 'Procesando...'


class PresentationPageView(TemplateResponseMixin,View):
    http_method_names = ['get']
    template_name = 'presentation.html'

    def dispatch(self,request, *args, **kwargs):
        return self.render_to_response({})

class ReferencesPageView(TemplateResponseMixin,View):
    http_method_names = ['get']
    template_name = 'references.html'

    def dispatch(self,request, *args, **kwargs):
        return self.render_to_response({})
