django-forums
===============

Small standalone django forums application.

## Key features

* Reusable forums app
* Templates use Bootstrap (twitter) styles
* ...

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-forums

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-forums#egg=django-forums

Add `forums` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'forums',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^your-url/$', include('forums.urls')),
        ...
    )

