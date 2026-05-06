---
aid: cqrs
name: CQRS
x-type: topic
description: Command Query Responsibility Segregation (CQRS) is an architectural pattern that separates read and write operations for a data store into distinct models. Commands mutate state and produce events; queries return data optimized for the read side. CQRS is frequently combined with Event Sourcing, Domain-Driven Design (DDD), and message-based integration to scale complex domains. The pattern is most associated with Greg Young, building on Bertrand Meyer's Command-Query Separation principle, and is widely covered in writings by Martin Fowler and the Microsoft Patterns and Practices team.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/cqrs/refs/heads/main/apis.yml
type: Index
access: Open Source
position: Producing
created: '2025-01-01'
modified: '2026-04-28'
tags:
  - Architecture
  - Command Query Responsibility Segregation
  - Commands
  - CQRS
  - Domain-Driven Design
  - Event Sourcing
  - Events
  - Patterns
  - Queries
  - Read Models
apis: []
common:
  - type: MartinFowlerOnCQRS
    url: https://martinfowler.com/bliki/CQRS.html
  - type: GregYoungOnCQRS
    url: https://gregyoung.com/blog/
  - type: CQRSDocumentsByGregYoung
    url: https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf
  - type: MicrosoftCQRSPattern
    url: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
  - type: AWSCQRSPattern
    url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html
  - type: CommandQuerySeparation
    url: https://martinfowler.com/bliki/CommandQuerySeparation.html
  - type: EventSourcingPattern
    url: https://microservices.io/patterns/data/event-sourcing.html
  - type: DDDCommunity
    url: https://www.dddcommunity.org/
  - type: AxonFramework
    url: https://www.axoniq.io/products/axon-framework
  - type: EventStoreDB
    url: https://www.eventstore.com/
  - type: NServiceBus
    url: https://particular.net/nservicebus
  - type: MediatRGitHub
    url: https://github.com/jbogard/MediatR
  - type: WikipediaCQRS
    url: https://en.wikipedia.org/wiki/Command%E2%80%93query_separation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
