---
aid: rabbitmq
url: https://raw.githubusercontent.com/api-evangelist/rabbitmq/refs/heads/main/apis.yml
apis:
- aid: rabbitmq:rabbitmq-management-http-api
  name: RabbitMQ Management HTTP API
  description: HTTP-based API for management and monitoring of RabbitMQ nodes and clusters. Allows you to manage exchanges, queues, bindings, users, virtual hosts, permissions, and more.
  humanURL: https://www.rabbitmq.com/management.html
  baseURL: http://localhost:15672/api
  tags:
  - HTTP
  - Management
  - Monitoring
  - REST API
  properties:
  - type: Documentation
    url: https://rawcdn.githack.com/rabbitmq/rabbitmq-server/v3.12.0/deps/rabbitmq_management/priv/www/api/index.html
  - type: OpenAPI
    url: openapi/rabbitmq-management.yml
  - type: Authentication
    url: https://www.rabbitmq.com/management.html#permissions
- aid: rabbitmq:rabbitmq-amqp-messaging-api
  name: RabbitMQ AMQP Messaging API
  description: AMQP 0-9-1 messaging protocol for producing and consuming messages via exchanges, queues, and bindings with support for multiple exchange types, message acknowledgment, and consumer groups.
  humanURL: https://www.rabbitmq.com/tutorials/amqp-concepts.html
  tags:
  - AMQP
  - Messaging
  - Pub-Sub
  - Queues
  properties:
  - type: Documentation
    url: https://www.rabbitmq.com/tutorials/amqp-concepts.html
  - type: AsyncAPI
    url: asyncapi/rabbitmq-messaging.yml
  - type: JSONSchema
    url: json-schema/rabbitmq-message.json
name: RabbitMQ
tags:
- AMQP
- Distributed Systems
- Event Streaming
- Message Broker
- Messaging
- Queue
type: Contract
image: https://www.rabbitmq.com/img/rabbitmq-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: RabbitMQ is a widely deployed open source message broker. It supports multiple messaging protocols and can be deployed in distributed and federated configurations to meet high-scale, high-availability requirements.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

