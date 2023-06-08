# Translation and Transcription language choices
LANGUAGE_CHOICES = [
    ("en", "English"),
    ("hi", "Hindi"),
    ("as", "Assamese"),
    ("bn", "Bengali"),
    ("brx", "Bodo"),
    ("doi", "Dogri"),
    ("gu", "Gujarati"),
    ("kn", "Kannada"),
    ("ks", "Kashmiri"),
    ("gom", "Konkani"),
    ("mai", "Maithili"),
    ("ml", "Malayalam"),
    ("mr", "Marathi"),
    ("mni", "Manipuri"),
    ("ne", "Nepali"),
    ("or", "Oriya"),
    ("pa", "Punjabi"),
    ("sa", "Sanskrit"),
    ("sat", "Santali"),
    ("sd", "Sindhi"),
    ("si", "Sinhala"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("ur", "Urdu"),
]

# Indic Trans API supported languages
INDIC_TRANS_SUPPORTED_LANGUAGES = {
    "Assamese": "as",
    "Bengali": "bn",
    "English": "en",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Oriya": "or",
    "Punjabi": "pa",
    "Tamil": "ta",
    "Telugu": "te",
}

LANG_NAME_TO_CODE = {
    "English": "en",
    "Assamese": "as",
    "Bhojpuri": "bho",
    "Bengali": "bn",
    "Bodo": "brx",
    "Dogri": "doi",
    "Dhivehi": "dv",
    "Konkani": "gom",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Kashmiri": "ks",
    "Mizo": "lus",
    "Maithili": "mai",
    "Malayalam": "ml",
    "Manipuri": "mni",
    "Marathi": "mr",
    "Nepali": "ne",
    "Odia": "or",
    "Punjabi": "pa",
    "Sanskrit": "sa",
    "Santali": "sat",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
}

LANG_CODE_TO_NAME = {
    lang_code: lang_name for lang_name, lang_code in LANG_NAME_TO_CODE.items()
}
