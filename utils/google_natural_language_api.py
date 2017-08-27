"""
https://cloud.google.com/natural-language/docs/sentiment-tutorial
"""
import sys
from pprint import pprint

import httplib2
from googleapiclient import discovery
from googleapiclient.errors import HttpError

NLP_API_KEY = "AIzaSyDVQQU2X9oeEzTeo9Uv0VJ_op5pyUfiC1I"


class GoogleNLP(object):
    discovery_url = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
    key = NLP_API_KEY

    def __init__(self, api='language', version='v1beta1'):
        self.service = discovery.build(
            api,
            version,
            http=httplib2.Http(),
            discoveryServiceUrl=self.discovery_url,
            developerKey=self.key,
        )

    def analyze_entities(self, input_text, is_html=False):
        """
        https://cloud.google.com/natural-language/reference/rest/v1beta1/documents/analyzeEntities

        :param input_text: the text to analyse
        :param is_html: 'True' if text contains html tags, 'False' by default
        :return:
            If successful, the response body contains data with the following structure:
                {
                    "entities": [ { object(Entity) } ],
                    "language": string,
                }
        """
        service_request = self.service.documents().analyzeEntities(
            body={
                'document': {
                    'type': 'HTML' if is_html else 'PLAIN_TEXT',
                    'content': input_text,
                },
                'encodingType': 'UTF16' if sys.maxunicode == 65535 else 'UTF32',
            })

        try:
            response = service_request.execute()
        except HttpError, e:
            response = {'error': e}

        return response

    def analyze_sentiment(self, input_text, is_html=False):
        """
        https://cloud.google.com/natural-language/reference/rest/v1beta1/documents/analyzeSentiment

        :param input_text: the text to analyse
        :param is_html: 'True' if text contains html tags, 'False' by default
        :return:
            If successful, the response body contains data with the following structure:
                {
                    "documentSentiment": { object(Sentiment) },
                    "language": string,
                }
        """
        service_request = self.service.documents().analyzeSentiment(
            body={
                'document': {
                    'type': 'HTML' if is_html else 'PLAIN_TEXT',
                    'content': input_text,
                },
            })

        try:
            response = service_request.execute()
        except HttpError, e:
            response = {'error': e}

        return response

    def annotate_text(self, input_text, is_html=False):
        """
        https://cloud.google.com/natural-language/reference/rest/v1beta1/documents/annotateText

        :param input_text: the text to analyse
        :param is_html: 'True' if text contains html tags, 'False' by default
        :return:
            If successful, the response body contains data with the following structure:
                {
                    "sentences": [ { object(Sentence) } ],
                    "tokens": [ { object(Token) } ],
                    "entities": [ { object(Entity) } ],
                    "documentSentiment": { object(Sentiment) },
                    "language": string,
                }
        """
        service_request = self.service.documents().annotateText(
            body={
                'document': {
                    'type': 'HTML' if is_html else 'PLAIN_TEXT',
                    'content': input_text,
                },
                'features': {
                    'extract_syntax': True,
                    'extractEntities': True,
                    'extractDocumentSentiment': True,
                },
                'encodingType': 'UTF16' if sys.maxunicode == 65535 else 'UTF32',
            })

        try:
            response = service_request.execute()
        except HttpError, e:
            response = {'error': e}

        return response


if __name__ == '__main__':
    text = u"Super Mario si sente contenta. Luigi invece si sente preoccupatissimo."

    nlp = GoogleNLP()
    pprint(nlp.analyze_entities(text))
    pprint(nlp.analyze_sentiment(text))
    pprint(nlp.annotate_text(text))
