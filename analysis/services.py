# -*- coding: utf-8 -*-
import json

from analysis.constants import ENTITY_TYPES
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


def get_entities(row_entities):
    return [{
        'name': entity.get('name'),
        'name_type': ENTITY_TYPES.get(entity.get('type')),
        'wiki_url': entity.get('metadata', {}).get('wikipedia_url'),
    } for entity in row_entities]


def get_sentences(json_dump):
    emotions = {emotion.slug: emotion.category for emotion in Emotion.objects.all()}
    analysis = json.loads(json_dump)
    matching = [emotions.get(token['lemma']) for token in analysis.get('tokens', []) if token['lemma'] in emotions]
    return {
        'sentences': analysis['sentences'] if 'sentences' in analysis else [],
        'entities': get_entities(analysis.get('entities', [])),
        'emotions': set(matching),
        'language': analysis.get('language'),
    }
