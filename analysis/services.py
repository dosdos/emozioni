# -*- coding: utf-8 -*-
import json

from analysis.models import Emotion
from utils.google_natural_language_api import GoogleNLP


def get_nlp_analysis(query):
    print query
    try:
        nlp = GoogleNLP()
        nlp_analysis = nlp.annotate_text(query)
        nlp_analysis = json.dumps(nlp_analysis)
    except Exception as e:
        nlp_analysis = '{}'
        print e
    print nlp_analysis
    return nlp_analysis


def get_sentences(json_dump):
    emotions = {emotion.slug: emotion.category for emotion in Emotion.objects.all()}
    analysis = json.loads(json_dump)
    matching_emotions = [emotions.get(token['lemma']) for token in analysis['tokens'] if token['lemma'] in emotions]
    return {
        'sentences': analysis['sentences'],
        'emotions': matching_emotions,
    }
