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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Entso E Agentic Access
  operation_count: 2
  slug: entso-e-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Single query endpoint for every Transparency Platform data item. The documentType, processType, and domain parameters select the dataset.
  name: ENTSO-E Market Data Query API
  slug: entso-e-market-data-query-api
artifact_total: 11
collections:
- collection_type: open
  name: ENTSO-E Transparency Platform RESTful API
  slug: open-entso-e
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/entso-e-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entso-e-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/entso-e-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/entso-e
- group: company
  title: ''
  type: Website
  url: https://www.entsoe.eu/
- group: start
  title: ''
  type: Portal
  url: https://transparency.entsoe.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://transparencyplatform.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/entso-e-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/entso-e-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/entso-e-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.entsoe.eu/news/
- group: other
  title: ''
  type: TransparencyPlatform
  url: https://transparency.entsoe.eu/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://transparencyplatform.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EnergieID/entsoe-py
- group: docs
  title: ''
  type: PostmanDocumentation
  url: https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- group: other
  title: ''
  type: Registration
  url: https://transparency.entsoe.eu/usrm/user/createPublicUser
- group: operate
  title: ''
  type: Contact
  url: https://www.entsoe.eu/contact/
- group: company
  title: ''
  type: About
  url: https://www.entsoe.eu/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html
- group: other
  title: ''
  type: Email
  url: mailto:transparency@entsoe.eu
created: '2026-07-11'
description: ENTSO-E, the European Network of Transmission System Operators for Electricity, operates the Transparency Platform - the central publication point for pan-European electricity market data under EU Regulation 543/2013. Its free RESTful API returns day-ahead prices, system load, generation, balancing, and cross-border transmission data for every European bidding zone and control area as IEC 62325 XML market documents, selected by coded documentType and processType parameters against a single endpoint.
finops:
- name: Entso E Finops
  service_category: Analytics and Data
  slug: entso-e-finops
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/entso-e.png
layout: provider
modified: '2026-08-08'
name: ENTSO-E
nav: Providers
network: true
overview: 'ENTSO-E publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data Query API. Tagged areas include Electricity, Energy, Energy Markets, Day-Ahead Prices, and Balancing.


  ENTSO-E''s developer surface includes authentication, developer portal, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Entso E Plans Pricing
  plan_count: 1
  slug: entso-e-plans-pricing
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 5
  name: Entso E Rate Limits
  slug: entso-e-rate-limits
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 38.4
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.8
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/entso-e/refs/heads/main/screenshots/entso-e-2026-07-25T213441.png
security:
- kind: authentication
  name: Entso E Authentication
  slug: entso-e-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Entso E Domain Security
  slug: entso-e-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: entso-e
tags:
- Electricity
- Energy
- Energy Markets
- Day-Ahead Prices
- Balancing
- Transmission
- Grid Data
- Europe
website: https://www.entsoe.eu/
---
