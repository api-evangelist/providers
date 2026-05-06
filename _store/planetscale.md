---
aid: planetscale
url: https://raw.githubusercontent.com/api-evangelist/planetscale/refs/heads/main/apis.yml
apis:
  - aid: planetscale:platform-api
    name: PlanetScale Platform API
    tags:
      - Branching
      - Cloud
      - Databases
      - Deploy Requests
      - MySQL
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.planetscale.com/v1
    humanURL: https://api-docs.planetscale.com/reference/getting-started-with-planetscale-api
    properties:
      - url: https://api-docs.planetscale.com/reference/getting-started-with-planetscale-api
        type: Documentation
      - url: openapi/planetscale-platform-api-openapi.yml
        type: OpenAPI
      - url: asyncapi/planetscale-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The PlanetScale Platform API provides programmatic access to manage PlanetScale serverless MySQL databases. It allows developers to create and delete database branches, manage deploy requests, automate password and connection string management, and integrate PlanetScale into CI/CD pipelines and infrastructure-as-code workflows. The API supports authentication via service tokens and OAuth, and its base URL is https://api.planetscale.com/v1 with an OpenAPI 3.0 specification available for download.
  - aid: planetscale:oauth
    name: PlanetScale OAuth
    tags:
      - Applications
      - Authentication
      - Authorization
      - OAuth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.planetscale.com
    humanURL: https://planetscale.com/docs/api/planetscale-api-oauth-applications
    properties:
      - url: https://planetscale.com/docs/api/planetscale-api-oauth-applications
        type: Documentation
    description: PlanetScale OAuth allows developers to create OAuth applications that can access users' PlanetScale accounts on their behalf. The implementation supports the Authorization Code grant type, enabling third-party applications to authenticate users and obtain delegated access to PlanetScale resources. This is particularly useful for building integrations and tools that need to interact with organization-level PlanetScale endpoints on behalf of multiple users.
  - aid: planetscale:serverless-driver
    name: PlanetScale Serverless Driver for JavaScript
    tags:
      - Driver
      - Edge Computing
      - JavaScript
      - MySQL
      - SDK
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://planetscale.com/docs/tutorials/using-the-serverless-driver
    properties:
      - url: https://planetscale.com/docs/tutorials/using-the-serverless-driver
        type: Documentation
    description: The PlanetScale Serverless Driver for JavaScript is a Fetch API-compatible database driver designed for serverless and edge compute platforms such as Cloudflare Workers, Vercel Edge Functions, and Netlify Edge Functions. It enables developers to query PlanetScale databases over HTTP connections, bypassing the TCP restrictions common in edge environments.
  - aid: planetscale:cli
    name: PlanetScale CLI
    tags:
      - CLI
      - Command Line
      - Database Management
      - Developer Tools
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://planetscale.com/docs/reference/planetscale-cli
    properties:
      - url: https://planetscale.com/docs/reference/planetscale-cli
        type: Documentation
    description: The PlanetScale CLI (pscale) is a command-line tool that brings PlanetScale database management to the terminal. It allows developers to create, delete, and list databases and branches, open interactive MySQL shells for database branches, and manage deploy requests directly from the command line. The CLI is available via Homebrew and as a downloadable binary, and includes a Model Context Protocol (MCP) server that provides AI tools with direct access to PlanetScale databases.
common:
  - type: JSON-LD
    url: json-ld/planetscale-context.jsonld
  - type: JSONSchema
    url: json-schema/planetscale-database-schema.json
  - type: Features
    data:
      - Postgres EBS single-node from $5/mo
      - Postgres EBS HA 3-node from $15/mo
      - Postgres Metal 3-node from $50/mo
      - Vitess Non-Metal 3-node from $39/mo
      - Vitess Metal 3-node from $609/mo
      - Cluster sizes from 1/16 vCPU to 96 vCPU
      - arm64 and x86-64 architectures
      - Multi-region deployment options
      - Optional PgBouncer for Postgres
      - Optional read replicas
      - Branching for safe schema changes
      - Deploy requests for review-and-merge schema flow
      - Connection pooling built in
      - Insights for query performance
      - Boost for query result caching
      - Management API at 240 req/min/org
    sources:
      - https://planetscale.com/pricing
    updated: '2026-05-04'
modified: '2026-05-04'
description: PlanetScale is a serverless MySQL database platform powered by Vitess, providing horizontal scaling, branching workflows, non-blocking schema changes, and other developer-friendly database features.
---
