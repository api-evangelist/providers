---
aid: vlex
name: vLex
description: vLex (part of Clio) is a global legal intelligence platform that applies AI to ingest, enrich, classify, and deliver insights from over 100 million legal documents across 2,000+ multilingual sources. The vLex Iceberg platform provides REST APIs for legal document anonymization, classification, key phrase extraction, citation detection, and AI-powered legal research. vLex also offers the Fastcase Legal Data API for raw legal data feeds.
type: Index
position: Consumer
access: 3rd-Party
image: https://vlex.com/hubfs/vlex-logo.svg
tags:
  - AI
  - Classification
  - Legal Research
  - Legal Tech
  - Natural Language Processing
  - Privacy
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/vlex/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: vlex:iceberg-anonymization-api
    name: vLex Iceberg Anonymization API
    description: Identifies and anonymizes names and personally identifiable information from any text input. Pre-trained on legal data to recognize names, organizations, and sensitive entities within legal documents for privacy protection and data compliance.
    humanURL: https://developer.vlex.com/apis
    tags:
      - Anonymization
      - NLP
      - Privacy
      - Legal Tech
    properties:
      - type: Documentation
        url: https://developer.vlex.com/apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vlex/refs/heads/main/openapi/vlex-iceberg-anonymization-openapi.yml
  - aid: vlex:iceberg-legal-research-api
    name: vLex Iceberg Legal Research API
    description: AI-powered legal research API providing document search, classification, key phrase extraction, citation detection (vCite), and legal entity identification across vLex's corpus of 100+ million legal documents from global jurisdictions.
    humanURL: https://developer.vlex.com/apis
    tags:
      - AI
      - Case Law
      - Citation Detection
      - Classification
      - Legal Research
      - Legal Tech
      - Search
    properties:
      - type: Documentation
        url: https://developer.vlex.com/apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vlex/refs/heads/main/openapi/vlex-iceberg-legal-research-openapi.yml
  - aid: vlex:remote-auth-api
    name: vLex Remote Authentication API
    description: Single sign-on authentication API for corporate vLex accounts. Generates redirect URLs using HMAC authentication for seamless user access to vLex.com from institutional portals.
    humanURL: https://github.com/vlex/remote_auth
    tags:
      - Authentication
      - Single Sign-On
      - SSO
    properties:
      - type: GitHub Repository
        url: https://github.com/vlex/remote_auth
common:
  - url: https://vlex.com/
    type: Website
  - url: https://developer.vlex.com/
    type: Developer Portal
  - url: https://developer.vlex.com/apis
    type: Reference
  - url: https://vlex.com/iceberg-ai
    type: Documentation
  - url: https://developer.vlex.com/use-cases
    type: Use Cases
  - url: https://vlex.com/integrations
    type: Integrations
  - url: https://github.com/vlex
    type: GitHub Organization
  - url: https://vlex.com/products/fastcase
    type: Product
  - url: https://support.vlex.com/
    type: Support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
