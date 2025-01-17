# -*- coding: utf-8 -*-
ENTITY_TYPES = {
    'UNKNOWN': "Sconosciuto",
    'PERSON': "Persona",
    'LOCATION': "Luogo",
    'ORGANIZATION': "Organizzazione",
    'EVENT': "Evento",
    'WORK_OF_ART': "Opera d'arte",
    'CONSUMER_GOOD': "Prodotto",
    'OTHER': "Altro",
}
MENTION_TYPES = {
    'UNKNOWN': "Sconosciuto",
    'PROPER': "Proprio",
    'COMMON': "Comune",
}

SAMPLE_SENTENCE = "Il giocatore che mi rende più contento di tutti è Messi. Invece Ronaldo non mi piace proprio, " \
                  "anche se ho la sua maglia del Real."

SORROW = 'tristezza'
ANGER = 'rabbia'
SURPRISE = 'sorpresa'
JOY = 'gioia'
CONTEMPT = 'disprezzo'
DISGUST = 'disgusto'
FEAR = 'paura'
SHAME = 'vergogna'

EMOTION_CATEGORIES_CHOICES = (
    (SORROW, 'Tristezza'),
    (ANGER, 'Rabbia'),
    (SURPRISE, 'Sorpresa'),
    (JOY, 'Gioia'),
    (CONTEMPT, 'Disprezzo'),
    (DISGUST, 'Disgusto'),
    (FEAR, 'Paura'),
    (SHAME, 'Vergogna'),
)

