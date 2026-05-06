---
aid: replicate
name: Replicate
description: Replicate lets you run machine learning models in the cloud with a simple API. Thousands of open-source models are available, and you can run your own custom models at scale. Run image generation, language models, audio synthesis, video generation, and more with a few lines of code. Replicate makes AI accessible to every software engineer.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Machine Learning
  - Image Generation
  - Language Models
  - Model Deployment
url: https://raw.githubusercontent.com/api-evangelist/replicate/refs/heads/main/apis.yml
created: '2024-11-13'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: replicate:replicate
    name: Replicate
    description: Replicate lets you run machine learning models in the cloud with a simple REST API. Access thousands of open-source models for image generation, language modeling, audio synthesis, video generation, upscaling, and more. Create predictions, manage deployments, fine-tune models, and run training jobs via a clean API with webhooks and streaming support.
    humanURL: https://replicate.com/
    tags:
      - Accounts
      - Artificial Intelligence
      - Collections
      - Deployments
      - Hardware
      - Machine Learning
      - Models
      - Predictions
      - Training
      - Webhooks
    properties:
      - url: https://replicate.com/docs
        type: Documentation
      - url: https://replicate.com/docs/reference/http
        type: OpenAPI Documentation
      - url: openapi/replicate-openapi.yml
        type: OpenAPI
      - url: rules/replicate-rules.yml
        type: SpectralRuleset
      - url: capabilities/model-inference.yaml
        type: NaftikoCapability
      - url: capabilities/model-management.yaml
        type: NaftikoCapability
      - url: vocabulary/replicate-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://replicate.com
  - type: Documentation
    url: https://replicate.com/docs
  - type: Pricing
    url: https://replicate.com/pricing
  - type: Blog
    url: https://replicate.com/blog
  - type: ChangeLog
    url: https://replicate.com/changelog
  - type: TermsOfService
    url: https://replicate.com/terms
  - type: PrivacyPolicy
    url: https://replicate.com/privacy
  - type: SignUp
    url: https://replicate.com/signin?next=/docs
  - type: Login
    url: https://replicate.com/signin
  - type: Playground
    url: https://replicate.com/explore
  - type: GitHub Organization
    url: https://github.com/replicate
  - type: SDKs
    url: https://replicate.com/docs/reference/client-libraries
  - type: Python SDK
    url: https://github.com/replicate/replicate-python
  - type: Node.js SDK
    url: https://github.com/replicate/replicate-javascript
  - type: Go SDK
    url: https://github.com/replicate/replicate-go
  - type: Swift SDK
    url: https://github.com/replicate/replicate-swift
  - type: Cog
    url: https://github.com/replicate/cog
  - type: Status
    url: https://status.replicate.com
  - type: Features
    data:
      - T4 GPU at $0.000225/sec (cheapest)
      - L40S GPU at $0.000975/sec
      - A100 80GB at $0.00140/sec
      - H100 at $0.001525/sec (highest performance)
      - Pay only for execution time (per second)
      - Default 10 predictions/sec; can be raised to 100 on paid
      - 'Other endpoints: 60 req/sec'
      - Public model library with thousands of models
      - Cog framework for packaging your own models
      - Deployments for low-latency inference (charges idle time)
      - Webhooks for prediction completion
      - OAuth 2.0 and API tokens
      - Streaming output for LLM models
      - Files input via signed URLs
      - Training service for fine-tuning
      - Trainings billed at hardware rate
    sources:
      - https://replicate.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
