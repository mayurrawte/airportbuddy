"""AirportBuddyy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from staffpanel import views as staffviews


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'stafflogin/',staffviews.staffindex,name="staffindex"),
    url(r'staffregister/',staffviews.staffregister,name="staffregister"),
    url(r'dash/',staffviews.dash,name="dashboard"),
    url(r'getflightstatus/(?P<airport>\w+)/(?P<airline_code>\w+)/(?P<airline_no>\w+)',staffviews.getflightstatus ,name="getFlightStatus"),
    url(r'admin/sos',staffviews.sos, name="SOS"),
    url(r'airportservice/(?P<airport>\w+)/',staffviews.airportservice,name="airport service"),
    url(r'ola/(?P<lat>.*)/(?P<long>.*)/(?P<cat>\w+)',staffviews.olaservice,name="ola service"),
    url(r'getuser/',staffviews.getUser,name="staff user"),
    url(r'stafflogout/',staffviews.logout,name="logout"),
    url(r'faqlist/',staffviews.faqlist,name="faqlist"),
    url(r'notifyuser/',staffviews.notifyuser,name="notify user")
]
