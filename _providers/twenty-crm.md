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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Twenty Crm Agentic Access
  operation_count: 36
  slug: twenty-crm-agentic-access
  summary_line: 36 operations · 22 acting
api_count: 8
apis:
- description: Auto-generated GraphQL API over the same workspace schema, exposing queries, mutations, batch upserts via plural object names, and relation traversal for the Core API (/graphql) and Metadata API (/met
  name: Twenty GraphQL API
  slug: twenty-crm-graphql-api
- description: Core API CRUD over company records.
  name: Twenty Companies API
  slug: twenty-crm-companies-api
- description: Metadata API management of field definitions.
  name: Twenty Metadata - Fields API
  slug: twenty-crm-metadata-fields-api
- description: Metadata API management of object definitions.
  name: Twenty Metadata - Objects API
  slug: twenty-crm-metadata-objects-api
- description: Core API CRUD over note records.
  name: Twenty Notes API
  slug: twenty-crm-notes-api
- description: Core API CRUD over opportunity records.
  name: Twenty Opportunities API
  slug: twenty-crm-opportunities-api
- description: Core API CRUD over person records.
  name: Twenty People API
  slug: twenty-crm-people-api
- description: Core API CRUD over task records.
  name: Twenty Tasks API
  slug: twenty-crm-tasks-api
artifact_total: 17
collections:
- collection_type: open
  name: Twenty CRM API
  slug: open-twenty-crm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twenty-crm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/twenty-crm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twenty-crm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twenty-crm-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twentyhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twenty-crm
- group: company
  title: ''
  type: Website
  url: https://twenty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.twenty.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/twenty-crm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/twenty-crm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/twenty-crm-finops.yml
created: '2026-06-20'
description: Twenty is an open-source CRM and a modern alternative to Salesforce. It auto-generates both a REST API and a GraphQL API from your workspace data model, exposing a Core API for records (People, Companies, Opportunities, Notes, Tasks, and custom objects) and a Metadata API for schema (objects, fields, and relations). Twenty is free to self-host and available as a managed Twenty Cloud offering.
finops:
- name: Twenty Crm Finops
  service_category: CRM and Sales
  slug: twenty-crm-finops
graphqls:
- description: Representative GraphQL schema for [Twenty](https://twenty.com/), the open-source CRM.
  name: Twenty GraphQL Schema
  slug: twenty-crm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twenty-crm.png
layout: provider
modified: '2026-06-20'
name: Twenty
nav: Providers
network: true
overview: 'Twenty publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Metadata - Fields API, Metadata - Objects API, and 4 more. Tagged areas include CRM, Open Source, Sales, GraphQL, and REST.


  Twenty''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Twenty Crm Plans Pricing
  plan_count: 3
  slug: twenty-crm-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Twenty Crm Rate Limits
  slug: twenty-crm-rate-limits
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twenty-crm/refs/heads/main/screenshots/twenty-crm-2026-06-20T195950.png
security:
- kind: authentication
  name: Twenty Crm Authentication
  slug: twenty-crm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Twenty Crm Domain Security
  slug: twenty-crm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Twenty Crm Vulnerability Disclosure
  slug: twenty-crm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: twenty-crm
tags:
- CRM
- Open Source
- Sales
- GraphQL
- REST
website: https://twenty.com/
---
