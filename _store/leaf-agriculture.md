---
aid: leaf-agriculture
name: Leaf Agriculture
description: Leaf Agriculture is the provider of a unified farm data API. The platform addresses the difficulty of building applications in food and agriculture by providing a standardized API for accessing data from multiple farm data sources, including field boundaries, machine operations (planting, harvest, application, tillage), weather data, provider integrations (John Deere, CNHi, Climate FieldView, Trimble), webhooks for real-time notifications, and Leaf Lake for SQL-based analysis of normalized farm data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Farm Data
  - Field Boundaries
  - Machine Operations
  - Provider Integrations
  - Unified API
  - Weather
  - Webhooks
url: https://raw.githubusercontent.com/api-evangelist/leaf-agriculture/refs/heads/main/apis.yml
created: '2024-07-11'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: leaf-agriculture:leaf-agriculture
    name: Leaf Agriculture API
    description: Leaf Agriculture's unified farm data API for accessing agricultural data from multiple sources and farm management systems. The API provides Bearer-token authentication and exposes endpoints for field management, machine operation files, weather forecasts, provider integrations, and webhook subscriptions.
    humanURL: https://withleaf.io
    tags:
      - Agriculture
      - Farm Data
      - Field Boundaries
      - Machine Operations
      - Weather
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.withleaf.io/
      - type: Getting Started
        url: https://docs.withleaf.io/docs/welcome
      - type: Authentication
        url: https://docs.withleaf.io/docs/authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/leaf-agriculture/refs/heads/main/openapi/leaf-agriculture-openapi.yml
common:
  - type: Website
    url: https://withleaf.io
  - type: Documentation
    url: https://docs.withleaf.io/
  - type: GitHub Organization
    url: https://github.com/Leaf-Agriculture
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
