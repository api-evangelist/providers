---
aid: prisma
url: https://raw.githubusercontent.com/api-evangelist/prisma/refs/heads/main/apis.yml
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
name: Prisma
tags:
- API
type: Contract
image: https://www.prisma.io/images/prisma-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Prisma is a next-generation ORM that helps developers build applications faster and with fewer errors. It provides a type-safe database client, migrations system, and visual database browser.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

