---
name: Amazon Lex
description: Amazon Lex is a fully managed artificial intelligence (AI) service with advanced natural language models to design, build, test, and deploy conversational interfaces in applications. It provides the deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, enabling you to build applications with highly engaging user experiences and lifelike conversational interactions.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://apis.io/amazon-lex
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Lex API
    description: The Amazon Lex API provides programmatic access to manage bots, bot aliases, bot channels, intents, slots, and slot types for building conversational AI interfaces and chatbots.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    baseURL: https://models-v2-lex.amazonaws.com
    properties:
      - type: documentation
        url: https://docs.aws.amazon.com/lex/latest/dg/what-is.html
      - type: openapi
        url: openapi/openapi.yml
      - type: openapi
        url: https://api.apis.guru/v2/specs/amazonaws.com/models.lex.v2/latest/openapi.yaml
      - type: json-schema
        url: json-schema/json-schema.yml
      - type: json-ld
        url: json-ld/json-ld.yml
      - type: pricing
        url: https://aws.amazon.com/lex/pricing/
      - type: getting-started
        url: https://aws.amazon.com/lex/getting-started/
      - type: faq
        url: https://aws.amazon.com/lex/faqs/
      - type: JSONSchema
        url: json-schema/amazon-lex-bot-schema.json
      - type: JSONSchema
        url: json-schema/amazon-lex-intent-schema.json
      - type: JSONLD
        url: json-ld/amazon-lex-context.jsonld
common:
  - type: portal
    url: https://aws.amazon.com/
  - type: website
    url: https://aws.amazon.com/lex/
  - type: documentation
    url: https://docs.aws.amazon.com/lex/
  - type: terms-of-service
    url: https://aws.amazon.com/service-terms/
  - type: privacy-policy
    url: https://aws.amazon.com/privacy/
  - type: support
    url: https://aws.amazon.com/premiumsupport/
  - type: blog
    url: https://aws.amazon.com/blogs/machine-learning/
  - type: github
    url: https://github.com/aws
  - type: console
    url: https://console.aws.amazon.com/lex/
  - type: sign-up
    url: https://portal.aws.amazon.com/billing/signup
  - type: login
    url: https://signin.aws.amazon.com/
  - type: status
    url: https://health.aws.amazon.com/health/status
  - type: knowledge-center
    url: https://repost.aws/knowledge-center
  - type: youtube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: stack-overflow
    url: https://stackoverflow.com/questions/tagged/amazon-lex
  - type: contact
    url: https://aws.amazon.com/contact-us/
  - type: security
    url: https://aws.amazon.com/security/
  - type: compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Automatic Speech Recognition
        description: Convert speech to text with high accuracy using the same deep learning technology as Amazon Alexa.
      - name: Natural Language Understanding
        description: Understand the intent behind user input to build conversational interfaces.
      - name: Multi-Channel Deployment
        description: Deploy bots across web, mobile, messaging channels (Slack, Facebook Messenger, Twilio), and contact centers.
      - name: Amazon Connect Integration
        description: Build intelligent contact center bots with native integration with Amazon Connect.
      - name: Streaming Conversations
        description: Support multi-turn streaming conversations for complex dialog flows.
      - name: Intent Recognition
        description: Recognize user intents and extract slot values from natural language input.
  - type: UseCases
    data:
      - name: Customer Service Chatbot
        description: Build self-service chatbots for customer support and FAQ handling.
      - name: Contact Center Automation
        description: Automate contact center interactions with intelligent IVR and agent assist.
      - name: Internal Help Desk
        description: Create employee-facing bots for IT help desk and HR self-service.
      - name: E-Commerce Assistant
        description: Build shopping assistants that understand natural language product queries.
  - type: Integrations
    data:
      - name: Amazon Connect
        description: Deploy Lex bots in Amazon Connect contact flows for IVR and agent assist.
      - name: Amazon Kendra
        description: Combine Lex for dialog management with Kendra for intelligent document search.
      - name: AWS Lambda
        description: Use Lambda for fulfillment logic and business rules in bot conversations.
      - name: Amazon Polly
        description: Convert bot text responses to natural speech using Amazon Polly TTS.
  - type: SpectralRules
    url: rules/amazon-lex-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-lex-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-lex-vocabulary.yaml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
