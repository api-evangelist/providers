---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
- acting_count: 5
  human_in_the_loop: 0
  name: Maya Mobile Agentic Access
  operation_count: 9
  slug: maya-mobile-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 4
apis:
- description: eSIM provisioning, activation codes/QR, suspend and reactivate.
  name: Maya Mobile eSIMs API
  slug: maya-mobile-esims-api
- description: Placing and assigning data-package orders, including top-ups.
  name: Maya Mobile Orders API
  slug: maya-mobile-orders-api
- description: Pre-made data plans and the catalog of countries, regions, and networks.
  name: Maya Mobile Plans API
  slug: maya-mobile-plans-api
- description: Real-time eSIM status and data-usage reporting.
  name: Maya Mobile Usage API
  slug: maya-mobile-usage-api
artifact_total: 11
collections:
- collection_type: open
  name: Maya Mobile Connect+ Connectivity API
  slug: open-maya-mobile
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maya-mobile-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maya-mobile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maya-mobile-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mayamobile-us
- group: company
  title: ''
  type: Website
  url: https://maya.net/
- group: docs
  title: ''
  type: Documentation
  url: https://maya.net/business/esim-api
- group: commercial
  title: ''
  type: Plans
  url: plans/maya-mobile-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maya-mobile-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maya-mobile-finops.yml
created: '2026-06-21'
description: Maya Mobile (Mobile Maya Inc) is a US-based global eSIM and connectivity platform aggregating 400+ roaming networks across 200+ destinations. Its Connect+ Connectivity REST API lets resellers and developers provision eSIMs, assign data packages, monitor activation status and data usage, suspend or reactivate lines, process top-ups, and receive lifecycle events via webhooks.
finops:
- name: Maya Mobile Finops
  service_category: Networking and Connectivity
  slug: maya-mobile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maya-mobile.png
layout: provider
modified: '2026-06-21'
name: Maya Mobile
nav: Providers
network: true
overview: 'Maya Mobile publishes 4 APIs on the [APIs.io](https://apis.io/) network, including eSIMs API, Orders API, Plans API, and 1 more. Tagged areas include eSIM, Connectivity, Mobile Data, Roaming, and Telecom.


  Maya Mobile''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Maya Mobile Plans Pricing
  plan_count: 2
  slug: maya-mobile-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Maya Mobile Rate Limits
  slug: maya-mobile-rate-limits
score:
  band: thin
  composite: 32.6
  delta: -4.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maya-mobile/refs/heads/main/screenshots/maya-mobile-2026-07-25T230448.png
security:
- kind: authentication
  name: Maya Mobile Authentication
  slug: maya-mobile-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Maya Mobile Domain Security
  slug: maya-mobile-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maya-mobile
tags:
- eSIM
- Connectivity
- Mobile Data
- Roaming
- Telecom
website: https://maya.net/
---