EMOTIONS = {
    SORROW: [
        "abbandono", "abbandonare", "abbandonato",
        "abbattimento", "abbattere", "abbattuto",
        "accasciare", "accasciato",
        "addoloramento", "addolorare", "addolorato",
        "afflizione", "affliggimento", "affliggere", "afflitto",
        "affrangere", "affranto",
        "amarezza", "amareggiare", "amareggiato",
        "angoscia", "angosciare", "angosciato",
        "autocommiserare", "autocommiserazione",
        "avvilimento", "avvilire", "avvilito", "avvilente",
        "bisognoso",
        "colpevolezza", "incolpare", "colpevolizzare", "colpevole", "colpevolmente",
        "contrizione", "contrire", "contrito",
        "cupezza", "incupire", "cupo", "cupamente",
        "delusione", "deludere", "deluso", "deludente",
        "depressione", "deprimere", "depresso",
        "desolazione", "desolare", "desolato", "desolante",
        "disillusione", "disilludere", "disilluso",
        "disperazione", "disperare", "disperato", "disperatamente",
        "dolore", "dolere", "dolente",
        "ferita", "ferire", "ferito",
        "frustrazione", "frustrare", "frustrato", "frustrante",
        "infelicità", "infelice", "infelicemente",
        "insoddisfazione", "insoddisfatto", "insoddisfacente",
        "isolamento", "isolare", "isolatamente",
        "malinconia", "malinconico", "malinconicamente",
        "mestizia", "mesto", "mestamente",
        "noia", "annoiare", "annoiato",
        "nostalgia", "nostalgico", "nostalgicamente",
        "oppressione", "opprimere", "oppresso", "opprimente",
        "pena", "penare", "penoso", "penosamente",
        "penitente",
        "perdita", "perdere", "perduto", "perdente",
        "prostrazione", "prostrare", "prostrato",
        "rassegnazione", "rassegnare", "rassegnato", "rassegnatamente",
        "rattristare", "rattristato",
        "rimordere", "rimorso",
        "rimpianto", "rimpiangere",
        "rincrescimento", "rincrescere", "rincresciuto",
        "sconforto", "sconfortare", "sconfortato", "sconfortante",
        "scontento", "scontentare",
        "scoraggiamento", "scoraggiare", "scoraggiato", "scoraggiante", "scoraggiatamente",
        "sofferenza", "soffrire", "sofferto", "sofferente",
        "solitudine",
        "squallore", "squallido",
        "stanchezza", "stancare", "stanco", "stancante",
        "stufo", "stufare",
        "svilire", "svilito", "svilente",
        "tetro", "tetramente",
        "tormento", "tormentare", "tormentato", "tormentosamente",
        "trasandato", "trasandatamente",
        "trascuratezza", "trascurare", "trascurato", "trascuratamente",
        "tristezza", "intristire", "triste", "tristemente",
    ],
    ANGER: [
        "acrimonia", "acrimonioso", "acrimoniosamente",
        "alterazione", "alterare", "alterato",
        "animosità", "animoso", "animosamente",
        "arrabbiatura", "arrabbiare", "arrabbiato",
        "astio", "astioso", "astiosamente",
        "collera", "collerico", "collericamente",
        "esasperazione", "esasperare", "esasperato", "esasperatamente",
        "furia", "furibondo", "furioso", "furiosamente",
        "gelosia", "ingelosire", "geloso", "gelosamente",
        "impaziente", "impazientememte",
        "incavolatura", "incavolare", "incavolato",
        "incazzatura", "incazzare", "incazzato",
        "indignazione", "indignare", "indignato",
        "inferocito",
        "infuriare", "infuriato",
        "intrattabile", "intrattabilmente",
        "invidia", "invidiare", "invidioso", "invidiosamete",
        "ira", "irare", "irato", "iratamente",
        "irritabilità", "irritazione", "irritare", "irritabile", "irritevole", "irritevolmente",
        "odio", "odiare", "odioso", "odiosamente",
        "offesa", "offendere", "offeso", "offensivo", "offensivamente",
        "ostilità", "ostile", "ostilmente",
        "permalosità", "permaloso",
        "rabbia", "rabbioso", "rabbiosamente",
        "risentimento", "risentire", "risentitamente", "risentito",
        "scontrosità", "scontroso",
        "stizza", "stizzire", "stizzosamente", "stizzoso",
        "suscettibilità", "suscettibile", "suscettibilmente",
        "vendetta", "vendicare", "vendicativamente", "vendicativo", "vendicatore",
        "violenza", "violento", "violentemente",
    ],
    SURPRISE: [
        "annebbiato",
        "attonitaggine", "attonimento", "attonito", "attonitamente",
        "caotico", "caoticamente",
        "colpito",
        "confusione", "confondere", "confuso", "confusamente",
        "disarmonia", "disarmonizzare", "disarmonioso", "disarmonico", "disarmonicamente",
        "disordine", "disordinare", "disordinato", "disordinatamente",
        "disorganizzazione", "disorganizzare", "disorganizzato", "disorganizzatamente",
        "diversità", "diverso", "diversamente",
        "esterrefatto",
        "impressionare", "impressionato",
        "incantamento", "incantatore", "incantare", "incantato",
        "incasinamento", "incasinare", "incasinato", "incasinatamente",
        "incoerenza", "incoerente",
        "incomprensibilità", "incomprensibile", "incomprensibilmente",
        "incredulità", "incredulo",
        "indistinto", "indistintamente",
        "meraviglia", "meraviglaire", "meravigliato",
        "mescolato",
        "mischiato",
        "oscuro",
        "particolare",
        "sbalestrato",
        "sbalordimento", "sbalordire", "sbalordito", "sbalorditivo",
        "sbigottimento", "sbigottire", "sbigottito",
        "sbilanciato",
        "scioccato", "scioccare",
        "sconcerto", "sconcertare", "sconcertato", "sconcertante", "sconcertantemente",
        "sconnesso", "sconnessamente",
        "sgomento", "sgomentare", "sgomentato",
        "singolarità", "singolare",
        "sorprendimento", "sorpresa", "sorprendente", "sorprendentemente", "sorprendere",
        "sottosopra",
        "squilibrato",
        "stralunato",
        "strambo",
        "strampalato",
        "strano", "stranamente",
        "stupefazione", "stupefatto", "stupefare", "stupefacente",
        "stupore", "stupire", "stupito",
        "trasecolato", "trasecolare",
        "vago", "vagamente",
    ],
    JOY: [
        "accettazione",
        "adorazione", "adorare", "adorevole", "adorato",
        "affabilità", "affabile", "affabilmente",
        "affettuoso", "affettuosamente",
        "affinità",
        "allegro", "allegramente",
        "appagamento", "appagare", "appagato", "appagante",
        "beatitudine", "beato",
        "bene",
        "benevolenza",
        "caloroso", "calorosamente",
        "capriccio", "capriccioso", "capricciosamente",
        "compiacimento", "compiacenza", "compiacere", "compiaciuto", "compiaciutamente",
        "contentezza", "contento",
        "desiderio", "desiderare", "desiderato",
        "devozione", "devoto", "devotamente",
        "diletto",
        "divertimento", "divertire", "divertito",
        "eccitato", "eccitare", "eccitante",
        "entusiasmo",
        "esaltazione", "esaltare", "esaltato",
        "espansivo",
        "estasi", "estasiare", "estasiato",
        "euforico", "euforicamente",
        "felicità", "felice", "felicemente",
        "festoso", "festosamente",
        "fiducioso", "fiducia", "fiduciosamente",
        "fierezza", "fiero", "fieramente",
        "gaiezza", "gaio",
        "gioia", "gioire", "gioioso", "gioiosamente",
        "gioviale",
        "godimento", "godere", "goduto", "gaudente",
        "gratificazione", "gratificare", "gratificato", "gratificante",
        "infatuazione", "infatuare", "infatuato",
        "interesse", "interessare", "interessato", "interessante",
        "lieto", "lietamente",
        "ottimista", "ottimistico",
        "piacere",
        "quiete", "quietezza", "quietitudine", "quieto"
        "sereno", "serenità", "serenamente",
        "soddisfazione", "soddisfacimento", "soddisfare", "soddisfacente", "soddisfatto",
        "sollevato",
        "sollievo",
        "spensierato", "spensieratamente",
        "speranza", "speranzoso", "speranzosamente",
        "tenerezza", "tenero",
    ],
    CONTEMPT: [
        "aborrimento", "aborrire", "aborrevole", "aborrevolmente",
        "avversione", "avversare", "avverso",
        "disprezzo", "disprezzare", "disprezzato",
        "sdegno", "sdegnosità", "sdegnare", "sdegnato", "sdegnoso", "sdegnosamente", "sdegnatamente",
    ],
    DISGUST: [
        "disgusto", "disgustare", "disgustato", "disgustosamente",
        "fastidio", "fastidiosità", "fastidiosamente", "fastidioso",
        "infastidire", "infastidito",
        "inorridito", "inorridire",
        "nausea", "nauseare", "nauseato",
        "repulsione",
        "ribrezzo",
        "ripugnanza", "ripugnare", "ripugnato", "ripugnante",
        "rivoltato",
        "scandalizzare", "scandalizzato",
        "schifo", "schifare", "schifato", "schifiltoso",
        "stomachevolezza", "stomachevole", "stomacare", "stomacato",
        "urtare", "urtato",
        "voltastomaco",
    ],
    FEAR: [
        "agitazione", "agitare", "agitato",
        "allarme", "allarmare", "allarmato", "allarmante",
        "ansia", "ansioso", "ansiosamente",
        "apprensione", "apprensivo",
        "atterrimento", "atterrire", "atterrito",
        "cautela",
        "chiuso",
        "diffidenza", "diffidare", "diffidente",
        "dubbio", "dubbiosità", "dubbioso", "dubbiosamente",
        "esitazione", "esitare", "esitante",
        "fobia",
        "goffo", "goffamente",
        "impacciato", "impacciatamente",
        "impaurire", "impaurito",
        "incerto",
        "innervosimento", "innervosire", "innervosito",
        "inquieto",
        "insicuro",
        "intimorimento", "intimorire", "intimorito",
        "irrigidimento", "irrigidire", "irrigidito",
        "nervosismo", "nervoso", "nervosetto", "nervosamente",
        "panico",
        "paura", "pauroso", "paurosamente",
        "pavido", "pavidamente",
        "preoccupazione", "preoccupare", "preoccupato",
        "ritroso",
        "sconvolgimento", "sconvolgere", "sconvolto", "sconvolgente",
        "spavento", "spaventare", "spaventato", "spaventosamente",
        "tensione",
        "terrore",
        "teso",
        "timido", "timidamente",
        "timore", "timoroso", "timorosamente",
        "umile", "umilmente",
    ],
    SHAME: [
        "imbarazzo", "imbarazzare", "imbarazzato",
        "mortificazione", "mortificare", "mortificato", "mortificante",
        "rossore", "arrossire", "arrossito",
        "pentimento", "pentire", "pentito",
        "pudicizia", "pudico", "pudicamente",
        "pudore",
        "riguardo",
        "ritegno",
        "umiliazione", "umiliare", "umiliante", "umiliato",
        "vergogna", "vergognare", "vergognato", "vergognosamente",
    ],
}
