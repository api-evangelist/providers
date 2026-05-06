---
aid: bot-butcher
url: https://raw.githubusercontent.com/api-evangelist/bot-butcher/refs/heads/main/apis.yml
name: Bot Butcher
tags:
  - Bots
  - Spam Detection
  - Contact Forms
  - AI Classification
  - Security
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-07'
modified: '2026-04-21'
position: Consuming
description: Bot Butcher is an AI-powered spam detection API that uses a fine-tuned large language model to classify contact form submissions as spam or legitimate messages. The service analyzes messages within the context of what each website is about, providing context-aware classification with 99% reported accuracy. It supports multi-tenant architectures and is designed for enterprise scalability across vertical SaaS and website builder platforms.
apis:
  - aid: bot-butcher:bot-butcher-classification-api
    name: Bot Butcher Classification API
    tags:
      - Spam Detection
      - Bot Detection
      - AI Classification
      - Contact Forms
    humanURL: https://botbutcher.com/
    properties:
      - url: https://botbutcher.com/
        type: Documentation
    description: Submit contact form data to Bot Butcher and receive a JSON classification result indicating whether the message is spam or legitimate. The AI model classifies each message within the context of your specific website, delivering context-aware spam detection for multi-tenant and enterprise applications.
    contact:
      - FN: Bot Butcher Support
        url: https://botbutcher.com/
common:
  - type: Website
    url: https://botbutcher.com/
  - type: Documentation
    url: https://botbutcher.com/
properties:
  - type: x-domain
    value: botbutcher.com
  - type: x-industry
    value: Cybersecurity, Spam Detection
  - type: x-authentication
    value: API Key
  - type: x-classification-model
    value: Fine-tuned Large Language Model (LLM)
  - type: x-accuracy
    value: 99% against benchmark test
  - type: x-features
    value: Spam classification, message retrieval by message_id, optional message storage, Do Not Train mode, Do Not Save mode, multi-tenant support, unlimited websites, context-aware classification
  - type: x-use-cases
    value: Contact form spam filtering, enterprise SaaS spam protection, multi-tenant application security, website builder platform integration
  - type: x-response-format
    value: JSON
  - type: x-workflow
    value: 1. POST contact form data to Bot Butcher endpoint, 2. AI classifies message as spam or not spam, 3. Receive JSON result, 4. Optionally retrieve message by message_id
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
