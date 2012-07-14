quickfolio
==========

Simple Gallery/Portfolio Site with Picasa Web Albums as the CMS (using Tornado and Google Data API)

The idea is to have a simle way for users to update their portfolio without having to install a full blown CMS or use a database or some bloated blogging software.
An added value gained by using the gdata api is a robust yes simple portfolio site, without having to serve any of the images, so in theory, any site using this should be able to withstand any feasible level of slashdot effect. 


**quickfolio_nginx** is an example of an nginx configuration for serving the site

**app/** includes the **main.py** and the templates. The most interesting template is **gallery.py**, it contains some logic for presenting the table of thumbnails etc.

**static/** holds static content (css, js, various images).
