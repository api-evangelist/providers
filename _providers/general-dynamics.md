---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: General Dynamics Agentic Access
  operation_count: 3
  slug: general-dynamics-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Technology products operations
  name: General Dynamics Products API
  slug: general-dynamics-products-api
- description: Mission systems operations
  name: General Dynamics Systems API
  slug: general-dynamics-systems-api
artifact_total: 8
collections:
- collection_type: open
  name: General Dynamics Mission Systems API
  slug: open-general-dynamics-mission-systems-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/general-dynamics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/general-dynamics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/general-dynamics
- group: company
  title: ''
  type: Website
  url: https://www.gd.com
- group: other
  title: ''
  type: Mission Systems
  url: https://gdmissionsystems.com
description: 'General Dynamics Corporation is a global aerospace and defense company headquartered in Reston, Virginia. The company operates across five business segments: Aerospace, Marine Systems, Combat Systems, Technologies, and Mission Systems, providing business aviation, ship construction, land combat vehicles, weapons systems, and technology products and services.'
finops:
- name: General Dynamics Finops
  service_category: Defense & Aerospace
  slug: general-dynamics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/general-dynamics.png
layout: provider
modified: '2026-05-19'
name: General Dynamics
nav: Providers
network: true
overview: 'General Dynamics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Products API and Systems API. Tagged areas include Aerospace, Defense, Mission Systems, Government, and Fortune 100.'
plans:
- name: General Dynamics Plans Pricing
  plan_count: 1
  slug: general-dynamics-plans-pricing
press:
- date: '2026-05-25'
  title: GENERAL | definition in the Cambridge English Dictionary
  url: https://dictionary.cambridge.org/us/dictionary/english/general
- date: '2026-05-25'
  title: The General® Car Insurance | Get a Quote to Insure Your Car
  url: https://www.thegeneral.com/
- date: '2026-05-25'
  title: GENERAL Definition & Meaning
  url: https://www.merriam-webster.com/dictionary/general
- date: '2026-05-25'
  title: General (United States)
  url: https://en.wikipedia.org/wiki/General_(United_States)
- date: '2026-05-25'
  title: 'General Motors: Iconic Vehicles for Every Drive'
  url: https://www.gm.com/
random_paper: 20
rate_limits:
- limit_count: 1
  name: General Dynamics Rate Limits
  slug: general-dynamics-rate-limits
score:
  band: emerging
  composite: 26.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.6
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/general-dynamics/refs/heads/main/screenshots/general-dynamics-2026-06-20T181724.png
security:
- kind: domain-security
  name: General Dynamics Domain Security
  slug: general-dynamics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: general-dynamics
tags:
- Aerospace
- Defense
- Mission Systems
- Government
- Fortune 100
website: https://www.gd.com
---
