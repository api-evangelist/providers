---
aid: masstransit
name: MassTransit
description: MassTransit is a free, open source distributed application framework for .NET that makes it easy to create applications and services that leverage message-based, loosely-coupled asynchronous communication for higher availability, reliability, and scalability.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - .NET
  - Event-Driven
  - Message Bus
  - Messaging
  - Open Source
  - Sagas
url: https://raw.githubusercontent.com/api-evangelist/masstransit/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
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
common:
  - type: Website
    url: https://masstransit.io/
  - type: Documentation
    url: https://masstransit.io/documentation/concepts
  - type: Getting Started
    url: https://masstransit.io/quick-starts
  - type: GitHub
    url: https://github.com/MassTransit/MassTransit
  - type: Discord
    url: https://discord.gg/rNpQgYn
  - type: NuGet
    url: https://www.nuget.org/packages/MassTransit
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
