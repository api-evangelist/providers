---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: A lightweight, extensible, open source and cross-platform ORM for .NET. Supports SQL Server, PostgreSQL, MySQL, SQLite, Cosmos DB, and in-memory databases.
  name: Entity Framework Core
  slug: ef-core
- description: The mature and stable ORM for .NET Framework with Code First, Database First, and Model First workflows.
  name: Entity Framework 6
  slug: ef6
artifact_total: 27
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-entity-framework-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-entity-framework-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://learn.microsoft.com/en-us/ef/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/dotnet/tag/entity-framework/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotnet
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/entity-framework-core
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/playlist?list=PLdo4fOcmZ0oX0ObHwBrJ0vJpZ7PiYMqeA
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/ef/core/get-started/overview/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
created: '2024-01-01'
description: Microsoft Entity Framework is an object-relational mapping (ORM) framework for .NET developers enabling database access using .NET objects. EF Core is the modern, cross-platform version supporting SQL Server, PostgreSQL, MySQL, SQLite, and Cosmos DB with LINQ queries, change tracking, migrations, and code-first modeling.
features:
- description: Write database queries using Language Integrated Query (LINQ) with strongly-typed C# expressions.
  name: LINQ Queries
- description: Automatic tracking of entity changes for efficient database updates.
  name: Change Tracking
- description: Database schema versioning with code-first migrations for evolving data models.
  name: Migrations
- description: Define database schemas using C# classes and data annotations or Fluent API.
  name: Code First Modeling
- description: Plugin architecture supporting SQL Server, PostgreSQL, MySQL, SQLite, Cosmos DB, and more.
  name: Database Providers
- description: Control related entity loading with lazy, eager, and explicit loading strategies.
  name: Lazy and Eager Loading
- description: Execute raw SQL and stored procedures alongside LINQ queries.
  name: Raw SQL Queries
- description: Apply automatic filtering to all queries for multi-tenancy and soft deletes.
  name: Global Query Filters
- description: Custom type conversions between .NET types and database column types.
  name: Value Converters
- description: Pre-compile LINQ queries for improved performance in hot paths.
  name: Compiled Queries
finops:
- name: Microsoft Entity Framework Finops
  service_category: API
  slug: microsoft-entity-framework-finops
image: https://docs.microsoft.com/en-us/ef/images/ef-logo.png
layout: provider
modified: '2026-04-28'
name: Microsoft Entity Framework
nav: Providers
network: true
overview: 'Microsoft Entity Framework publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, Data Access, Database, Entity Framework, and ORM.


  The Microsoft Entity Framework catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Entity Framework''s developer surface includes developer portal, engineering blog, Stack Overflow tag, YouTube channel, support, and 5 more developer resources.'
plans:
- name: Microsoft Entity Framework Plans Pricing
  plan_count: 3
  slug: microsoft-entity-framework-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Microsoft Entity Framework Rate Limits
  slug: microsoft-entity-framework-rate-limits
rules:
- name: Microsoft Entity Framework API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: entity-framework-spectral-rules
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 92.5
    governance: 26.3
    operational_transparency: 36.8
  previous_composite: 32.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-entity-framework/refs/heads/main/screenshots/microsoft-entity-framework-2026-06-20T185456.png
security:
- kind: domain-security
  name: Microsoft Entity Framework Domain Security
  slug: microsoft-entity-framework-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Entity Framework Vulnerability Disclosure
  slug: microsoft-entity-framework-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-entity-framework
solutions:
- description: Modern, cross-platform ORM for .NET 6+ applications.
  name: Entity Framework Core
- description: Mature ORM for .NET Framework applications.
  name: Entity Framework 6
- description: CLI and Package Manager Console tools for migrations and scaffolding.
  name: EF Core Tools
tags:
- .NET
- Data Access
- Database
- Entity Framework
- ORM
use_cases:
- description: Data access layer for ASP.NET Core web applications and APIs.
  name: Web Application Data Access
- description: Database access for .NET microservices with per-service databases.
  name: Microservices Data Layer
- description: Version-controlled schema evolution with automatic migration generation.
  name: Database Migration Management
- description: Applications connecting to multiple database providers simultaneously.
  name: Multi-Database Applications
- description: Implement DDD patterns with aggregate roots, value objects, and repositories.
  name: Domain-Driven Design
- description: Map existing database schemas to modern .NET classes with Database First.
  name: Legacy Database Integration
website: https://learn.microsoft.com/en-us/ef/
---
