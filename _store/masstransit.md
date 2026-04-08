---
aid: masstransit
url: https://raw.githubusercontent.com/api-evangelist/masstransit/refs/heads/main/apis.yml
apis:
- aid: masstransit:masstransit-messaging
  name: MassTransit Messaging Framework
  description: MassTransit provides a consistent abstraction on top of message transports like RabbitMQ, Azure Service Bus, and Amazon SQS, with support for sagas, state machines, routing slip activities, and a standardized message envelope format.
  humanURL: https://masstransit.io/
  tags:
  - .NET
  - Event-Driven
  - Message Bus
  - Messaging
  - Sagas
  properties:
  - type: Documentation
    url: https://masstransit.io/documentation/concepts
  - type: JSONSchema
    url: json-schema/masstransit-message-envelope.json
  - type: JSONSchema
    url: json-schema/masstransit-saga-state.json
name: MassTransit
tags:
- .NET
- Event-Driven
- Message Bus
- Messaging
- Open Source
- Sagas
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: MassTransit is a free, open source distributed application framework for .NET that makes it easy to create applications and services that leverage message-based, loosely-coupled asynchronous communication for higher availability, reliability, and scalability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

