---
aid: stepzen
name: StepZen
description: StepZen (now IBM API Connect Essentials) is a GraphQL-as-a-Service platform that enables developers to build, deploy, and manage GraphQL APIs by connecting to multiple backends including REST APIs, SQL databases, NoSQL databases, GraphQL endpoints, and SOAP services. APIs are defined declaratively using GraphQL SDL with custom directives like @rest and @dbquery. StepZen runs a high-performance in-memory Golang GraphQL engine deployed on Kubernetes, optimizing queries at runtime for low latency and high throughput.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backend Integration
  - GraphQL
  - API Gateway
  - REST to GraphQL
  - IBM
  - Data Federation
url: https://raw.githubusercontent.com/api-evangelist/stepzen/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stepzen:stepzen-api
    name: StepZen GraphQL API
    description: GraphQL API platform for connecting to REST, databases, and other backends, automatically generating a GraphQL schema and resolvers from your data sources. Supports authentication via API key, OAuth, and custom headers. Deployed instances are accessible at account.stepzen.net endpoints.
    humanURL: https://stepzen.com/
    baseURL: https://{account}.stepzen.net/{folder}/{name}/__graphql
    tags:
      - GraphQL
      - API Integration
      - Data Federation
      - REST
      - Database
    properties:
      - type: Documentation
        url: https://stepzen.com/docs
      - type: GitHub Organization
        url: https://github.com/stepzen-dev
      - type: CLI Reference
        url: https://stepzen.com/docs/cli/cli-commands
      - type: Getting Started
        url: https://stepzen.com/docs/quick-start/install-and-setup
      - type: IBM Documentation
        url: https://www.ibm.com/docs/en/stepzen
  - aid: stepzen:stepzen-admin-api
    name: StepZen Admin API
    description: REST API for managing StepZen accounts, deployed GraphQL endpoints, API keys, and usage metrics programmatically.
    humanURL: https://stepzen.com/docs
    tags:
      - Administration
      - API Management
      - GraphQL
    properties:
      - type: Documentation
        url: https://stepzen.com/docs
common:
  - type: Portal
    url: https://stepzen.com/
  - type: Documentation
    url: https://stepzen.com/docs
  - type: Website
    url: https://stepzen.com/
  - type: GitHub Organization
    url: https://github.com/stepzen-dev
  - type: Dashboard
    url: https://dashboard.ibm.stepzen.com/
  - type: IBM Product Page
    url: https://www.ibm.com/products/api-connect
features:
  - name: REST to GraphQL
    description: Import existing REST APIs and auto-generate GraphQL schemas using @rest directive
  - name: Database to GraphQL
    description: Connect SQL (MySQL, PostgreSQL, MSSQL) and NoSQL databases using @dbquery directive
  - name: GraphQL Federation
    description: Import and stitch multiple GraphQL endpoints into a unified schema
  - name: SOAP to GraphQL
    description: Connect SOAP/WSDL services to GraphQL using @connector directive
  - name: Declarative Schema
    description: Define APIs with GraphQL SDL and custom directives, no resolver code needed
  - name: Auto-Generated Resolvers
    description: StepZen generates and optimizes resolvers at runtime from declarative schema
  - name: Query Optimization
    description: Runtime query planning and optimization for low latency and high throughput
  - name: Schema Explorer
    description: Built-in browser-based GraphQL schema explorer for testing deployed APIs
  - name: CLI Import
    description: stepci import curl/graphql/mysql commands to introspect and generate schemas
useCases:
  - name: API Aggregation
    description: Combine multiple REST and database sources into a single unified GraphQL API
  - name: Frontend BFF
    description: Create tailored Backend-for-Frontend GraphQL layers for React, Next.js, Vue
  - name: Data Federation
    description: Federate data from multiple disparate sources into a single queryable schema
  - name: Legacy API Modernization
    description: Expose legacy REST and SOAP APIs as modern GraphQL endpoints
  - name: Rapid Prototyping
    description: Quickly build and deploy GraphQL APIs from existing data sources
integrations:
  - name: MySQL
    description: Connect MySQL databases using @dbquery directive
  - name: PostgreSQL
    description: Connect PostgreSQL databases using @dbquery directive
  - name: REST APIs
    description: Import any REST/HTTP API using @rest directive or stepzen import curl
  - name: GraphQL
    description: Import existing GraphQL schemas using stepzen import graphql
  - name: Shopify
    description: Pre-built Shopify GraphQL integration
  - name: WordPress
    description: Connect WordPress data via REST API import
  - name: Next.js
    description: Official Next.js starter template and integration guide
  - name: Netlify
    description: StepZen build plugin for Netlify deployments
  - name: Apigee
    description: GraphQL API management integration with Google Apigee
solutions:
  - name: GraphQL as a Service
    description: Fully managed GraphQL execution layer without infrastructure management
  - name: IBM API Connect Essentials
    description: StepZen functionality available as part of IBM API Connect platform
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
