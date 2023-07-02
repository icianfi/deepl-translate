# deepl-translate

This is an API built with FastAPI that allows you to translate texts using the deepl library.

## Install

1. Clone this repo:

    ```bash
   git clone https://
   ```

2. Install dependencies:

    ```bash
   pip install -r requirements.txt
   ```

## Usage

Make sure you set you Deepl apikey into `auth_key`

1. Start the API server by executing the following command:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the automatically generated documentation in your browser at the following URL: <http://localhost:8000/docs>
3. Use the API to translate texts:
    * Endpoint: `/translate`
    * Method: GET
    * Params:
      * `text`: The text you wish to translate (required).
      * `source`: The source language of the text (optional, default: `None`).
      * `target`: The target language for the translation (optional).
    * Request example

    ```bash
    GET /translate?text=marca&target=EN-US
    ```

   * Response example

   ```json
   {
    "translated": "brand"
    }
   ```

   Make sure that the source and target languages are in the supported language sets. You can find the list of supported languages in the source code.
