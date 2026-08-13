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
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The Southwest Gas My Account API powers the online customer portal and mobile application for natural gas utility customers in Arizona, Nevada, and California. Customers can view usage history, pay bi
  name: Southwest Gas My Account API
  slug: southwest-gas-my-account-api
- description: The Southwest Gas Agency Portal provides access for charitable organizations and assistance agencies to look up customer accounts and submit utility assistance pledges on behalf of customers in need.
  name: Southwest Gas Agency Portal API
  slug: southwest-gas-agency-portal-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southwest-gas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swgas.com
- group: start
  title: ''
  type: Customer Portal
  url: https://myaccount.swgas.com/
- group: start
  title: ''
  type: Agency Portal
  url: https://agency.swgas.com/Portal/
- group: other
  title: ''
  type: Mobile App
  url: https://www.swgas.com/en/mobile-app
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.swgasholdings.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southwest-gas
- group: other
  title: ''
  type: X
  url: https://twitter.com/SouthwestGas
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/json-ld/southwest-gas-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/vocabulary/southwest-gas-vocabulary.yml
created: '2026-03-24'
description: Southwest Gas Holdings is a natural gas distribution company that purchases, distributes, and transports natural gas for customers in Arizona, Nevada, and California. As a Fortune 1000 utility company headquartered in Las Vegas, Nevada, Southwest Gas serves over 2 million customers through its regulated utility segment and also operates Centuri Group, a full-service utility infrastructure services company.
examples:
- key_count: 12
  name: Southwest Gas Account Example
  slug: southwest-gas-account-example
- key_count: 11
  name: Southwest Gas Usage Example
  slug: southwest-gas-usage-example
finops:
- name: Southwest Gas Finops
  service_category: Utility (Natural Gas)
  slug: southwest-gas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southwest-gas.png
json_schemas:
- name: Southwest Gas Customer Account
  property_count: 12
  slug: southwest-gas-account
- name: Southwest Gas Usage Record
  property_count: 11
  slug: southwest-gas-usage
json_structures:
- name: Southwest Gas Account Structure
  property_count: 0
  slug: southwest-gas-account-structure
jsonld:
- class_count: 8
  name: Southwest Gas Context
  property_count: 13
  slug: southwest-gas-context
layout: provider
modified: '2026-05-02'
name: Southwest Gas
nav: Providers
network: true
overview: 'Southwest Gas publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Natural Gas, Utility, and Energy.


  The Southwest Gas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Southwest Gas Plans Pricing
  plan_count: 1
  slug: southwest-gas-plans-pricing
press:
- date: '2026-05-25'
  title: Southwest Gas Holdings, Inc. Reports First Quarter 2026 ...
  url: https://www.prnewswire.com/news-releases/southwest-gas-holdings-inc-reports-first-quarter-2026-financial-results-affirms-full-year-2026-and-long-term-guidance-302761931.html
- date: '2026-05-25'
  title: Southwest Gas Holdings Announces Decision to Separate ...
  url: https://www.prnewswire.com/news-releases/southwest-gas-holdings-announces-decision-to-separate-centuri-creating-two-focused-independent-companies-to-unlock-value-for-stockholders-301493318.html
- date: '2026-05-25'
  title: Southwest Gas Gets Upgrade Ahead of Strong 2026 Earnings
  url: https://www.ainvest.com/news/southwest-gas-upgrade-strong-2026-earnings-2605/
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/92416/000169211520000031/swx0331208k.htm
- date: '2026-05-25'
  title: 2024 Sustainability Report
  url: https://www.swgas.com/1409224719685/SWG-2024-SR.pdf
random_paper: 54
rate_limits:
- limit_count: 1
  name: Southwest Gas Rate Limits
  slug: southwest-gas-rate-limits
rules:
- name: Southwest Gas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: southwest-gas-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 33.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 24.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/screenshots/southwest-gas-2026-06-20T194233.png
security:
- kind: domain-security
  name: Southwest Gas Domain Security
  slug: southwest-gas-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: southwest-gas
tags:
- Fortune 1000
- Natural Gas
- Utility
- Energy
website: https://www.swgas.com
---
