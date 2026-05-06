---
aid: taxi-describe-how-your-apis-and-data-relate
name: Taxi - Describe How Your APIs and Data Relate
description: Taxi is an open-source language (Apache 2.0) for describing APIs, data models, and how data relates across an entire ecosystem. TaxiQL is a declarative query language that lets consumers define the data they want while Taxi handles orchestration across REST APIs, databases, Kafka topics, gRPC services, and S3 buckets. Taxi eliminates manual integration code by using semantic type annotations to automatically discover data paths and adapt to evolving API schemas.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Description
  - Data Integration
  - Open Source
  - Query Language
  - Schema
  - Semantic
created: '2026-01-05'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/taxi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: taxi-describe-how-your-apis-and-data-relate:taxi-language
    name: Taxi Language
    description: The core Taxi schema language for defining types, models, API services, and semantic annotations. Used to describe OpenAPI, Protobuf, database schemas, and Kafka topics with rich type semantics that power TaxiQL queries and data orchestration.
    humanURL: https://taxilang.org/
    tags:
      - API Description
      - Data Modeling
      - Open Source
      - Schema
      - Semantic Types
    properties:
      - type: Documentation
        url: https://docs.taxilang.org/
      - type: GitHub
        url: https://github.com/taxilang/taxilang
      - type: OpenAPI
        url: openapi/taxi-language-openapi.yml
  - aid: taxi-describe-how-your-apis-and-data-relate:taxiql-query-api
    name: TaxiQL Query API
    description: TaxiQL is a declarative query language for federated data retrieval across multiple APIs and data sources. Queries specify the desired data structure using semantic types and Taxi automatically discovers the data paths, calls APIs, and assembles results.
    humanURL: https://docs.taxilang.org/language-reference/querying-with-taxiql/
    tags:
      - Data Query
      - Federated Query
      - Open Source
      - Query Language
    properties:
      - type: Documentation
        url: https://docs.taxilang.org/language-reference/querying-with-taxiql/
      - type: GitHub
        url: https://github.com/taxilang/taxilang
  - aid: taxi-describe-how-your-apis-and-data-relate:orbital-platform
    name: Orbital Platform
    description: Orbital is the companion data platform for Taxi that hosts TaxiQL queries, provides a schema registry, and executes federated data integrations across APIs, databases, and streams using Taxi annotations.
    humanURL: https://orbitalhq.com
    tags:
      - Data Platform
      - Federated Query
      - Integration
      - Schema Registry
    properties:
      - type: Documentation
        url: https://orbitalhq.com
  - aid: taxi-describe-how-your-apis-and-data-relate:taxi-playground
    name: Taxi Playground
    description: Interactive web-based editor for writing Taxi schemas and TaxiQL queries with live diagram generation and query execution preview.
    humanURL: https://playground.taxilang.org
    tags:
      - Developer Tools
      - Playground
      - Schema Editor
    properties:
      - type: Documentation
        url: https://playground.taxilang.org
common:
  - type: Website
    url: https://taxilang.org/
  - type: Documentation
    url: https://docs.taxilang.org/
  - type: GitHub Org
    url: https://github.com/taxilang
  - type: Playground
    url: https://playground.taxilang.org
  - type: Slack
    url: https://join.slack.com/t/taxi-lang/shared_invite
  - type: OpenAPI
    url: openapi/taxi-language-openapi.yml
  - type: JSONSchema
    url: json-schema/taxi-schema-definition-schema.json
  - type: JSONStructure
    url: json-structure/taxi-schema-structure.json
  - type: JSONLD
    url: json-ld/taxi-context.jsonld
  - type: Vocabulary
    url: vocabulary/taxi-vocabulary.yml
  - type: NaftikoCapability
    url: capabilities/data-integration.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
