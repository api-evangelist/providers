---
aid: salesforce-einstein
url: https://raw.githubusercontent.com/api-evangelist/salesforce-einstein/refs/heads/main/apis.yml
apis:
- name: Einstein Vision API
  description: Image recognition and classification API for building custom AI-powered image recognition models.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-vision.png
  humanURL: https://www.salesforce.com/products/einstein/ai-deep-dive/image-recognition/
  baseURL: https://api.einstein.ai/v2/vision
  tags:
  - Computer Vision
  - Image Recognition
  - Machine Learning
  properties:
  - type: Documentation
    url: https://metamind.readme.io/docs/intro-to-einstein-vision
  - type: OpenAPI
    url: https://api.einstein.ai/v2/vision/openapi.json
  - type: Authentication
    url: https://metamind.readme.io/docs/generate-oauth-token
  - type: Pricing
    url: https://www.salesforce.com/products/einstein/pricing/
  - type: SignUp
    url: https://api.einstein.ai/signup
  - type: OpenAPI
    url: openapi/salesforce-einstein-vision-openapi.yml
- name: Einstein Language API
  description: Natural language processing API for sentiment analysis, intent detection, and text classification.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-language.png
  humanURL: https://www.salesforce.com/products/einstein/ai-deep-dive/natural-language-processing/
  baseURL: https://api.einstein.ai/v2/language
  tags:
  - Machine Learning
  - Natural Language Processing
  - Sentiment Analysis
  - Text Classification
  properties:
  - type: Documentation
    url: https://metamind.readme.io/docs/intro-to-einstein-language
  - type: OpenAPI
    url: https://api.einstein.ai/v2/language/openapi.json
  - type: Authentication
    url: https://metamind.readme.io/docs/generate-oauth-token
  - type: Pricing
    url: https://www.salesforce.com/products/einstein/pricing/
  - type: OpenAPI
    url: openapi/salesforce-einstein-language-openapi.yml
- name: Einstein Prediction Builder API
  description: Create custom AI predictions on Salesforce data without code using Einstein AI.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/prediction-builder.png
  humanURL: https://help.salesforce.com/s/articleView?id=sf.einstein_prediction_builder.htm
  baseURL: https://[instance].salesforce.com/services/data/v58.0/einstein/
  tags:
  - CRM
  - Machine Learning
  - No-Code
  - Predictive Analytics
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/einstein_prediction_builder.htm
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: OpenAPI
    url: openapi/salesforce-einstein-prediction-builder-openapi.yml
- name: Einstein Discovery API
  description: Advanced analytics and automated insights API for predicting outcomes and recommending actions.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-discovery.png
  humanURL: https://www.salesforce.com/products/einstein/features/
  baseURL: https://[instance].salesforce.com/services/data/v58.0/analytics/
  tags:
  - Automated Insights
  - Business Intelligence
  - Machine Learning
  - Predictive Analytics
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_rest_overview.htm
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: OpenAPI
    url: openapi/salesforce-einstein-discovery-openapi.yml
- name: Einstein Bots API
  description: Conversational AI API for building intelligent chatbots and virtual assistants.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-bots.png
  humanURL: https://www.salesforce.com/products/service-cloud/features/chatbots/
  baseURL: https://[instance].salesforce.com/services/data/v58.0/einstein/
  tags:
  - Chatbots
  - Conversational AI
  - Customer Service
  - Natural Language Processing
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/service/einstein-bots/guide/einstein-bots-developer-overview.html
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  - type: Setup Guide
    url: https://help.salesforce.com/s/articleView?id=sf.bots_service_intro.htm
  - type: OpenAPI
    url: openapi/salesforce-einstein-bots-openapi.yml
- name: Einstein GPT API
  description: Generative AI API powered by OpenAI integration for creating personalized content across Salesforce.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-gpt.png
  humanURL: https://www.salesforce.com/einstein-gpt/
  baseURL: https://[instance].salesforce.com/services/data/v58.0/einstein/
  tags:
  - Content Generation
  - Generative AI
  - GPT
  - Large Language Models
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/einstein/genai/overview
  - type: Announcement
    url: https://www.salesforce.com/news/press-releases/2023/03/07/einstein-gpt/
  - type: Trust & Safety
    url: https://www.salesforce.com/company/ethical-and-humane-use/
  - type: OpenAPI
    url: openapi/salesforce-einstein-gpt-openapi.yml
name: Salesforce Einstein
tags:
- Artificial Intelligence
- Computer Vision
- CRM
- Machine Learning
- Natural Language Processing
- Predictive Analytics
- Salesforce
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of Salesforce Einstein AI and machine learning APIs for predictive analytics, natural language processing, computer vision, and intelligent automation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

