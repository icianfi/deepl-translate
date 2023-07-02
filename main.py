from fastapi import FastAPI
import deepl

supported_sources = {'BG', 'CS', 'DA', 'DE', 'EL', 'EN', 'ES', 'ET', 'FI', 'FR', 'HU', 'ID', 'IT', 'JA', 'KO', 'LT',
                     'LV', 'NB', 'NL', 'PL', 'PT', 'RO', 'RU', 'SK', 'SL', 'SV', 'TR', 'UK', 'ZH', None}

supported_targets = {'BG', 'DA', 'CS', 'DE', 'EL', 'EN', 'EN-GB', 'EN-US', 'ES', 'ET', 'FI', 'FR', 'HU', 'ID', 'IT',
                     'JA', 'KO', 'LT', 'LV', 'NB', 'NL', 'PL', 'PT', 'PT-BR', 'PT-PT', 'RO', 'RU', 'SK', 'SL', 'SV',
                     'TR', 'UK', 'ZH'}
app = FastAPI()
auth_key = ''
translator = deepl.Translator(auth_key)


def is_language_supported(language, supported_languages):
    if language not in supported_languages:
        return False
    return True


@app.get("/translate")
async def translate(target: str, text: str, source: str = None):
    """
    Endpoint to translate text using Deepl
    """
    if not is_language_supported(source, supported_sources):
        return {'error': f'Source language {source} is not supported.'}
    if not is_language_supported(target, supported_targets):
        return {'error': f'Target language {target} is not supported.'}
    translated = translator.translate_text(text, source_lang=source, target_lang=target)
    return {"translated": f"{translated}"}
