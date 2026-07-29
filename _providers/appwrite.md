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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Appwrite Agentic Access
  operation_count: 5
  slug: appwrite-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 4
apis:
- description: User account management
  name: Appwrite Account API
  slug: appwrite-account-api
- description: Database and collection management
  name: Appwrite Databases API
  slug: appwrite-databases-api
- description: File storage management
  name: Appwrite Storage API
  slug: appwrite-storage-api
- description: Server-side user management (requires server key)
  name: Appwrite Users API
  slug: appwrite-users-api
artifact_total: 35
asyncapis:
- description: AsyncAPI specification for the Appwrite Realtime WebSocket API. Appwrite Realtime lets clients subscribe to channels and receive callbacks whenever a subscribed resource changes. Subscriptions are sco
  name: Appwrite Realtime API
  slug: appwrite-asyncapi
collections:
- collection_type: postman
  name: Appwrite Account API
  slug: postman-appwrite-account-api
- collection_type: postman
  name: Appwrite Account Databases API
  slug: postman-appwrite-databases-api
- collection_type: postman
  name: Appwrite Account Storage API
  slug: postman-appwrite-storage-api
- collection_type: postman
  name: Appwrite Account Users API
  slug: postman-appwrite-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/appwrite/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appwrite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appwrite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appwrite-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appwrite
- group: company
  title: ''
  type: Website
  url: https://appwrite.io/
- group: docs
  title: ''
  type: Documentation
  url: https://appwrite.io/docs
- group: company
  title: ''
  type: Blog
  url: https://appwrite.io/blog
- group: operate
  title: ''
  type: Community
  url: https://appwrite.io/community
- group: start
  title: ''
  type: Signup
  url: https://cloud.appwrite.io/register
- group: start
  title: ''
  type: Login
  url: https://cloud.appwrite.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appwrite
- group: commercial
  title: ''
  type: Pricing
  url: https://appwrite.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appwrite.online/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/appwrite/mcp-for-api
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/appwrite/agent-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://appwrite.io/llms.txt
created: '2025-02-17'
description: Appwrite is an open-source backend server for building web and mobile applications. It provides a wide range of features including user authentication, file storage, database management, cloud functions, and messaging. With Appwrite, developers can easily set up a backend for their applications without writing code from scratch, offering a simple and intuitive API for seamless front-end integration.
examples:
- key_count: 10
  name: User Example
  slug: user-example
finops:
- name: Appwrite Finops
  service_category: API
  slug: appwrite-finops
graphqls:
- description: Appwrite exposes its full backend API surface through a GraphQL endpoint that mirrors every REST operation. All services — Account, Databases, Storage, Functions, Teams, Locale, Messaging, and Users —
  name: Appwrite GraphQL API
  slug: appwrite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appwrite.png
json_schemas:
- name: User
  property_count: 10
  slug: user
json_structures:
- name: User Structure
  property_count: 0
  slug: user-structure
jsonld:
- class_count: 10
  name: Appwrite Context
  property_count: 0
  slug: appwrite-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Appwrite
nav: Providers
network: true
overview: 'Appwrite publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Databases API, Storage API, and 1 more. Tagged areas include Applications, Backends, Mobile, and Open Source.


  The Appwrite catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Appwrite''s developer surface includes authentication, documentation, engineering blog, signup flow, pricing, and 12 more developer resources.'
plans:
- name: Appwrite Plans Pricing
  plan_count: 3
  slug: appwrite-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Appwrite Rate Limits
  slug: appwrite-rate-limits
rules:
- name: Appwrite API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: appwrite-asyncapi-spectral-rules
- name: Appwrite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appwrite-jsonschema-spectral-rules
- name: Appwrite API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appwrite-spectral-rules
score:
  band: strong
  composite: 59.8
  delta: -2.6
  facets:
    commercial_clarity: 63.2
    contract_quality: 84.7
    developer_ergonomics: 39.1
    discoverability: 55.6
    governance: 47.9
    operational_transparency: 52.6
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/screenshots/appwrite-2026-06-20T172338.png
security:
- kind: authentication
  name: Appwrite Authentication
  slug: appwrite-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appwrite Domain Security
  slug: appwrite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 11
skills:
- name: appwrite-cli
  slug: appwrite-cli
- name: appwrite-dart
  slug: appwrite-dart
- name: appwrite-dotnet
  slug: appwrite-dotnet
- name: appwrite-go
  slug: appwrite-go
- name: appwrite-kotlin
  slug: appwrite-kotlin
- name: appwrite-php
  slug: appwrite-php
- name: appwrite-python
  slug: appwrite-python
- name: appwrite-ruby
  slug: appwrite-ruby
- name: appwrite-rust
  slug: appwrite-rust
- name: appwrite-swift
  slug: appwrite-swift
- name: appwrite-typescript
  slug: appwrite-typescript
slug: appwrite
tags:
- Applications
- Backends
- Mobile
- Open Source
website: https://appwrite.io/
---
