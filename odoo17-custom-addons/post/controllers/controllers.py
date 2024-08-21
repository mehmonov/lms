# -*- coding: utf-8 -*-
# from odoo import http


# class Post(http.Controller):
#     @http.route('/post/post', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/post/post/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('post.listing', {
#             'root': '/post/post',
#             'objects': http.request.env['post.post'].search([]),
#         })

#     @http.route('/post/post/objects/<model("post.post"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('post.object', {
#             'object': obj
#         })

