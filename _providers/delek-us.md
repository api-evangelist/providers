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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Corporate website redirect for Delek US, the doing-business-as brand of Delek US Holdings, Inc. The canonical site is delekus.com and provides corporate, investor, and sustainability information.
  name: Delek US Website
  slug: delek-us-website
artifact_total: 5
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
modified: '2026-04-28'
name: Delek US
nav: Providers
network: true
overview: Delek US publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Alias, Downstream, Energy, Petroleum, and Refining.
plans:
- name: Delek Us Plans Pricing
  plan_count: 1
  slug: delek-us-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 1
  name: Delek Us Rate Limits
  slug: delek-us-rate-limits
score:
  band: emerging
  composite: 16.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.5
  schema_version: 0.5
  scored_at: '2026-07-23'
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
