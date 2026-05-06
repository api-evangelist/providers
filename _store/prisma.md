---
name: Prisma
description: Prisma is a next-generation ORM that helps developers build applications faster and with fewer errors. It provides a type-safe database client, migrations system, and visual database browser.
image: https://www.prisma.io/images/prisma-logo.svg
url: https://www.prisma.io
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.18'
apis:
  - name: Prisma Data Platform API
    description: REST API for managing Prisma Data Platform resources including projects, environments, and database connections through the Prisma Console.
    image: https://www.prisma.io/images/prisma-logo.svg
    humanUrl: https://www.prisma.io/docs/platform/about
    baseUrl: https://api.cloud.prisma.io
    tags:
      - Database
      - Developer Tools
      - ORM
      - Platform
    properties:
      - type: Documentation
        url: https://www.prisma.io/docs/platform/about
      - type: OpenAPI
        url: https://api.cloud.prisma.io/openapi.json
      - type: OpenAPI
        url: openapi/prisma-data-platform-openapi.yml
      - type: Authentication
        url: https://www.prisma.io/docs/management-api/authentication
      - type: Getting Started
        url: https://www.prisma.io/docs/console/getting-started
    contact:
      - FN: Prisma Support
        email: support@prisma.io
        url: https://www.prisma.io/support
  - name: Prisma Accelerate API
    description: API for Prisma Accelerate, a fully managed global connection pool and caching layer for existing databases with query-level cache policies directly from the Prisma ORM.
    image: https://www.prisma.io/images/prisma-logo.svg
    humanUrl: https://www.prisma.io/docs/accelerate
    baseUrl: https://accelerate.prisma-data.net
    tags:
      - Caching
      - Connection Pooling
      - Database
      - Performance
      - Serverless
    properties:
      - type: Documentation
        url: https://www.prisma.io/docs/accelerate
      - type: OpenAPI
        url: openapi/prisma-accelerate-openapi.yml
      - type: Getting Started
        url: https://www.prisma.io/docs/accelerate/getting-started
      - type: Reference
        url: https://www.prisma.io/docs/accelerate/reference/api-reference
      - type: FAQ
        url: https://www.prisma.io/docs/accelerate/more/faq
    contact:
      - FN: Prisma Support
        email: support@prisma.io
        url: https://www.prisma.io/support
  - name: Prisma Pulse API
    description: API for Prisma Pulse, a managed Change Data Capture service enabling real-time database change events and type-safe subscriptions via Prisma Client.
    image: https://www.prisma.io/images/prisma-logo.svg
    humanUrl: https://www.prisma.io/docs/pulse/database-events
    baseUrl: https://pulse.prisma-data.net
    tags:
      - Change Data Capture
      - Database
      - Events
      - Real-Time
      - Subscriptions
    properties:
      - type: Documentation
        url: https://www.prisma.io/docs/pulse/database-events
      - type: OpenAPI
        url: openapi/prisma-pulse-openapi.yml
      - type: Getting Started
        url: https://www.prisma.io/docs/pulse/getting-started
      - type: FAQ
        url: https://www.prisma.io/docs/pulse/faq
    contact:
      - FN: Prisma Support
        email: support@prisma.io
        url: https://www.prisma.io/support
  - name: Prisma Postgres Management API
    description: REST API for programmatically provisioning and managing Prisma Postgres databases, projects, and workspaces, supporting automation, CI/CD workflows, and partner integrations.
    image: https://www.prisma.io/images/prisma-logo.svg
    humanUrl: https://www.prisma.io/docs/postgres/introduction/management-api
    baseUrl: https://api.prisma.io/v1
    tags:
      - Database
      - Infrastructure
      - Managed Database
      - PostgreSQL
      - Provisioning
    properties:
      - type: Documentation
        url: https://www.prisma.io/docs/postgres/introduction/management-api
      - type: OpenAPI
        url: openapi/prisma-postgres-management-openapi.yml
      - type: Getting Started
        url: https://www.prisma.io/docs/guides/management-api-basic
      - type: Authentication
        url: https://www.prisma.io/docs/management-api/authentication
      - type: SDKs
        url: https://www.prisma.io/docs/management-api/sdk
    contact:
      - FN: Prisma Support
        email: support@prisma.io
        url: https://www.prisma.io/support
  - name: Prisma Client API
    description: Auto-generated, type-safe query builder for Node.js and TypeScript that provides programmatic database access for PostgreSQL, MySQL, SQLite, SQL Server, MongoDB, and CockroachDB.
    image: https://www.prisma.io/images/prisma-logo.svg
    humanUrl: https://www.prisma.io/docs/orm/reference/prisma-client-reference
    tags:
      - Database
      - Node.js
      - ORM
      - Query Builder
      - TypeScript
    properties:
      - type: Documentation
        url: https://www.prisma.io/docs/orm
      - type: OpenAPI
        url: openapi/prisma-client-openapi.yml
      - type: Reference
        url: https://www.prisma.io/docs/orm/reference/prisma-client-reference
      - type: Getting Started
        url: https://www.prisma.io/docs/getting-started/prisma-orm/quickstart/prisma-postgres
      - type: SDKs
        url: https://www.npmjs.com/package/@prisma/client
    contact:
      - FN: Prisma Support
        email: support@prisma.io
        url: https://www.prisma.io/support
  - name: Prisma Optimize API
    description: Query performance tool for analyzing, debugging, and improving database queries during development, with AI-powered recommendations to reduce database load and improve responsiveness.
    image: https://www.prisma.io/images/prisma-logo.svg
    humanUrl: https://www.prisma.io/docs/optimize
    tags:
      - AI
      - Database
      - Developer Tools
      - Performance
      - Query Optimization
    properties:
      - type: Documentation
        url: https://www.prisma.io/docs/optimize
      - type: OpenAPI
        url: openapi/prisma-optimize-openapi.yml
      - type: Getting Started
        url: https://www.prisma.io/docs/optimize/getting-started
      - type: SDKs
        url: https://www.npmjs.com/package/@prisma/extension-optimize
    contact:
      - FN: Prisma Support
        email: support@prisma.io
        url: https://www.prisma.io/support
