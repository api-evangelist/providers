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
- description: The EnPro Industries API provides access to platform services and data for enterprise integration and automation.
  name: EnPro Industries API
  slug: enpro-industries-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enpro-industries-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/about-enpro
- group: company
  title: ''
  type: Website
  url: https://www.enproindustries.com
created: '2026-04-19'
description: EnPro Industries is a major US corporation and Fortune 1000 company. The EnPro Industries API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Enpro Industries Finops
  service_category: Industrial Manufacturing Integration
  slug: enpro-industries-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enpro-industries.png
layout: provider
modified: '2026-04-19'
name: EnPro Industries
nav: Providers
network: true
overview: EnPro Industries publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial, Sealing, and Manufacturing.
plans:
- name: Enpro Industries Plans Pricing
  plan_count: 1
  slug: enpro-industries-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Enpro Industries Rate Limits
  slug: enpro-industries-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/enpro-industries/refs/heads/main/screenshots/enpro-industries-2026-07-25T213418.png
security:
- kind: domain-security
  name: Enpro Industries Domain Security
  slug: enpro-industries-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enpro-industries
tags:
- Industrial
- Sealing
- Manufacturing
website: https://www.enproindustries.com
---
