---
aid: gremlin
name: Gremlin
description: Gremlin is a chaos engineering platform that helps teams build more resilient systems by running controlled failure experiments. It provides tools to simulate infrastructure failures, network issues, and resource exhaustion to identify and fix weaknesses before they cause real outages.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.gremlin.com
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Chaos Engineering
  - Fault Injection
  - Infrastructure Testing
  - Reliability
  - Site Reliability Engineering
apis:
  - aid: gremlin:gremlin-api
    name: Gremlin API
    description: The Gremlin Failure-as-a-Service API for programmatically running chaos engineering attacks, scenarios, reliability tests, disaster recovery experiments, and managing teams, integrations, and infrastructure targets across cloud, container, and Kubernetes environments.
    humanURL: https://www.gremlin.com/docs
    baseURL: https://api.gremlin.com/v1
    tags:
      - Chaos Engineering
      - Fault Injection
      - Reliability
    properties:
      - type: Documentation
        url: https://www.gremlin.com/docs
      - type: OpenAPI
        url: openapi/gremlin-openapi.yml
      - type: Capabilities
        url: capabilities/gremlin-capabilities.yml
      - type: Rules
        url: rules/gremlin-rules.yml
      - type: JSONSchema
        url: json-schema/gremlin-schema-index.yml
common:
  - type: Portal
    url: https://www.gremlin.com
  - type: Documentation
    url: https://www.gremlin.com/docs
  - type: Getting Started
    url: https://www.gremlin.com/docs/getting-started
  - type: Authentication
    url: https://www.gremlin.com/docs/api-reference
  - type: Pricing
    url: https://www.gremlin.com/pricing
  - type: Terms of Service
    url: https://www.gremlin.com/terms
  - type: Privacy Policy
    url: https://www.gremlin.com/privacy
  - type: Support
    url: https://www.gremlin.com/support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
