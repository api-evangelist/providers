---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Chowly Agentic Access
  operation_count: 3
  slug: chowly-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: Connects third-party delivery marketplaces (DoorDash, Uber Eats, Grubhub, and 150+ channels) and 50+ native POS systems (Toast, Square, SpotOn, Clover, and others). Marketplace and POS partners integr
  name: Chowly Integrations API
  slug: integrations
- description: Retrieve the menu synchronized across ordering channels.
  name: Chowly Menu API
  slug: chowly-menu-api
- description: Create and retrieve orders injected into the restaurant POS.
  name: Chowly Orders API
  slug: chowly-orders-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chowly POS Integration Menu API
  slug: open-chowly-menu-api
- collection_type: open
  name: Chowly POS Integration Menu Orders API
  slug: open-chowly-orders-api
- collection_type: open
  name: Chowly POS Integration API
  slug: open-chowly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chowly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chowly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chowly-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chowly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chowly
- group: company
  title: ''
  type: Website
  url: https://www.chowly.com
- group: docs
  title: ''
  type: Documentation
  url: https://chowly.help/s/faqs
- group: commercial
  title: ''
  type: Plans
  url: plans/chowly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chowly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chowly-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://chowly.com/resources/blogs/
created: '2026-06-21'
description: Chowly is a restaurant digital-ordering and delivery-integration platform that connects third-party delivery marketplaces (DoorDash, Uber Eats, Grubhub, and 150+ others) and direct online ordering into a restaurant's point-of-sale (POS) system. The Chowly platform injects third-party orders directly into the POS, synchronizes menus across every channel, and manages locations. Its developer surface is a partner-gated POS integration API keyed per location; the most commonly referenced operations are menu retrieval and order creation/retrieval.
finops:
- name: Chowly Finops
  service_category: Business Application Services
  slug: chowly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chowly.png
layout: provider
modified: '2026-06-21'
name: Chowly
nav: Providers
network: true
overview: 'Chowly publishes 2 APIs on the [APIs.io](https://apis.io/) network: Menu API and Orders API. Tagged areas include Restaurants, Online Ordering, Delivery, POS Integration, and Menu Sync.


  Chowly''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Chowly Plans Pricing
  plan_count: 1
  slug: chowly-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: Chowly Rate Limits
  slug: chowly-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chowly/refs/heads/main/screenshots/chowly-2026-07-25T205258.png
security:
- kind: authentication
  name: Chowly Authentication
  slug: chowly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chowly Domain Security
  slug: chowly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chowly
tags:
- Restaurants
- Online Ordering
- Delivery
- POS Integration
- Menu Sync
website: https://www.chowly.com
---
