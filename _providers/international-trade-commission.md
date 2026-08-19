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
- description: The USITC DataWeb provides interactive access to U.S. international trade statistics and U.S. tariff data, including imports, exports, and production by commodity and country.
  name: USITC DataWeb
  slug: usitc-dataweb
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/international-trade-commission-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usitc.gov/
- group: other
  title: ''
  type: Data
  url: https://www.usitc.gov/data/index.htm
created: '2024-12-03'
description: The United States International Trade Commission (USITC) is an independent, nonpartisan, quasi-judicial federal agency that fulfills a range of trade-related mandates. The USITC provides high-quality analysis of international trade issues to the President and the Congress, and serves as the primary forum for the adjudication of intellectual property and trade disputes. The agency exposes U.S. trade and tariff statistics through the USITC DataWeb interactive data service.
finops:
- name: International Trade Commission Finops
  service_category: API
  slug: international-trade-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/international-trade-commission.png
layout: provider
modified: '2026-04-28'
name: International Trade Commission
nav: Providers
network: true
overview: 'International Trade Commission publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Government Data, Intellectual Property, Trade, and Tariffs.


  The International Trade Commission catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: International Trade Commission Plans Pricing
  plan_count: 3
  slug: international-trade-commission-plans-pricing
random_paper: 127
rate_limits:
- limit_count: 5
  name: International Trade Commission Rate Limits
  slug: international-trade-commission-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: International Trade Commission API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: international-trade-commission-rules
score:
  band: minimal
  composite: 9.4
  delta: -2.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/screenshots/international-trade-commission-2026-06-20T183500.png
security:
- kind: domain-security
  name: International Trade Commission Domain Security
  slug: international-trade-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: international-trade-commission
tags:
- Federal Government
- Government Data
- Intellectual Property
- Trade
- Tariffs
website: https://www.usitc.gov/
---
