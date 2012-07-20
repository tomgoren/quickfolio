#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import tornado.template
from quickfolio_config import picasa_user, album_id, baseurl, listen_port, ga_account

# Requires the "python-gdata" package on Ubuntu
import gdata.photos.service

# This is the only interesting handler, it retrieves the list of image URLs and metadata
# from the Picasa Web Albums and renders the "gallery" which is then populated with the data
class GalleryHandler(tornado.web.RequestHandler):
    def get(self):
        title = "Works"

        # thumbnail size hardcoded here, this way we get static urls for everything
        # see Google's API reference on all the various options available
        api_album_url = "/data/feed/api/user/%s/albumid/%s?kind=photo&thumbsize=150c"
        gd_client = gdata.photos.service.PhotosService()
        image_list = gd_client.GetFeed( api_album_url % (
                                  picasa_user, album_id))
        self.render("./templates/gallery.html", baseurl=baseurl, ga_account=ga_account, title=title, image_list=image_list)

# Just a bunch of boilerplate pages for the rest of the site, usually found on a portfolio website
class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/about.html", baseurl=baseurl, ga_account=ga_account, title="About")

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/contact.html", baseurl=baseurl, ga_account=ga_account, title="contact")

class PressHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/press.html", baseurl=baseurl, ga_account=ga_account, title="Press")

class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/news.html", baseurl=baseurl, ga_account=ga_account, title="Current")

application = tornado.web.Application(
    [ ('/', GalleryHandler),
      ('/index.html', GalleryHandler),
      ('/about.html', AboutHandler),
      ('/press.html', PressHandler),
      ('/news.html', NewsHandler),
      ('/contact.html', ContactHandler),
    ])

if __name__ == "__main__":
    application.listen(listen_port)
    tornado.ioloop.IOLoop.instance().start()

