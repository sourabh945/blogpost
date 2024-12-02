from django.urls import path


urlpatterns = [] 

### import urls from inner apps

## from register app that provide login and signup for sites

from .register import urls as register_urls 


urlpatterns += register_urls.urlpatterns

### for api app that provide api function to the app

from .apis import urls as api_urls

urlpatterns += api_urls.urlpatterns