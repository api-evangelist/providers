---
aid: ibm-watson
name: IBM Watson
description: IBM Watson is IBM's AI and machine learning platform offering a suite of cloud-based services including natural language processing, speech recognition, visual recognition, and other AI-powered capabilities for building intelligent applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - IBM
  - Machine Learning
  - Natural Language Processing
  - Speech Recognition
url: https://raw.githubusercontent.com/api-evangelist/ibm-watson/refs/heads/main/apis.yml
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ibm-watson:ibm-watson-speech-to-text
    name: IBM Watson Speech to Text
    description: Convert speech into text using AI-powered speech recognition and transcription. The service uses machine learning to combine knowledge of grammar, language structure, and audio signal composition to accurately transcribe human voice.
    humanURL: https://www.ibm.com/products/speech-to-text
    tags:
      - AI
      - Speech Recognition
      - Transcription
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/speech-to-text
      - type: Getting Started
        url: https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-gettingStarted
  - aid: ibm-watson:ibm-watson-text-to-speech
    name: IBM Watson Text to Speech
    description: Convert written text to natural-sounding audio in a variety of languages and voices. The service synthesizes natural language text to audio using deep learning AI for lifelike speech synthesis.
    humanURL: https://www.ibm.com/products/text-to-speech
    tags:
      - AI
      - Speech Synthesis
      - Text to Speech
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/text-to-speech
      - type: Getting Started
        url: https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-gettingStarted
  - aid: ibm-watson:ibm-watson-natural-language-understanding
    name: IBM Watson Natural Language Understanding
    description: Analyze text to extract metadata from content such as concepts, entities, keywords, categories, sentiment, emotion, relations, and semantic roles.
    humanURL: https://www.ibm.com/products/natural-language-understanding
    tags:
      - AI
      - Natural Language Processing
      - Text Analysis
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/natural-language-understanding
      - type: Getting Started
        url: https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-getting-started
  - aid: ibm-watson:ibm-watson-assistant
    name: IBM Watson Assistant
    description: Build, train, and deploy conversational interactions into any application, device, or channel. Create AI-powered virtual agents that understand natural language and provide helpful responses.
    humanURL: https://www.ibm.com/products/watson-assistant
    tags:
      - Chatbot
      - Conversational AI
      - Virtual Assistant
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/assistant-v2
      - type: Getting Started
        url: https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-getting-started
common:
  - type: Website
    url: https://www.ibm.com/watson
  - type: Portal
    url: https://cloud.ibm.com/developer/watson/
  - type: Documentation
    url: https://cloud.ibm.com/docs/watson
  - type: Getting Started
    url: https://cloud.ibm.com/developer/watson/documentation
  - type: Support
    url: https://www.ibm.com/mysupport
  - type: Pricing
    url: https://www.ibm.com/watson/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
