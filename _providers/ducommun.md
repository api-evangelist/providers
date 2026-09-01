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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Ducommun API provides access to platform services and data for enterprise integration and automation.
  name: Ducommun API
  slug: ducommun-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ducommun-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ducommun-incorporated
- group: company
  title: ''
  type: Website
  url: https://www.ducommun.com
created: '2026-04-19'
description: Ducommun is a major US corporation and Fortune 1000 company. The Ducommun API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Ducommun Finops
  service_category: Aerospace & Defense Manufacturing
  slug: ducommun-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ducommun.png
layout: provider
modified: '2026-04-19'
name: Ducommun
nav: Providers
network: true
overview: Ducommun publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aerospace, Defense, and Manufacturing.
plans:
- name: Ducommun Plans Pricing
  plan_count: 1
  slug: ducommun-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ducommun Rate Limits
  slug: ducommun-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ducommun/refs/heads/main/screenshots/ducommun-2026-06-20T180312.png
security:
- kind: domain-security
  name: Ducommun Domain Security
  slug: ducommun-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ducommun
tags:
- Aerospace
- Defense
- Manufacturing
website: https://www.ducommun.com
---
