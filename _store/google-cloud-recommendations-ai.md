---
name: Google Cloud Recommendations AI
description: Google Cloud Recommendations AI delivers personalized product recommendations at scale. It uses machine learning to understand customer behavior and product catalog data to generate highly relevant recommendations for retail and e-commerce use cases including product discovery, related items, and frequently bought together.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-recommendations-ai/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - E-Commerce
  - Google Cloud
  - Machine Learning
  - Personalization
  - Recommendations
  - Retail
apis:
  - name: Google Cloud Recommendations AI API
    description: Delivers personalized product recommendations at scale using machine learning, supporting catalog management, user event ingestion, and real-time prediction serving for retail and e-commerce.
    humanURL: https://cloud.google.com/recommendations-ai
    baseURL: https://recommendationengine.googleapis.com
    tags:
      - Personalization
      - Recommendations
      - Retail
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/catalog-item.json
      - type: JSONLD
        url: json-ld/context.jsonld
common:
  - type: GettingStarted
    url: https://cloud.google.com/recommendations-ai/docs/overview
  - type: Pricing
    url: https://cloud.google.com/recommendations-ai/pricing
  - type: JSONLD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
