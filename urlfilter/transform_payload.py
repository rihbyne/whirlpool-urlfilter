from urllib.parse import urlparse
import utils
import json

log = utils.UrlfilterLogging().getLogger()

def add_abs_urls(contents):
    try:
        transformed = dict()
        original = dict(json.loads(contents))

        if (original.get('origin') == None or not isinstance(original.get('hrefs'), dict)):
            raise TypeError('unsupported hrefs or origin types')

        origin = original.get('origin')
        hrefs = original.get('hrefs')
        url_ranks = list(hrefs.keys())

        for rank in url_ranks:
            if not isinstance(hrefs[rank], list):
                raise TypeError('{} should be of type list'.format(rank))

            transformed[rank] = list()
            hrefs_in_rank = list(hrefs.get(rank))

            for href_meta in hrefs_in_rank:
                if (not isinstance(href_meta, dict)):
                    raise TypeError('rank list {} should be of type dict'.format(rank))

                new_href_meta = dict()
                new_href_meta = href_meta.copy()

                log.debug('transforming urls for rank {}'.format(rank))

                uri = urlparse(href_meta.get("url"))

                if len(uri.scheme) == 0 or uri.hostname == None:
                    tmp_href = "{}{}".format(origin, uri.path)
                    new_href_meta['url'] = tmp_href

                transformed[rank].append(new_href_meta)

        log.info('made urls absolute for origin {}'.format(origin))
    except TypeError as attr_err:
        log.error('AttributeError {}'.format(attr_err))

    return transformed
