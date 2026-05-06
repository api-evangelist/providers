---
aid: kafka-connect
name: Kafka Connect
description: Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. It makes it simple to quickly define connectors that move large collections of data into and out of Kafka.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache Kafka
  - Connectors
  - Data Integration
  - ETL
  - Streaming
url: https://raw.githubusercontent.com/api-evangelist/kafka-connect/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
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
common:
  - type: Website
    url: https://kafka.apache.org/documentation/#connect
  - type: Documentation
    url: https://kafka.apache.org/documentation/#connect
  - type: Getting Started
    url: https://kafka.apache.org/quickstart
  - type: GitHub Organization
    url: https://github.com/apache/kafka
  - type: Blog
    url: https://kafka.apache.org/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
