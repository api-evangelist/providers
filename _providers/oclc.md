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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The Discovery API allows you to surface both WorldCat and WorldCat Discovery central index data in search results, including: Materials held by your library and ...'
  name: OCLC
  slug: oclc
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oclc-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oclc
- group: company
  title: ''
  type: Blog
  url: https://www.oclc.org/en/news.html
created: '2025-01-08'
description: 'The Discovery API allows you to surface both WorldCat and WorldCat Discovery central index data in search results, including: Materials held by your library and ...'
finops:
- name: Oclc Finops
  service_category: API
  slug: oclc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oclc.png
layout: provider
modified: '2026-04-28'
name: OCLC
nav: Providers
network: true
overview: 'OCLC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Library, WorldCat, Discovery, and Bibliographic.


  OCLC''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Oclc Plans Pricing
  plan_count: 3
  slug: oclc-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Oclc Rate Limits
  slug: oclc-rate-limits
score:
  band: minimal
  composite: 8.2
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
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oclc/refs/heads/main/screenshots/oclc-2026-06-20T190605.png
security:
- kind: domain-security
  name: Oclc Domain Security
  slug: oclc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oclc
tags:
- Library
- WorldCat
- Discovery
- Bibliographic
---
