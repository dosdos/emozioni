import time

from django.core.management.base import BaseCommand

from analysis.constants import EMOTIONS
from analysis.models import Emotion


class Command(BaseCommand):
    help = 'Create and assign Knowledge Graph nodes into learning paths entities'

    def handle(self, *args, **options):
        time_start = time.clock()
        added = 0

        for category in EMOTIONS.keys():
            for emotion in EMOTIONS[category]:
                Emotion.objects.get_or_create(name=emotion, category=category)
                added += 1

        print "{} emotions loaded or updated in {} seconds".format(added, time.clock() - time_start)
