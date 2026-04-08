---
aid: debezium
url: https://raw.githubusercontent.com/api-evangelist/debezium/refs/heads/main/apis.yml
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
name: Debezium
tags:
- Apache Kafka
- CDC
- Change Data Capture
- Databases
- Event Streaming
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Debezium is an open source distributed platform for change data capture (CDC) that converts changes in existing databases into event streams, enabling applications to detect and respond to row-level changes in databases in real time.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

