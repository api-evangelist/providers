---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delek-us-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/delek-us
- group: company
  title: ''
  type: Website
  url: https://www.delekus.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.delekus.com
- group: other
  title: ''
  type: Alias
  url: https://raw.githubusercontent.com/api-evangelist/delek-us-holdings/refs/heads/main/apis.yml
created: '2026-03-21'
description: 'Delek US is an alias for Delek US Holdings, Inc. (NYSE: DK), a diversified downstream energy company headquartered in Brentwood, Tennessee with assets in petroleum refining, logistics, asphalt operations, renewable fuels, and convenience store retailing. Delek operates four refineries in Tyler and Big Spring (Texas), El Dorado (Arkansas), and Krotz Springs (Louisiana) with combined crude throughput capacity of roughly 302,000 barrels per day. The canonical profile for this company is maintained under aid delek-us-holdings; this entry exists as a name alias and references the corporate site. Delek does not publish a developer API; partner integrations occur through industry-standard EDI, terminal automation, and ticketing systems.'
finops:
- name: Delek Us Finops
  service_category: Energy
  slug: delek-us-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delek-us.png
layout: provider
modified: '2026-07-25'
name: Delek US
nav: Providers
network: true
overview: Delek US is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Alias, Downstream, Energy, Petroleum, and Refining.
plans:
- name: Delek Us Plans Pricing
  plan_count: 1
  slug: delek-us-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Delek Us Rate Limits
  slug: delek-us-rate-limits
score:
  band: minimal
  composite: 12.7
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Delek Us Domain Security
  slug: delek-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: delek-us
tags:
- Alias
- Downstream
- Energy
- Petroleum
- Refining
- Retail
- Fortune 500
website: https://www.delekus.com
---