common:
  - type: Portal
    url: https://console.prisma.io/login
  - type: Documentation
    url: https://www.prisma.io/docs
  - type: Getting Started
    url: https://www.prisma.io/docs/getting-started
  - type: Authentication
    url: https://www.prisma.io/docs/management-api/authentication
  - type: Blog
    url: https://www.prisma.io/blog
  - type: Change Log
    url: https://www.prisma.io/changelog
  - type: GitHub Organization
    url: https://github.com/prisma
  - type: Community
    url: https://www.prisma.io/community
  - type: Discord
    url: https://pris.ly/discord
  - type: Twitter
    url: https://twitter.com/prisma
  - type: Pricing
    url: https://www.prisma.io/pricing
  - type: Status
    url: https://www.prisma-status.com
  - type: Support
    url: https://www.prisma.io/support
  - type: Terms of Service
    url: https://www.prisma.io/terms
  - type: Privacy Policy
    url: https://www.prisma.io/privacy
  - type: Website
    url: https://www.prisma.io
  - type: Login
    url: https://console.prisma.io/login
  - type: Sign Up
    url: https://console.prisma.io/sign-up
  - type: JSON-LD Context
    url: json-ld/prisma-context.jsonld
  - type: JSON Schema
    url: json-schema/prisma-workspace-schema.json
  - type: JSON Schema
    url: json-schema/prisma-project-schema.json
  - type: JSON Schema
    url: json-schema/prisma-database-schema.json
  - type: JSON Schema
    url: json-schema/prisma-cache-strategy-schema.json
  - type: JSON Schema
    url: json-schema/prisma-pulse-event-schema.json
  - type: JSON Schema
    url: json-schema/prisma-query-recommendation-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://www.prisma.io
---
