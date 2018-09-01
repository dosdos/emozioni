import time

from django.core.management.base import BaseCommand

from analysis.constants import EMOTIONS
from analysis.models import Emotion


class Command(BaseCommand):
    help = 'Load emotion mapping from constants file'

    def handle(self, *args, **options):
        time_start = time.clock()
        added = tot = 0

        for category in EMOTIONS.keys():
            for emotion in EMOTIONS[category]:
                emotion = emotion.lower()
                try:
                    Emotion.objects.get(name=emotion.title())
                    print("DOPPIA!", emotion)
                except Emotion.DoesNotExist:
                    Emotion(name=emotion.title(), category=category).save()
                    added += 1
                tot += 1
                print("[{}] {} -> {}".format(tot, emotion, category))

        print("{}/{} emotions loaded or updated in {} seconds".format(added, tot, time.clock() - time_start))
