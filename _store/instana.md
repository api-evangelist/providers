---
aid: instana
name: Instana
description: Instana is an enterprise observability and application performance monitoring platform that provides automated full-stack visibility and AI-powered APM. Instana offers a public REST API for programmatic access to monitoring data, configurations, and integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APM
  - Infrastructure
  - Monitoring
  - Observability
url: https://raw.githubusercontent.com/api-evangelist/instana/refs/heads/main/apis.yml
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: instana:instana-api
    name: Instana API
    description: The Instana REST API provides programmatic access to the Instana observability platform, enabling integration with monitoring data, events, alerts, and infrastructure configuration.
    humanURL: https://www.ibm.com/docs/en/instana-observability/current?topic=apis-rest-api
    tags:
      - APM
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://instana.github.io/openapi/
      - type: OpenAPI
        url: openapi/instana-openapi.yml
      - type: GitHub Organization
        url: https://github.com/instana/openapi
common:
  - type: Website
    url: https://www.ibm.com/products/instana
  - type: Documentation
    url: https://www.ibm.com/docs/en/instana-observability/current
  - type: Support
    url: https://www.ibm.com/mysupport
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
