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
- description: Power your digital workflows using comprehensive property and location intelligence data from LightBox.
  name: LightBox
  slug: lightbox
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightbox-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightbox-re
created: '2025-02-17'
description: Power your digital workflows using comprehensive property and location intelligence data from LightBox.
finops:
- name: Lightbox Finops
  service_category: API
  slug: lightbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightbox.png
layout: provider
modified: '2026-04-28'
name: LightBox
nav: Providers
network: true
overview: LightBox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Location Intelligence, Property Data, and Real-Estate.
plans:
- name: Lightbox Plans Pricing
  plan_count: 3
  slug: lightbox-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Lightbox Rate Limits
  slug: lightbox-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightbox/refs/heads/main/screenshots/lightbox-2026-06-20T184513.png
security:
- kind: domain-security
  name: Lightbox Domain Security
  slug: lightbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightbox
tags:
- Location Intelligence
- Property Data
- Real-Estate
---
