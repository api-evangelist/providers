---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Knack Agentic Access
  operation_count: 6
  slug: knack-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: Resource-oriented REST API for managing records in Knack applications. Supports create, retrieve, update, and delete operations against specific objects or page views. All requests and responses use J
  name: Knack REST API
  slug: rest-api
- description: CRUD operations on records via object endpoints
  name: Knack Object Records API
  slug: knack-object-records-api
- description: Operations on records via page view endpoints
  name: Knack View Records API
  slug: knack-view-records-api
artifact_total: 7
collections:
- collection_type: open
  name: Knack REST API
  slug: open-knack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knack-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knackhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knackhq
- group: company
  title: ''
  type: Website
  url: https://www.knack.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knack.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.knack.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.knack.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://support.knack.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.knack.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.knack.com/blog/feed/
created: '2026-05-11'
description: Knack is a no-code database and application platform that lets users build custom web applications from structured data without writing code. The platform combines a relational database, forms, search, charts, and user access controls with embeddable pages. Knack offers a resource-oriented REST API with predictable URLs for creating, retrieving, updating, and deleting records, authenticated via an Application ID and REST API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knack.png
layout: provider
modified: '2026-05-11'
name: Knack
nav: Providers
network: true
overview: 'Knack publishes 2 APIs on the [APIs.io](https://apis.io/) network: Object Records API and View Records API. Tagged areas include No-Code, Database, Application Builder, Low-Code, and Web Applications.


  Knack''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 34
score:
  band: thin
  composite: 30.9
  delta: -2.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knack/refs/heads/main/screenshots/knack-2026-06-20T184106.png
security:
- kind: authentication
  name: Knack Authentication
  slug: knack-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Knack Domain Security
  slug: knack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knack
tags:
- No-Code
- Database
- Application Builder
- Low-Code
- Web Applications
website: https://www.knack.com
---
