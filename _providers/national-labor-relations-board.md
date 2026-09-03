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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: NLRB case data including Unfair Labor Practice and Elections data from the Case Activity Tracking System available on data.gov.
  name: National Labor Relations Board
  slug: national-labor-relations-board
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-labor-relations-board-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-labor-relations-board
- group: company
  title: ''
  type: Website
  url: https://www.nlrb.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.nlrb.gov/data-on-datagov
created: '2024-12-03'
description: The National Labor Relations Board (NLRB) is an independent federal agency responsible for protecting the rights of employees and employers in the United States. The NLRB administers the National Labor Relations Act, which guarantees the rights of employees to form unions and engage in collective bargaining with their employers.
finops:
- name: National Labor Relations Board Finops
  service_category: API
  slug: national-labor-relations-board-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-labor-relations-board.png
layout: provider
modified: '2026-04-28'
name: National Labor Relations Board
nav: Providers
network: true
overview: 'National Labor Relations Board publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Employment, Federal-Government, and Labor.


  National Labor Relations Board''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: National Labor Relations Board Plans Pricing
  plan_count: 3
  slug: national-labor-relations-board-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: National Labor Relations Board Rate Limits
  slug: national-labor-relations-board-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-labor-relations-board/refs/heads/main/screenshots/national-labor-relations-board-2026-06-20T190031.png
security:
- kind: domain-security
  name: National Labor Relations Board Domain Security
  slug: national-labor-relations-board-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: national-labor-relations-board
tags:
- Employment
- Federal-Government
- Labor
website: https://www.nlrb.gov/
---
