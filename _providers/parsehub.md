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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Parsehub Agentic Access
  operation_count: 8
  slug: parsehub-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 2
apis:
- description: The Projects API from ParseHub — 4 operation(s) for projects.
  name: ParseHub Projects API
  slug: parsehub-projects-api
- description: The Runs API from ParseHub — 3 operation(s) for runs.
  name: ParseHub Runs API
  slug: parsehub-runs-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ParseHub Projects API
  slug: open-parsehub-projects-api
- collection_type: open
  name: ParseHub Projects Runs API
  slug: open-parsehub-runs-api
- collection_type: open
  name: ParseHub API
  slug: open-parsehub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parsehub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsehub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parsehub-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.parsehub.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parsehub
- group: company
  title: ''
  type: Website
  url: https://www.parsehub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.parsehub.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.parsehub.com/docs/ref/api/v2/
created: '2026-03-29'
description: ParseHub is a visual web scraping tool that turns any website into an API with a point-and-click interface for data extraction.
finops:
- name: Parsehub Finops
  service_category: API
  slug: parsehub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parsehub.png
layout: provider
modified: '2026-05-19'
name: ParseHub
nav: Providers
network: true
overview: 'ParseHub publishes 2 APIs on the [APIs.io](https://apis.io/) network: Projects API and Runs API. Tagged areas include Data Extraction, Scraping, and Visual Scraping.


  ParseHub''s developer surface includes authentication, engineering blog, documentation, API reference, and 4 more developer resources.'
plans:
- name: Parsehub Plans Pricing
  plan_count: 3
  slug: parsehub-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Parsehub Rate Limits
  slug: parsehub-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parsehub/refs/heads/main/screenshots/parsehub-2026-06-20T191423.png
security:
- kind: authentication
  name: Parsehub Authentication
  slug: parsehub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parsehub Domain Security
  slug: parsehub-domain-security
  summary_line: TLSv1.3 · HSTS
slug: parsehub
tags:
- Data Extraction
- Scraping
- Visual Scraping
website: https://www.parsehub.com/
---
