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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ourpeople Agentic Access
  operation_count: 6
  slug: ourpeople-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 2
apis:
- description: Token issuance and refresh.
  name: OurPeople Authentication API
  slug: ourpeople-authentication-api
- description: Inspect broadcasts, deliveries, and recipient engagement.
  name: OurPeople Broadcasts API
  slug: ourpeople-broadcasts-api
artifact_total: 9
collections:
- collection_type: open
  name: OurPeople API
  slug: open-ourpeople
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ourpeople-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ourpeople-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ourpeople-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OurPeople
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/our-people-ltd
- group: start
  title: ''
  type: Portal
  url: https://developer.ourpeople.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ourpeople.com/
- group: company
  title: ''
  type: Website
  url: https://ourpeople.com/
- group: operate
  title: ''
  type: Support
  url: https://ourpeople.com/support
created: '2025-02-08'
description: The OurPeople API uses common standards to allow easy read and write access to your data. OurPeople is a frontline communications platform that helps organizations communicate with deskless workers.
finops:
- name: Ourpeople Finops
  service_category: API
  slug: ourpeople-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ourpeople.png
layout: provider
modified: '2026-05-19'
name: OurPeople
nav: Providers
network: true
overview: 'OurPeople publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Broadcasts API. Tagged areas include Communications, Workforce, and Frontline.


  OurPeople''s developer surface includes authentication, developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Ourpeople Plans Pricing
  plan_count: 3
  slug: ourpeople-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Ourpeople Rate Limits
  slug: ourpeople-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -1.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.9
    developer_ergonomics: 32.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/ourpeople/refs/heads/main/screenshots/ourpeople-2026-06-20T191224.png
security:
- kind: authentication
  name: Ourpeople Authentication
  slug: ourpeople-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ourpeople Domain Security
  slug: ourpeople-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ourpeople
tags:
- Communications
- Workforce
- Frontline
website: https://ourpeople.com/
---
