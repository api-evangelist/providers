---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Mysql Agentic Access
  operation_count: 4
  slug: mysql-agentic-access
  summary_line: 4 operations · 2 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The MySQL REST Service (MRS) provides a RESTful interface for accessing MySQL databases. Endpoints are dynamically defined per database schema and table by the database administrator.
  name: MySQL REST Service
  slug: mysql-rest-service
- description: Modern API for MySQL with CRUD operations and NoSQL document store capabilities, available across multiple language connectors.
  name: MySQL X DevAPI
  slug: x-devapi
- description: Native driver APIs for connecting applications to MySQL across multiple programming languages including Python, Node.js, Java, and .NET.
  name: MySQL Connector APIs
  slug: connectors
- description: MRS authentication endpoints (SCRAM and OAuth2).
  name: MySQL Authentication API
  slug: mysql-authentication-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MySQL REST Service (MRS) Runtime Authentication API
  slug: open-mysql-authentication-api
- collection_type: open
  name: MySQL REST Service (MRS) Runtime API
  slug: open-mysql
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mysql-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mysql-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mysql-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.mysql.com/doc/mysql-getting-started/en/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.mysql.com/doc/
- group: other
  title: ''
  type: Downloads
  url: https://dev.mysql.com/downloads/
- group: operate
  title: ''
  type: Community
  url: https://www.mysql.com/community/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/mysql/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mysql
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/mysql
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mysql.com/about/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-01'
description: MySQL is the world's most popular open-source relational database management system. This index covers the developer-facing APIs and interfaces for MySQL, including the MySQL REST Service, X DevAPI, and native connectors.
finops:
- name: Mysql Finops
  service_category: API
  slug: mysql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mysql.png
layout: provider
modified: '2026-04-28'
name: MySQL
nav: Providers
network: true
overview: 'MySQL publishes 1 API on the [APIs.io](https://apis.io/) network: Authentication API. Tagged areas include Database, Open Source, RDBMS, Relational Database, and SQL.


  MySQL''s developer surface includes authentication, getting-started guide, documentation, engineering blog, Stack Overflow tag, and 7 more developer resources.'
plans:
- name: Mysql Plans Pricing
  plan_count: 3
  slug: mysql-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Mysql Rate Limits
  slug: mysql-rate-limits
score:
  band: thin
  composite: 33.9
  delta: -0.8
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 41.3
    developer_ergonomics: 38.1
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mysql/refs/heads/main/screenshots/mysql-2026-06-20T185918.png
security:
- kind: authentication
  name: Mysql Authentication
  slug: mysql-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mysql Domain Security
  slug: mysql-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mysql
tags:
- Database
- Open Source
- RDBMS
- Relational Database
- SQL
website: https://www.mysql.com
---
