# This script dumps all HydroShare TimeSeries resource-relevant data into timeseriesresource.json to be used to  
# ingest the auxiliary generic resource access control data back into new system for manual migration purpose.
# This script is most likely not needed, though, since we most likely do not need to dump resources by type
# but rather dump all resources with all types with single script.   
# Author: Hong Yi
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'hydroshare.settings'

import django
from django.core import serializers
from hs_app_timeseries.models import TimeSeriesResource 

django.setup()
data = serializers.serialize("json", TimeSeriesResource.objects.all(), fields=('short_id', 'public', 'comments_count', 'rating_count', 'rating_average', 'rating_sum', 'user', 'creator', 'owners', 'view_users', 'edit_users'), indent=4)
out = open("timeseriesresource.json", "w")
out.write(data)
out.close()
