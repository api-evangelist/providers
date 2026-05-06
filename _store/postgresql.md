---
aid: postgresql
name: PostgreSQL
description: PostgreSQL is a powerful, open-source object-relational database system with over 35 years of active development. It provides advanced SQL compliance, ACID transactions, and extensibility. PostgreSQL exposes a binary wire protocol via libpq and language bindings rather than a public HTTP REST API, so there is no canonical OpenAPI specification. HTTP access is typically layered on top via PostgREST, Hasura, or application code.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database
  - Open Source
  - Relational Database
  - SQL
url: https://raw.githubusercontent.com/api-evangelist/postgresql/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: postgresql:postgresql
    name: PostgreSQL
    description: Open-source relational database with advanced SQL compliance and extensibility. Client libraries available in many languages.
    humanURL: https://www.postgresql.org/
    tags:
      - Database
      - SQL
    properties:
      - type: Documentation
        url: https://www.postgresql.org/docs/
      - type: Getting Started
        url: https://www.postgresql.org/docs/current/tutorial.html
common:
  - type: Website
    url: https://www.postgresql.org/
  - type: Documentation
    url: https://www.postgresql.org/docs/
  - type: Community
    url: https://www.postgresql.org/community/
  - type: GitHub Organization
    url: https://github.com/postgres/postgres
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
