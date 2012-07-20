# Google User
picasa_user = "example@gmail.com"

# Album ID - see https://developers.google.com/picasa-web/docs/1.0/developers_guide_python#ListAlbums 
# on how to retrieve it (or just look at the URL in the browser when you are viewing the album)
album_id = "12345678901234567890"
# I didn't implement authentication, so the picasaweb album must be made public
# but it should be trivial in case you want to expose the pictures only via the gallery

# Canonical site name - used throughout for all links and static content

baseurl = "http://saharzukerman.com"


# Tornado listening port (don't forget to point your static content server to this)
listen_port = 8080

# Google analytics account (the js is already set up in the 'base.html' template)
ga_account = "124376"
