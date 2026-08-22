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
- description: FHFA provides housing finance data datasets including house price indexes and other housing market statistics.
  name: Federal Housing Finance Agency
  slug: federal-housing-finance-agency
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-housing-finance-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fhfa
- group: company
  title: ''
  type: Website
  url: https://www.fhfa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fhfa.gov/data/datasets
created: '2024-12-03'
description: The Federal Housing Finance Agency (FHFA) is an independent agency that was established by the Housing and Economic Recovery Act of 2008 (HERA). The agency is responsible for the effective supervision, regulation, and oversight of the housing mission of Fannie Mae, Freddie Mac, and the Federal Home Loan Bank System.
finops:
- name: Federal Housing Finance Agency Finops
  service_category: API
  slug: federal-housing-finance-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-housing-finance-agency.png
layout: provider
modified: '2026-04-28'
name: Federal Housing Finance Agency
nav: Providers
network: true
overview: 'Federal Housing Finance Agency publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Finance, and Housing.


  Federal Housing Finance Agency''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Federal Housing Finance Agency Plans Pricing
  plan_count: 3
  slug: federal-housing-finance-agency-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Federal Housing Finance Agency Rate Limits
  slug: federal-housing-finance-agency-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: -1.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-housing-finance-agency/refs/heads/main/screenshots/federal-housing-finance-agency-2026-06-20T181116.png
security:
- kind: domain-security
  name: Federal Housing Finance Agency Domain Security
  slug: federal-housing-finance-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-housing-finance-agency
tags:
- Federal Government
- Finance
- Housing
website: https://www.fhfa.gov/
---
