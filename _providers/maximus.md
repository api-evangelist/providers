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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Maximus API provides access to platform services and data for enterprise integration and automation.
  name: Maximus API
  slug: maximus-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maximus-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maximus
- group: company
  title: ''
  type: Website
  url: https://www.maximus.com
- group: company
  title: ''
  type: Blog
  url: https://maximus.com/news
created: '2026-04-19'
description: Maximus is a major US corporation and Fortune 1000 company. The Maximus API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Maximus Finops
  service_category: Government Services / IT Modernization
  slug: maximus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maximus.png
layout: provider
modified: '2026-04-19'
name: Maximus
nav: Providers
network: true
overview: 'Maximus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government Services, Health, and Technology.


  Maximus'' developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Maximus Plans Pricing
  plan_count: 1
  slug: maximus-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Maximus Rate Limits
  slug: maximus-rate-limits
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maximus/refs/heads/main/screenshots/maximus-2026-06-20T185049.png
security:
- kind: domain-security
  name: Maximus Domain Security
  slug: maximus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maximus
tags:
- Government Services
- Health
- Technology
website: https://www.maximus.com
---
