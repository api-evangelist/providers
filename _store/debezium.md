---
aid: debezium
name: Debezium
description: Debezium is an open source distributed platform for change data capture (CDC) that converts changes in existing databases into event streams, enabling applications to detect and respond to row-level changes in databases in real time.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache Kafka
  - CDC
  - Change Data Capture
  - Databases
  - Event Streaming
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/debezium/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: opensource
apis:
  - aid: debezium:debezium-kafka-connect-api
    name: Debezium Kafka Connect REST API
    description: Debezium runs as Kafka Connect source connectors. This API manages Debezium CDC connectors, their configurations, tasks, and offsets via the standard Kafka Connect REST interface.
    humanURL: https://debezium.io/documentation/reference/stable/connectors/index.html
    baseURL: http://localhost:8083
    tags:
      - CDC
      - Connectors
      - Kafka Connect
      - REST API
    properties:
      - type: Documentation
        url: https://debezium.io/documentation/reference/stable/connectors/index.html
      - type: OpenAPI
        url: openapi/debezium-connect.yml
      - type: JSONSchema
        url: json-schema/debezium-change-event.json
      - type: Rules
        url: rules/debezium-kafka-connect-api-rules.yml
      - type: Capabilities
        url: capabilities/debezium-kafka-connect-api-capabilities.yml
common:
  - type: Website
    url: https://debezium.io/
  - type: Documentation
    url: https://debezium.io/documentation/
  - type: Getting Started
    url: https://debezium.io/documentation/reference/stable/tutorial.html
  - type: GitHub
    url: https://github.com/debezium/debezium
  - type: Blog
    url: https://debezium.io/blog/
  - type: Community
    url: https://debezium.io/community/
  - type: License
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: JSON-LD
    url: json-ld/debezium-context.jsonld
  - type: Vocabulary
    url: vocabulary/debezium-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
