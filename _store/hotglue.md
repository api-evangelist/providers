---
aid: hotglue
name: Hotglue
description: Hotglue is an embedded iPaaS platform that enables SaaS products to offer native integrations to their customers. Built on the Python ecosystem, it provides a code-first approach with over 600 open-source connectors, a CLI for programmatic configuration management, detailed job logs, webhooks, and observability integrations. Hotglue allows developers to build flexible, scalable integrations without the lock-in of traditional iPaaS tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Connectors
  - Embedded Integrations
  - ETL
  - Integration Platform
  - iPaaS
url: https://raw.githubusercontent.com/api-evangelist/hotglue/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hotglue:hotglue-api-v2
    name: Hotglue API V2
    description: The Hotglue API v2 enables programmatic management of embedded integrations including linked connectors, flow configurations, job execution, tenant management, and connector state for SaaS product integrations.
    humanURL: https://docs.hotglue.com/api-reference/v2
    baseURL: https://api.hotglue.com
    tags:
      - Connectors
      - Embedded Integrations
      - ETL
      - Integration Platform
    properties:
      - type: Documentation
        url: https://docs.hotglue.com/
      - type: APIReference
        url: https://docs.hotglue.com/api-reference/v2
      - type: GettingStarted
        url: https://docs.hotglue.com/getting-started
      - type: OpenAPI
        url: openapi/hotglue-openapi.yml
  - aid: hotglue:hotglue-api-v1
    name: Hotglue API V1
    description: The Hotglue API v1 provides the original REST API for managing integration flows, linked sources, linked targets, source state, and job execution.
    humanURL: https://docs.hotglue.com/api-reference/v1/introduction
    baseURL: https://api.hotglue.com
    tags:
      - Embedded Integrations
      - Integration Platform
    properties:
      - type: Documentation
        url: https://docs.hotglue.com/api-reference/v1/introduction
common:
  - type: Website
    url: https://hotglue.com/
  - type: Documentation
    url: https://docs.hotglue.com/
  - type: Pricing
    url: https://hotglue.com/pricing
  - type: Blog
    url: https://hotglue.com/blog/
  - type: Connectors
    url: https://hotglue.com/connectors/
  - type: SignUp
    url: https://hotglue.com/signup
  - type: Login
    url: https://hotglue.com/login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
