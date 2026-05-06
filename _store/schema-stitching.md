---
aid: schema-stitching
name: Schema Stitching
description: Schema Stitching is a GraphQL technique for combining multiple GraphQL schemas into a single unified API gateway. It enables developers to compose distributed GraphQL services, integrate third-party APIs, and build federated data layers by merging types, queries, and mutations from multiple subgraphs into one executable schema. The primary implementation is provided by The Guild's graphql-tools library, with support for type merging, stitching directives, schema delegation, and automated query planning.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Composition
  - API Gateway
  - Federation
  - GraphQL
  - Microservices
  - Schema Stitching
  - Type Merging
url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: schema-stitching:schema-stitching
    name: Schema Stitching
    description: Schema Stitching is a GraphQL technique for combining multiple GraphQL schemas into a single unified API gateway. The @graphql-tools/stitch package creates a combined proxy layer that delegates requests through to underlying service APIs, supporting type merging, stitching directives, and automated query planning comparable to Apollo Federation.
    humanURL: https://the-guild.dev/graphql/stitching
    tags:
      - API Composition
      - GraphQL
      - Schema Stitching
      - Type Merging
    properties:
      - type: Documentation
        url: https://the-guild.dev/graphql/stitching/docs
      - type: Getting Started
        url: https://the-guild.dev/graphql/stitching/docs/getting-started
      - type: Handbook
        url: https://the-guild.dev/graphql/stitching/handbook
      - type: GitHub Repository
        url: https://github.com/ardatan/graphql-tools
      - type: npm Package
        url: https://www.npmjs.com/package/@graphql-tools/stitch
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/json-schema/schema-stitching-config-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/json-structure/schema-stitching-config-structure.json
      - type: JSONLd
        url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/json-ld/schema-stitching-context.jsonld
  - aid: schema-stitching:graphql-mesh
    name: GraphQL Mesh
    description: GraphQL Mesh allows stitching together multiple data sources including REST APIs, databases, and other GraphQL APIs into a single unified GraphQL schema. It applies schema stitching techniques to transform and federate heterogeneous data sources.
    humanURL: https://the-guild.dev/graphql/mesh
    tags:
      - API Gateway
      - GraphQL
      - Schema Stitching
    properties:
      - type: Documentation
        url: https://the-guild.dev/graphql/mesh/docs
      - type: GitHub Repository
        url: https://github.com/ardatan/graphql-mesh
  - aid: schema-stitching:hive-gateway
    name: Hive Gateway
    description: Hive Gateway is a federated GraphQL routing engine from The Guild that supports both Apollo Federation and Schema Stitching approaches to compose distributed GraphQL services.
    humanURL: https://the-guild.dev/graphql/hive/docs/gateway
    tags:
      - API Gateway
      - Federation
      - GraphQL
    properties:
      - type: Documentation
        url: https://the-guild.dev/graphql/hive/docs/gateway
      - type: GitHub Repository
        url: https://github.com/the-guild-org/gateway
  - aid: schema-stitching:apollo-federation
    name: Apollo Federation
    description: Apollo Federation is an alternative to schema stitching for composing distributed GraphQL services. It uses a supergraph approach with subgraph schemas annotated with federation directives, managed through Apollo Studio or self-hosted routers.
    humanURL: https://www.apollographql.com/docs/federation/
    tags:
      - API Gateway
      - Apollo
      - Federation
      - GraphQL
    properties:
      - type: Documentation
        url: https://www.apollographql.com/docs/federation/
      - type: GitHub Repository
        url: https://github.com/apollographql/federation
common:
  - type: Website
    url: https://the-guild.dev/graphql/stitching
  - type: Documentation
    url: https://the-guild.dev/graphql/stitching/docs
  - type: Handbook
    url: https://the-guild.dev/graphql/stitching/handbook
  - type: GitHub Organization
    url: https://github.com/ardatan
  - type: Blog
    url: https://the-guild.dev/blog
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/vocabulary/schema-stitching-vocabulary.yml
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/schema-stitching/refs/heads/main/examples/schema-stitching-basic-gateway-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
