---
aid: hotglue
url: https://raw.githubusercontent.com/api-evangelist/hotglue/refs/heads/main/apis.yml
apis:
- aid: hotglue:hotglue-api-v2
  name: Hotglue API V2
  description: The Hotglue API v2 enables programmatic management of embedded integrations including linked connectors, flow configurations, job execution, tenant management, and sync operations for SaaS product integrations.
  humanURL: https://docs.hotglue.com/api-reference/v2
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
- aid: hotglue:hotglue-api-v1
  name: Hotglue API V1
  description: The Hotglue API v1 provides the original REST API for managing integration flows, connectors, and job execution.
  humanURL: https://docs.hotglue.com/api-reference/v1/introduction
  tags:
  - Embedded Integrations
  - Integration Platform
  properties:
  - type: Documentation
    url: https://docs.hotglue.com/api-reference/v1/introduction
name: Hotglue
tags:
- Connectors
- Embedded Integrations
- ETL
- Integration Platform
- iPaaS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Hotglue is an embedded iPaaS platform that enables SaaS products to offer native integrations to their customers. Built on the Python ecosystem, it provides a code-first approach with over 600 open-source connectors, a CLI for programmatic configuration management, detailed job logs, webhooks, and observability integrations. Hotglue allows developers to build flexible, scalable integrations without the lock-in of traditional iPaaS tools.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

