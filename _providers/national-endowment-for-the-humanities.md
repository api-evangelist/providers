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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Funded Project Query Form API exposing programmatic access to NEH grant records. Documentation is published as a PDF describing query parameters and response structure.
  name: NEH Funded Project Query API
  slug: funded-project-query
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-endowment-for-the-humanities-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-endowment-for-the-humanities
- group: company
  title: ''
  type: Website
  url: https://www.neh.gov/
- group: other
  title: ''
  type: OpenData
  url: https://www.neh.gov/data
- group: other
  title: ''
  type: BulkData
  url: https://securegrants.neh.gov/open/data/
- group: operate
  title: ''
  type: Contact
  url: https://www.neh.gov/about/contact
created: '2024-12-03'
description: The National Endowment for the Humanities (NEH) is the nation's largest public funder of the humanities, which include history, philosophy, literature, language, ethics, law, archaeology, political theory, comparative religion, anthropology, sociology, and media and cultural studies. NEH does not publish a fully documented public REST API, but it offers a Funded Project Query Form API and bulk XML datasets covering all grants awarded since 1965, plus evaluator and panelist information from 1988 onward.
finops:
- name: National Endowment For The Humanities Finops
  service_category: API
  slug: national-endowment-for-the-humanities-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-endowment-for-the-humanities.png
layout: provider
modified: '2026-04-28'
name: National Endowment for the Humanities
nav: Providers
network: true
overview: National Endowment for the Humanities publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Humanities, Grants, and Open Data.
plans:
- name: National Endowment For The Humanities Plans Pricing
  plan_count: 3
  slug: national-endowment-for-the-humanities-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: National Endowment For The Humanities Rate Limits
  slug: national-endowment-for-the-humanities-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-endowment-for-the-humanities/refs/heads/main/screenshots/national-endowment-for-the-humanities-2026-06-20T190014.png
security:
- kind: domain-security
  name: National Endowment For The Humanities Domain Security
  slug: national-endowment-for-the-humanities-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-endowment-for-the-humanities
tags:
- Federal-Government
- Humanities
- Grants
- Open Data
website: https://www.neh.gov/
---
