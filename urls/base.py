from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = []

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)



### views_category_one ###

# urlpatterns += patterns('app_name.views.views_category_one',

    # url(r'^modela/$', 'list', name='ListModelA'),
    # url(r'^modela/add/?$', 'add', name='AddModelA'),
# )


### views_category_two ###

# urlpatterns += patterns('app_name.views.views_category_two',

    # url(r'^modelb/', 'list', name='ListModelB'),
    # url(r'^modelb/add/', 'add', name='AddModelB'),
# )


