---
aid: microsoft-cognitive-services
url: https://raw.githubusercontent.com/api-evangelist/microsoft-cognitive-services/refs/heads/main/apis.yml
name: Microsoft Cognitive Services
description: Microsoft Cognitive Services (Azure AI Services) provides AI APIs for vision, speech, language, and OpenAI model access.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure AI
  - Computer Vision
  - Speech
  - NLP
  - OpenAI
  - Machine Learning
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-cognitive-services:vision
    name: Azure AI Vision API
    description: Image analysis, OCR, spatial analysis, and face detection capabilities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/
    baseURL: https://westus.api.cognitive.microsoft.com/
    tags:
      - Computer Vision
      - Image Analysis
      - OCR
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/
  - aid: microsoft-cognitive-services:speech
    name: Azure AI Speech API
    description: Speech-to-text, text-to-speech, speech translation, and speaker recognition.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/
    baseURL: https://westus.stt.speech.microsoft.com/
    tags:
      - Speech
      - Text to Speech
      - Speech to Text
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/
  - aid: microsoft-cognitive-services:language
    name: Azure AI Language API
    description: Natural language processing including sentiment analysis, entity recognition, and summarization.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/ai-services/language-service/
    baseURL: https://api.cognitive.microsoft.com/
    tags:
      - NLP
      - Text Analytics
      - Language Understanding
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/language-service/
  - aid: microsoft-cognitive-services:openai
    name: Azure OpenAI Service API
    description: REST API access to OpenAI models including GPT-4, DALL-E, and Whisper with enterprise security.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/ai-services/openai/
    baseURL: https://api.cognitive.microsoft.com/
    tags:
      - OpenAI
      - GPT
      - Large Language Models
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/
      - type: API Reference
        url: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/ai-services/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
