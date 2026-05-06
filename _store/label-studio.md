---
aid: label-studio
url: https://raw.githubusercontent.com/api-evangelist/label-studio/refs/heads/main/apis.yml
name: Label Studio
type: Index
tags:
  - AI
  - Annotation
  - Artificial Intelligence
  - Data Labeling
  - LLM
  - Machine Learning
  - Open Source
created: '2025-02-08'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
description: Label Studio is the most flexible open-source data labeling platform from HumanSignal, used to fine-tune LLMs, prepare training data, and validate AI models. The Label Studio REST API exposes projects, tasks, annotations, predictions, storage, webhooks, prompts, and review workflows.
apis:
  - aid: label-studio:label-studio
    name: Label Studio
    tags:
      - AI
      - Annotation
      - Data Labeling
      - LLM
      - Machine Learning
      - Open Source
      - REST
    image: https://raw.githubusercontent.com/api-evangelist/label-studio/refs/heads/main/image.png
    humanURL: https://labelstud.io/
    baseURL: https://app.humansignal.com/api
    description: 'The Label Studio REST API supports the full data labeling lifecycle: managing projects, tasks, annotations, annotation reviews, comments, predictions, ML backends, prompts, storage (S3 / Azure / GCS), webhooks, users, organizations, and analytics. The OpenAPI 3.1 specification is published by HumanSignal at https://api.labelstud.io/openapi.yaml.'
    properties:
      - url: https://labelstud.io/
        type: Documentation
      - url: https://api.labelstud.io/
        type: API Reference
      - url: openapi/label-studio-openapi.yml
        type: OpenAPI
      - url: https://github.com/HumanSignal/label-studio
        type: SourceCode
      - url: https://labelstud.io/community
        type: Community
common:
  - url: https://labelstud.io/
    type: Website
  - url: https://api.labelstud.io/
    type: Documentation
  - url: https://github.com/HumanSignal/label-studio
    type: SourceCode
  - url: https://labelstud.io/blog
    type: Blog
  - url: https://humansignal.com/privacy/
    type: Privacy Policy
  - url: https://humansignal.com/terms/
    type: Terms of Service
  - url: https://labelstud.io/community
    type: Community
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
