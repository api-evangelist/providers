---
aid: eventuate
name: Eventuate
description: Eventuate is a platform for developing transactional microservices using event sourcing and CQRS patterns, providing frameworks for managing distributed data consistency across services without two-phase commit.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CQRS
  - Distributed Data
  - Event Sourcing
  - Event-Driven
  - Microservices
  - Sagas
url: https://raw.githubusercontent.com/api-evangelist/eventuate/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-03-26'
specificationVersion: '0.19'
apis:
  - aid: eventuate:eventuate
    name: Eventuate
    description: Eventuate is a platform for developing transactional microservices using event sourcing and CQRS patterns, enabling reliable communication and data consistency across distributed services using the Saga pattern and transactional outbox.
    humanURL: https://eventuate.io/
    tags:
      - CQRS
      - Distributed Data
      - Event Sourcing
      - Event-Driven
      - Microservices
      - Sagas
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/eventuate/refs/heads/main/openapi/eventuate-api.yml
common:
  - type: Website
    url: https://eventuate.io/
  - type: Documentation
    url: https://eventuate.io/docs/general/getting-started.html
  - type: Getting Started
    url: https://eventuate.io/exampleapps.html
  - type: GitHub
    url: https://github.com/eventuate-tram
  - type: Blog
    url: https://eventuate.io/news.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
