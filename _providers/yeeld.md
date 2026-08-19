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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Move faster with payment experts offering advisory and development services, along with a Surcharging API to recover costs and ensure compliance.
  name: Yeeld
  slug: yeeld
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yeeld-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/theyeeld
- group: company
  title: ''
  type: Blog
  url: https://theyeeld.com/feed/
created: '2025-02-21'
description: Move faster with payment experts offering advisory and development services, along with a Surcharging API to recover costs and ensure compliance.
finops:
- name: Yeeld Finops
  service_category: API
  slug: yeeld-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yeeld.png
layout: provider
modified: '2026-03-16'
name: Yeeld
nav: Providers
network: true
overview: 'Yeeld publishes 1 API on the [APIs.io](https://apis.io/) network.


  Yeeld''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Yeeld Plans Pricing
  plan_count: 3
  slug: yeeld-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Yeeld Rate Limits
  slug: yeeld-rate-limits
score:
  band: minimal
  composite: 8.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 8.7
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yeeld/refs/heads/main/screenshots/yeeld-2026-06-20T201737.png
security:
- kind: domain-security
  name: Yeeld Domain Security
  slug: yeeld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yeeld
---
