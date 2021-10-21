from datetime import datetime
from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    context_object_name = "rooms"
    paginate_by = 10
    paginate_orphans = 9

    def get_context_data(self, **context):
        now = datetime.now()
        context["now"] = now
        return super().get_context_data(**context)
