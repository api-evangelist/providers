---
aid: xiaomi
url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/apis.yml
name: Xiaomi
tags:
  - Consumer Electronics
  - IoT
  - Smart Home
  - Mobile
  - Artificial Intelligence
  - Cloud Storage
  - Machine Learning
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-25'
modified: '2026-05-03'
position: Consumer
description: Xiaomi is a multinational technology company headquartered in Beijing, China, that designs, develops, and sells a wide range of consumer electronics and related software services. The company is known for its smartphones, laptops, smart home devices, and other innovative products. Xiaomi offers developer APIs for IoT device control, cloud storage (Galaxy FDS), account/identity (Open API), machine learning (Cloud-ML), and AI language models (MiMo).
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: xiaomi:xiaomi-open-api
    name: Xiaomi Open API
    description: The Xiaomi Open API provides OAuth 2.0 based access to user profile data, contact information, friend lists, and identity verification for Xiaomi account holders. It enables third-party applications to integrate Xiaomi account authentication and access authorized user data.
    humanURL: https://dev.mi.com/docs/passport/en/open-api/
    baseURL: https://open.account.xiaomi.com
    tags:
      - Identity
      - OAuth
      - Authentication
      - User Profile
    properties:
      - type: Documentation
        url: https://dev.mi.com/docs/passport/en/open-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/openapi/xiaomi-open-api-openapi.yml
    contact:
      - FN: Xiaomi Developer
        url: https://dev.mi.com/
  - aid: xiaomi:xiaomi-galaxy-fds
    name: Xiaomi Galaxy FDS API
    description: Xiaomi Galaxy File Data Storage (FDS) is a cloud object storage service offering a RESTful API for storing, retrieving, and managing objects and buckets. It supports multipart uploads, access control lists, object lifecycle operations, and CDN prefetch/refresh capabilities.
    humanURL: https://docs.api.xiaomi.com/en/fds/
    baseURL: https://cnbj0.fds.api.xiaomi.com
    tags:
      - Cloud Storage
      - Object Storage
      - File Storage
    properties:
      - type: Documentation
        url: https://docs.api.xiaomi.com/en/fds/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/openapi/xiaomi-galaxy-fds-openapi.yml
  - aid: xiaomi:xiaomi-mimo-api
    name: Xiaomi MiMo AI API
    description: The Xiaomi MiMo AI API provides OpenAI-compatible access to Xiaomi's MiMo large language models, including reasoning, coding, multimodal, and text-to-speech variants. Developers can use the API for chat completions with models such as mimo-v2.5-pro, mimo-v2.5, mimo-v2-omni, and mimo-v2-flash.
    humanURL: https://platform.xiaomimimo.com/
    baseURL: https://api.xiaomimimo.com
    tags:
      - Artificial Intelligence
      - Language Models
      - Chat Completions
      - Machine Learning
    properties:
      - type: Documentation
        url: https://platform.xiaomimimo.com/docs/api/chat/openai-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/openapi/xiaomi-mimo-api-openapi.yml
common:
  - type: Website
    url: https://www.mi.com
  - type: Developer Portal
    url: https://dev.mi.com
  - type: GitHub Organization
    url: https://github.com/XiaoMi
  - type: SDK
    url: https://github.com/XiaoMi/galaxy-fds-sdk-python
  - type: SDK
    url: https://github.com/XiaoMi/cloud-ml-sdk
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/json-schema/xiaomi-user-profile-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/json-schema/xiaomi-chat-completion-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/json-ld/xiaomi-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/xiaomi/refs/heads/main/vocabulary/xiaomi-vocabulary.yml
---
