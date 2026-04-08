---
aid: kafka-connect
url: https://raw.githubusercontent.com/api-evangelist/kafka-connect/refs/heads/main/apis.yml
apis:
- aid: kafka-connect:kafka-connect-rest-api
  name: Kafka Connect REST API
  description: The Kafka Connect REST API allows you to manage connectors and tasks, monitor status, and interact with the Connect cluster.
  humanURL: https://kafka.apache.org/documentation/#connect_rest
  baseURL: http://localhost:8083
  tags:
  - Connectors
  - REST API
  - Tasks
  properties:
  - type: Documentation
    url: https://kafka.apache.org/documentation/#connect_rest
name: Kafka Connect
tags:
- Apache Kafka
- Connectors
- Data Integration
- ETL
- Streaming
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. It makes it simple to quickly define connectors that move large collections of data into and out of Kafka.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

