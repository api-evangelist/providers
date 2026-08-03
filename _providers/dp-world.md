---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: DP World's APIs provide access to shipping schedules, container status, terminal operations, freight rates, and supply chain visibility data across the company's global port and logistics network. Thr
  name: DP World API
  slug: dp-world
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dp-world-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dp-world
- group: company
  title: ''
  type: Website
  url: https://www.dpworld.com
- group: other
  title: ''
  type: Digital Solutions
  url: https://www.dpworld.com/digital-solutions
- group: other
  title: ''
  type: CARGOES
  url: https://www.cargoes.com/
created: '2025-03-01'
description: DP World is an Emirati global logistics company that specializes in port operations, maritime services, and supply chain solutions. It manages and operates marine and inland terminals across more than 40 countries and operates a portfolio of digital platforms - including the CARGOES suite (Flow, Runner, TOS+, PCS, Customs), Searates, and the Digital Freight Alliance - that expose APIs and integrations for shipment visibility, freight pricing, terminal operations, and trade workflows.
finops:
- name: Dp World Finops
  service_category: API
  slug: dp-world-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dp-world.png
layout: provider
modified: '2026-04-28'
name: DP World
nav: Providers
network: true
overview: DP World publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Maritime, Ports, Supply Chain, and Logistics.
plans:
- name: Dp World Plans Pricing
  plan_count: 3
  slug: dp-world-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Dp World Rate Limits
  slug: dp-world-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 17.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dp-world/refs/heads/main/screenshots/dp-world-2026-06-20T180227.png
security:
- kind: domain-security
  name: Dp World Domain Security
  slug: dp-world-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dp-world
tags:
- Maritime
- Ports
- Supply Chain
- Logistics
website: https://www.dpworld.com
---
