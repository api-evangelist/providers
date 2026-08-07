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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Surfe Agentic Access
  operation_count: 10
  slug: surfe-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 4
apis:
- description: Credit balance and account utilities.
  name: Surfe Account API
  slug: surfe-account-api
- description: Search and enrich organizations.
  name: Surfe Companies API
  slug: surfe-companies-api
- description: Search and enrich individual contacts.
  name: Surfe People API
  slug: surfe-people-api
- description: ICP definition and lookalike account recommendations.
  name: Surfe Recommendations API
  slug: surfe-recommendations-api
artifact_total: 11
collections:
- collection_type: open
  name: Surfe API
  slug: open-surfe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/surfe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surfe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/surfe-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.surfe.com/blog/feed/
created: '2026-07-01'
description: Surfe (formerly Leadjet) is a B2B contact-data and sales-intelligence platform that syncs LinkedIn prospects into the CRM and exposes an API for people and company search plus enrichment. The Surfe API returns verified business emails and mobile phone numbers, company firmographics, and lookalike account recommendations, billed against a credit-based model.
finops:
- name: Surfe Finops
  service_category: Data and Analytics
  slug: surfe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surfe.png
layout: provider
modified: '2026-07-01'
name: Surfe
nav: Providers
network: true
overview: 'Surfe publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Companies API, People API, and 1 more. Tagged areas include B2B Data, Contact Data, Sales Intelligence, Enrichment, and Lead Generation.


  Surfe''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Surfe Plans Pricing
  plan_count: 4
  slug: surfe-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 4
  name: Surfe Rate Limits
  slug: surfe-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Surfe Authentication
  slug: surfe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Surfe Domain Security
  slug: surfe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: surfe
tags:
- B2B Data
- Contact Data
- Sales Intelligence
- Enrichment
- Lead Generation
- CRM
- Prospecting
---
