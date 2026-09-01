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
- description: Enhance your own applications with fast, reliable access to the data that powers our newsroom.
  name: ProPublica Data Store
  slug: propublica
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propublica-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/propublica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propublica
- group: company
  title: ''
  type: Blog
  url: https://www.propublica.org/feeds/propublica/main
created: '2024-04-14'
description: Enhance your own applications with fast, reliable access to the data that powers our newsroom.
finops:
- name: Propublica Finops
  service_category: API
  slug: propublica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/propublica.png
layout: provider
modified: '2026-04-28'
name: ProPublica Data Store
nav: Providers
network: true
overview: 'ProPublica Data Store publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Journalism, and News.


  ProPublica Data Store''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Propublica Plans Pricing
  plan_count: 3
  slug: propublica-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Propublica Rate Limits
  slug: propublica-rate-limits
score:
  band: emerging
  composite: 11.0
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
    operational_transparency: 10.5
  previous_composite: 11.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propublica/refs/heads/main/screenshots/propublica-2026-06-20T192215.png
security:
- kind: domain-security
  name: Propublica Domain Security
  slug: propublica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: propublica
tags:
- Data
- Journalism
- News
---
