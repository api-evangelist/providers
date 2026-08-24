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
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: API for accessing Peace Corps volunteer statistics, country programs, and development data.
  name: Peace Corps Data API
  slug: peace-corps-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peace-corps-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peacecorps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peace-corps
- group: company
  title: ''
  type: Website
  url: https://www.peacecorps.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peacecorps.gov/privacy/
created: '2026-03-16'
description: The Peace Corps is a U.S. government agency that sends American volunteers abroad to work with communities on development projects. They provide data APIs for accessing Peace Corps volunteer data, country information, and project statistics.
finops:
- name: Peace Corps Finops
  service_category: API
  slug: peace-corps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peace-corps.png
layout: provider
modified: '2026-04-28'
name: Peace Corps
nav: Providers
network: true
overview: Peace Corps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, International Development, and Volunteers.
plans:
- name: Peace Corps Plans Pricing
  plan_count: 3
  slug: peace-corps-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Peace Corps Rate Limits
  slug: peace-corps-rate-limits
score:
  band: emerging
  composite: 11.1
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peace-corps/refs/heads/main/screenshots/peace-corps-2026-06-20T191524.png
security:
- kind: domain-security
  name: Peace Corps Domain Security
  slug: peace-corps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: peace-corps
tags:
- Government
- International Development
- Volunteers
website: https://www.peacecorps.gov/
---
