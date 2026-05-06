---
aid: apollo-federation
name: Apollo Federation
description: Apollo Federation is an architecture and platform for building a unified supergraph that composes multiple GraphQL APIs (subgraphs) into a single distributed GraphQL endpoint, enabling teams to work independently on different parts of the graph while delivering a unified API to consumers. Federation 2 is the current stable version, supported by the Apollo Router written in Rust and the Rover CLI for schema management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Federation
  - GraphQL
  - Microservices
  - Open Source
  - Subgraphs
  - Supergraph
url: https://raw.githubusercontent.com/api-evangelist/apollo-federation/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apollo-federation:apollo-federation
    name: Apollo Federation
    description: Apollo Federation enables declarative composition of multiple subgraph APIs into a single federated supergraph. The Apollo Router orchestrates requests across subgraphs, combining GraphQL APIs and REST APIs (via Apollo Connectors) into a unified endpoint. Federation 2 defines the supergraph schema, federation directives, and composition rules. The Rover CLI manages schema publishing and checks.
    humanURL: https://www.apollographql.com/docs/federation/
    tags:
      - API Gateway
      - Federation
      - GraphQL
      - Microservices
      - Open Source
      - REST Integration
      - Router
      - Subgraphs
      - Supergraph
    properties:
      - type: Documentation
        url: https://www.apollographql.com/docs/federation/
      - type: GettingStarted
        url: https://www.apollographql.com/docs/federation/quickstart/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-federation/refs/heads/main/json-schema/supergraph-configuration.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-federation/refs/heads/main/json-schema/router-configuration.json
      - type: GitHubRepository
        url: https://github.com/apollographql/federation
      - type: ChangeLog
        url: https://www.apollographql.com/docs/graphos/reference/federation/versions
common:
  - type: Documentation
    url: https://www.apollographql.com/docs/federation/
  - type: GettingStarted
    url: https://www.apollographql.com/docs/federation/quickstart/
  - type: GitHubOrganization
    url: https://github.com/apollographql
  - type: GitHubRepository
    url: https://github.com/apollographql/federation
    title: Federation Spec
  - type: GitHubRepository
    url: https://github.com/apollographql/router
    title: Apollo Router
  - type: GitHubRepository
    url: https://github.com/apollographql/rover
    title: Rover CLI
  - type: GitHubRepository
    url: https://github.com/apollographql/apollo-federation-subgraph-compatibility
    title: Subgraph Compatibility Tests
  - type: SDK
    url: https://github.com/apollographql/federation-jvm
    title: JVM Support
  - type: Blog
    url: https://www.apollographql.com/blog/
  - type: Pricing
    url: https://www.apollographql.com/pricing/
  - type: SignUp
    url: https://studio.apollographql.com/signup
  - type: Features
    data:
      - name: Supergraph Composition
        description: Compose multiple subgraph schemas into a single unified supergraph schema.
      - name: Federation Directives
        description: Declarative federation directives (@key, @external, @requires, @provides, @shareable, @link) for schema coordination.
      - name: Apollo Router
        description: High-performance Rust-based router that orchestrates queries across subgraphs.
      - name: Apollo Connectors
        description: Declarative integration of REST APIs into federated graphs without writing a separate GraphQL server.
      - name: Schema Registry
        description: Apollo GraphOS schema registry for publishing, checking, and managing supergraph schemas.
      - name: Rover CLI
        description: Command-line tool for publishing subgraph schemas, running checks, and managing the supergraph.
      - name: Query Planning
        description: Intelligent query planning that decomposes client queries into efficient subgraph requests.
      - name: Subgraph Compatibility
        description: Federation-compatible subgraphs can be built in any language or framework.
      - name: Gray Release Support
        description: Progressive schema rollout with incremental migration from monolith to federated graph.
  - type: UseCases
    data:
      - name: Distributed Team Development
        description: Enable independent teams to own and develop separate subgraphs while delivering a unified API.
      - name: REST API Modernization
        description: Gradually expose existing REST APIs as GraphQL via Apollo Connectors without full rewrites.
      - name: API Consolidation
        description: Consolidate multiple disparate APIs into a single unified supergraph for consumers.
      - name: Microservices GraphQL Layer
        description: Add a federated GraphQL layer over existing microservice architectures.
      - name: Schema Governance
        description: Enforce schema design standards across all subgraphs via composition checks.
  - type: Integrations
    data:
      - name: Anthropic
        description: Apollo Connector for integrating Anthropic AI APIs into the supergraph.
      - name: OpenAI
        description: Apollo Connector for integrating OpenAI APIs into the supergraph.
      - name: AWS DynamoDB
        description: Apollo Connector for AWS DynamoDB via REST API integration.
      - name: AWS Lambda
        description: Apollo Connector for AWS Lambda function invocation.
      - name: Stripe
        description: Apollo Connector for Stripe payment API integration.
      - name: OData
        description: Apollo Connector for OData REST API integration.
      - name: Strapi
        description: Apollo Connector for Strapi CMS API integration.
      - name: Kubernetes
        description: Deploy Apollo Router as a Kubernetes service via Helm charts and operator patterns.
      - name: Terraform
        description: Official Terraform provider for Apollo GraphOS management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
