---
aid: fashn
name: FASHN AI
description: FASHN AI is an AI-first company specializing in human-centric generative image models tailored for fashion applications. The public API offers an asynchronous prediction workflow against a catalog of models including Try-On Max, Product to Model, Face to Model, Model Create, Model Swap, Edit, Reframe, Image to Video, and Background Remove.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
tags:
  - AI
  - Clothing
  - Fashion
  - Virtual Try-On
url: https://raw.githubusercontent.com/api-evangelist/fashn/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fashn:fashn
    name: FASHN
    tags:
      - Clothing
      - Fashion
      - AI
      - Virtual Try-On
    humanURL: https://fashn.ai/products/api
    baseURL: https://api.fashn.ai/v1
    properties:
      - url: https://fashn.ai/products/api
        type: Documentation
      - url: https://docs.fashn.ai/
        type: API Documentation
      - url: https://docs.fashn.ai/api-overview/api-fundamentals
        type: API Reference
      - url: https://app.fashn.ai/api
        type: Developer Portal
      - url: https://raw.githubusercontent.com/api-evangelist/fashn/refs/heads/main/openapi/fashn-openapi.yml
        type: OpenAPI
    description: 'The FASHN API is an asynchronous prediction service. Clients POST to /v1/run with a model_name and model-specific inputs, then poll /v1/status/{id} until the prediction completes. Authentication uses a Bearer token. Rate limits: 50 req/60s on /run, 50 req/10s on /status, 6 concurrent predictions. CDN outputs are retained for 72 hours.'
common:
  - type: Website
    url: https://fashn.ai/
  - type: Documentation
    url: https://fashn.ai/products/api
  - type: API Documentation
    url: https://docs.fashn.ai/
  - type: Developer Portal
    url: https://app.fashn.ai/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
