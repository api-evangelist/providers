---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Regal Rexnord API provides access to platform services and data for enterprise integration and automation.
  name: Regal Rexnord API
  slug: regal-rexnord-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regal-rexnord-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regal-rexnord
- group: company
  title: ''
  type: Website
  url: https://www.regalrexnord.com
created: '2026-04-19'
description: Regal Rexnord is a major US corporation and Fortune 1000 company. The Regal Rexnord API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Regal Rexnord Finops
  service_category: Industrial
  slug: regal-rexnord-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regal-rexnord.png
layout: provider
modified: '2026-04-19'
name: Regal Rexnord
nav: Providers
network: true
overview: Regal Rexnord publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial, Motion Control, and Manufacturing.
plans:
- name: Regal Rexnord Plans Pricing
  plan_count: 1
  slug: regal-rexnord-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Regal Rexnord Rate Limits
  slug: regal-rexnord-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regal-rexnord/refs/heads/main/screenshots/regal-rexnord-2026-06-20T192753.png
security:
- kind: domain-security
  name: Regal Rexnord Domain Security
  slug: regal-rexnord-domain-security
  summary_line: TLSv1.3 · DMARC
slug: regal-rexnord
tags:
- Industrial
- Motion Control
- Manufacturing
website: https://www.regalrexnord.com
---
