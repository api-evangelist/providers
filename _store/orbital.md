---
aid: orbital
url: https://raw.githubusercontent.com/api-evangelist/orbital/refs/heads/main/apis.yml
apis:
- aid: orbital:query-api
  name: Orbital Query API
  tags:
  - Data
  - Gateways
  - Integration
  - Queries
  humanURL: https://orbitalhq.com/docs/querying/writing-queries
  properties:
  - url: https://orbitalhq.com/docs/querying/writing-queries
    type: Documentation
  - url: openapi/orbital-query-api-openapi.yml
    type: OpenAPI
  - url: json-schema/query.json
    type: JSONSchema
  - url: json-schema/connection.json
    type: JSONSchema
  - url: json-schema/cache.json
    type: JSONSchema
  - url: json-ld/orbital-context.jsonld
    type: JSONLD
  description: The Orbital Query API allows developers to submit TaxiQL queries to the Orbital data gateway for integrating, transforming, and discovering data across APIs, databases, event streams, and other data sources. Queries are submitted to the /api/taxiql endpoint and results can be returned as JSON or streamed via Server-Sent Events. The API also provides endpoints for managing connections and caches.
- aid: orbital:schema-management-api
  name: Orbital Schema Management API
  tags:
  - Data
  - Gateways
  - Schemas
  - Types
  humanURL: https://orbitalhq.com/docs/describing-data-sources/open-api
  properties:
  - url: https://orbitalhq.com/docs/describing-data-sources/open-api
    type: Documentation
  - url: openapi/orbital-schema-management-api-openapi.yml
    type: OpenAPI
  - url: json-schema/schema.json
    type: JSONSchema
  - url: json-schema/service.json
    type: JSONSchema
  - url: json-schema/type.json
    type: JSONSchema
  - url: json-ld/orbital-context.jsonld
    type: JSONLD
  description: The Orbital Schema Management API provides endpoints for managing schemas, types, and data source definitions within an Orbital workspace. It allows developers to register, update, and remove Taxi schemas and type definitions that Orbital uses to understand the semantic relationships between data across connected services. Schemas can originate from OpenAPI specs, Protobuf definitions, database schemas, or Taxi projects.
name: Orbital
tags:
- Data
- Gateways
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-05'
modified: '2026-04-07'
position: Consuming
description: Orbital is a data gateway and integration platform that connects APIs, databases, event streams, and other data sources without requiring glue code or manual integration maintenance. The platform delivers self-repairing integrations through instant, on-the-fly orchestration that automatically adapts as APIs and schemas evolve, eliminating the need to write resolvers, generate API clients, or maintain YAML mapping files.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
common:
- name: Orbital - Automated integration for modern dev teams.
  description: 'null'
  url: https://orbitalhq.com/
  type: Website
- name: Getting started - Orbital
  description: 'null'
  url: https://orbitalhq.com/docs
  type: Documentation
- name: Changelog - Orbital
  description: 'null'
  url: https://orbitalhq.com/changelog
  type: ChangeLog
- name: Pricing - Orbital
  description: 'null'
  url: https://orbitalhq.com/pricing
  type: Pricing
- name: Blog - Orbital
  description: 'null'
  url: https://orbitalhq.com/blog
  type: Blog
---

