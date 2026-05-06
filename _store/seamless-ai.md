---
aid: seamless-ai
url: https://raw.githubusercontent.com/api-evangelist/seamless-ai/refs/heads/main/apis.yml
apis:
  - aid: seamless-ai:seamless-ai-contacts-api
    name: Seamless.AI Contacts API
    tags:
      - Contacts
      - Sales Intelligence
      - B2B
      - Prospecting
    humanURL: https://docs.seamless.ai/
    baseURL: https://api.seamless.ai
    properties:
      - url: openapi/seamless-ai-contacts-openapi.yml
        type: OpenAPI
      - url: https://docs.seamless.ai/
        type: Documentation
    description: The Seamless.AI Contacts API provides programmatic access to contact search, enrichment, and research capabilities. Search for B2B contacts by name, company, title, and location. Enrich existing contact records with emails, phone numbers, and job history. Access job-change intelligence to identify contacts that have recently changed roles.
  - aid: seamless-ai:seamless-ai-companies-api
    name: Seamless.AI Companies API
    tags:
      - Companies
      - Firmographics
      - Sales Intelligence
      - B2B
    humanURL: https://docs.seamless.ai/
    baseURL: https://api.seamless.ai
    properties:
      - url: openapi/seamless-ai-companies-openapi.yml
        type: OpenAPI
      - url: https://docs.seamless.ai/
        type: Documentation
    description: The Seamless.AI Companies API enables programmatic search and research of company data including firmographics, revenue, employee count, technology stack, and company intelligence. Use company search result IDs or direct identifiers such as domain or company name to retrieve comprehensive company profiles.
name: Seamless.AI
tags:
  - B2B
  - Contact Data
  - Sales Intelligence
  - Prospecting
  - Lead Generation
  - CRM Enrichment
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consuming
description: Seamless.AI is a B2B sales intelligence platform that provides real-time contact and company data to help sales teams find and connect with their ideal customers. The platform uses artificial intelligence to continuously verify and update contact information including emails, direct dials, and mobile numbers. Seamless.AI offers a RESTful API secured with OAuth 2.0 and API key authentication, enabling developers to integrate contact search, company search, enrichment, and job-change intelligence directly into CRM systems, marketing platforms, and internal sales tools.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Website
    url: https://seamless.ai
    type: Website
  - name: API Documentation
    url: https://docs.seamless.ai/
    type: Documentation
  - name: API Overview
    url: https://seamless.ai/products/api
    type: Overview
  - name: Getting Started
    url: https://seamless.ai/customers/education/articles/seamless-ai-api-overview
    type: GettingStarted
  - name: API Terms Glossary
    url: https://seamless.ai/customers/education/articles/api-terms-glossary
    type: Glossary
  - name: CRM Enrichment
    url: https://seamless.ai/news/releases/api
    type: Blog
  - url: json-schema/seamless-ai-contact-schema.json
    type: JSONSchema
  - url: json-schema/seamless-ai-company-schema.json
    type: JSONSchema
  - url: json-structure/seamless-ai-contact-structure.json
    type: JSONStructure
  - url: json-ld/seamless-ai-context.jsonld
    type: JSONLDContext
  - url: examples/seamless-ai-search-contacts-example.json
    type: Example
  - url: rules/seamless-ai-rules.yml
    type: SpectralRuleset
  - url: capabilities/sales-prospecting.yaml
    type: NaftikoCapability
  - url: vocabulary/seamless-ai-vocabulary.yml
    type: Vocabulary
---
