# -*- coding: utf-8 -*-
import json
import re
from urlparse import urlsplit, parse_qs

from odoo import http
from odoo.http import request


class WebsiteSearch(http.Controller):
    @http.route(['/products/search/<string:search>'], type='http', auth='none', methods=['GET'])
    def search(self, search=False ,**kw):
        """
        This function is responsible for handling the request containing query string and will filter data
        according to the query parameters and return the data in json format in http repoonse.
        :return: Http Response
        """
        path_length = 17
        req = request
        root_url = req.httprequest.url
        parsed_url = urlsplit(root_url).path[path_length:]
        query_string = parse_qs(parsed_url)
        if 'page' not in query_string:
            root_url += '&page=1'

        response = {
            'products': False,
        }

        response_404 = {'Result': 'Resource Unavailable'}

        if search:
            domain = self.get_search_domain(query_string)
            products = request.env['product.template'].sudo().search(domain)
            if products:
                total = len(products)
                if 'page' in query_string:
                    page = query_string['page'][0]
                else:
                    page = 1
                if 'per_page' in query_string:
                    per_page = query_string['per_page'][0]
                    l_page = int(total) % int(per_page)
                    if l_page == 1:
                        last_page = (int(total) / int(per_page)) + 1
                    else:
                        last_page = (int(total) / int(per_page))
                else:
                    per_page = 10
                    l_page = int(total) % int(per_page)
                    if l_page == 1:
                        last_page = (int(total) / int(per_page)) + 1
                    else:
                        last_page = (int(total) / int(per_page))
                if page and last_page and int(page) > int(last_page):
                    return json.dumps(response_404)

                response['products'] = []
                for product in products:
                    response['products'].append({
                        'current_page': page,
                        'data': {
                            'id': product.id,
                            'product_name': product.name,
                            'product_description': product.description_sale,
                            'product_url': product.store_url,
                            'shop': {'store_name': product.store_name,
                                     'store_url': product.store_url,
                                     'media': '', },
                            'geolocation': {'city_name': product.city_name,
                                            'state_id': product.state_id.id,
                                            'state_name': product.state_id.name,
                                            'site_id': product.site_id,
                                            'country_id': product.country_id.id,
                                            'country_name': product.country_id.name,
                                            'latitude': product.latitude,
                                            'longitude': product.longitude, },
                            'thumbnail': {'source_url': '%sweb/image/product.template/%s/image' % (
                                          req.httprequest.host_url, product.id),
                                          'thumb_url': '%sweb/image/product.template/%s/image' % (
                                          req.httprequest.host_url, product.id),
                                          'medium_url': '%sweb/image/product.template/%s/image' % (
                                          req.httprequest.host_url, product.id)},

                                },
                        'first_page_url': re.sub("&page=\d+", '&page=%s' % 1, root_url),
                        'last_page': last_page,
                        'next_page_url': re.sub("&page=\d+", '&page=%s' % (int(page)+1), root_url) if page and last_page != 1 else '',
                        'prev_page_url': re.sub("&page=\d+", '&page=%s' % (int(page) - 1), root_url) if page and int(page) != 1 else '',
                        'total': total,
                        'path': root_url,
                        'last_page_url': re.sub("&page=\d+", '&page=%s' % int(last_page), root_url) if last_page else '',
                        'per_page': per_page,
                        'from': page,
                        'to': int(page)+1 if page else ''
                                                })

        return json.dumps(response)

    def get_search_domain(self, search):
        """
        This function is responsible for creating the filter on the basis of query string.
        :param search: It is the dict containing the query string parameters on basis of which the data is to be
        filtered.
        :return: List of tuples containing filters.
        """
        if 'q' in search:
            name = search['q'][0]
            domain = [('name', '=', name)]

        if 'longitude' in search:
            longitude = search['longitude'][0]

            domain = ['&'] + domain
            domain += [('longitude', '=', longitude)]

        if 'latitude' in search:
            latitude = search['latitude'][0]

            domain = ['&'] + domain
            domain += [('latitude', '=', latitude)]

        if 'city_name' in search:
            city_name = search['city_name'][0]
            domain = ['&'] + domain
            domain += [('city_name', '=', city_name)]

        if 'country_id' in search:
            country_id = search['country_id'][0]
            domain = ['&'] + domain
            domain += [('country_id', '=', country_id)]

        if 'site_id' in search:
            site_id = search['site_id'][0]
            domain = ['&'] + domain
            domain += [('site_id', '=', site_id)]

        return domain
