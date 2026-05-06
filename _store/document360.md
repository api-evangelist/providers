---
aid: document360
name: Document360
description: Document360 is a SaaS knowledge base platform that allows teams to create, manage, and publish self-service knowledge bases and documentation portals. It supports version control, categories, team collaboration, analytics, and an API for integrating documentation into external workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Documentation
  - Knowledge Base
  - SaaS
url: https://raw.githubusercontent.com/api-evangelist/document360/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: document360:document360-api
    name: Document360 API
    description: The Document360 API provides programmatic access to manage knowledge base projects, articles, categories, drives, files, users, and teams. It enables integrating Document360 documentation workflows into CI/CD pipelines and external applications.
    humanURL: https://apidocs.document360.com/
    baseURL: https://apihub.document360.io/v2
    tags:
      - Documentation
      - Knowledge Base
    properties:
      - type: Documentation
        url: https://apidocs.document360.com/
      - type: Getting Started
        url: https://document360.com/blog/document360-api/
      - type: OpenAPI
        url: openapi/document360-document360-api-openapi.yml
      - type: JSON Schema
        url: json-schema/document360-article-schema.json
      - type: JSON Schema
        url: json-schema/document360-category-schema.json
      - type: JSON-LD
        url: json-ld/document360-context.jsonld
common:
  - type: Portal
    url: https://document360.com/
  - type: Documentation
    url: https://apidocs.document360.com/
  - type: Pricing
    url: https://document360.com/pricing/
  - type: Blog
    url: https://document360.com/blog/
  - type: Terms of Service
    url: https://document360.com/terms-of-service/
  - type: Privacy Policy
    url: https://document360.com/privacy-policy/
  - type: Support
    url: https://support.document360.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
