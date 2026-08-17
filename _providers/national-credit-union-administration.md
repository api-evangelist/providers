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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The NCUA publishes downloadable Call Report data, Financial Performance Reports, and a Research a Credit Union tool. There is no documented public REST API at this time; data is available as downloada
  name: NCUA Data and Call Reports
  slug: ncua-data
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-credit-union-administration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-credit-union-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-credit-union-administration
- group: company
  title: ''
  type: Website
  url: https://www.ncua.gov/
- group: start
  title: ''
  type: Portal
  url: https://ncua.gov/data
- group: other
  title: ''
  type: Locator
  url: https://mapping.ncua.gov/
- group: operate
  title: ''
  type: Contact
  url: mailto:BImail@ncua.gov
created: '2024-12-03'
description: Created by the U.S. Congress in 1970, the National Credit Union Administration is an independent federal agency that insures deposits at federally insured credit unions, protects the members who own credit unions, and charters and regulates federal credit unions. NCUA publishes Call Report and Financial Performance data and a Credit Union Locator, but does not currently document a public REST API.
finops:
- name: National Credit Union Administration Finops
  service_category: API
  slug: national-credit-union-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-credit-union-administration.png
layout: provider
modified: '2026-04-28'
name: National Credit Union Administration
nav: Providers
network: true
overview: 'National Credit Union Administration publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Credit Unions, Federal Government, Finance, and Banking.


  National Credit Union Administration''s developer surface includes developer portal and 6 more developer resources.'
plans:
- name: National Credit Union Administration Plans Pricing
  plan_count: 3
  slug: national-credit-union-administration-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 5
  name: National Credit Union Administration Rate Limits
  slug: national-credit-union-administration-rate-limits
score:
  band: minimal
  composite: 11.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-credit-union-administration/refs/heads/main/screenshots/national-credit-union-administration-2026-06-20T190008.png
security:
- kind: domain-security
  name: National Credit Union Administration Domain Security
  slug: national-credit-union-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: National Credit Union Administration Vulnerability Disclosure
  slug: national-credit-union-administration-vulnerability-disclosure
  summary_line: Bugcrowd
slug: national-credit-union-administration
tags:
- Credit Unions
- Federal Government
- Finance
- Banking
website: https://www.ncua.gov/
---
