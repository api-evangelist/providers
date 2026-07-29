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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Southwestern Energy investor relations portal provides financial data, shareholder information, earnings summaries, SEC filings, and corporate governance information. The investor relations infras
  name: Southwestern Energy Investor Relations API
  slug: southwestern-energy-investor-relations-api
- description: Following the merger, Expand Energy Corporation's investor relations portal provides access to combined company financial data, earnings releases, SEC filings, and investor presentations for the merge
  name: Expand Energy Investor Relations API
  slug: expand-energy-investor-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southwestern-energy-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.expandenergy.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.swn.com
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.swn.com/
- group: other
  title: ''
  type: Expand Energy
  url: https://www.expandenergy.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southwestern-energy
- group: other
  title: ''
  type: X
  url: https://twitter.com/SWNenergy
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/json-ld/southwestern-energy-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/vocabulary/southwestern-energy-vocabulary.yml
created: '2026-03-24'
description: Southwestern Energy Company (SWN) is one of the largest producers of natural gas in the United States, with exploration and production operations focused primarily on the Marcellus and Haynesville shales. In October 2024, Southwestern Energy completed a merger with Expand Energy Corporation (formerly Chesapeake Energy), though the SWN brand and investor relations infrastructure continues to operate under swn.com. As a Fortune 500 energy company, SWN focuses on responsible development of natural gas resources in the Appalachian Basin and Gulf Coast regions.
examples:
- key_count: 10
  name: Southwestern Energy Production Example
  slug: southwestern-energy-production-example
finops:
- name: Southwestern Energy Finops
  service_category: Energy (Upstream Natural Gas)
  slug: southwestern-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southwestern-energy.png
json_schemas:
- name: Southwestern Energy Natural Gas Production Record
  property_count: 10
  slug: southwestern-energy-production
json_structures:
- name: Southwestern Energy Production Structure
  property_count: 0
  slug: southwestern-energy-production-structure
jsonld:
- class_count: 8
  name: Southwestern Energy Context
  property_count: 13
  slug: southwestern-energy-context
layout: provider
modified: '2026-05-02'
name: Southwestern Energy
nav: Providers
network: true
overview: 'Southwestern Energy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Natural Gas, Energy, and Oil And Gas.


  The Southwestern Energy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Southwestern Energy''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Southwestern Energy Plans Pricing
  plan_count: 1
  slug: southwestern-energy-plans-pricing
press:
- date: '2026-05-25'
  title: Chesapeake to become top US natural gas producer with ...
  url: https://www.reuters.com/markets/deals/chesapeake-buy-southwestern-energy-74-billion-deal-2024-01-11/
- date: '2026-05-25'
  title: Industry Veterans Unite Operations, Chart Course As ...
  url: https://www.aogr.com/magazine/editors-choice/industry-veterans-unite-operations-chart-course-as-expand-energy
- date: '2026-05-25'
  title: Chesapeake Energy Corporation and Southwestern ...
  url: https://www.prnewswire.com/news-releases/chesapeake-energy-corporation-and-southwestern-energy-company-combination-expected-to-close-in-the-first-week-of-october-302259328.html
- date: '2026-05-25'
  title: tm243657-1_s4 - none - 58.1072356s
  url: https://www.sec.gov/Archives/edgar/data/895126/000110465924029464/tm243657-1_s4.htm
- date: '2026-05-25'
  title: Chesapeake Energy Corp. is buying Southwestern ...
  url: https://www.facebook.com/Investopedia/posts/chesapeake-energy-corp-is-buying-southwestern-energy-co-to-become-the-largest-na/765851035566707/
random_paper: 59
rate_limits:
- limit_count: 1
  name: Southwestern Energy Rate Limits
  slug: southwestern-energy-rate-limits
rules:
- name: Southwestern Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: southwestern-energy-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.9
  delta: -7.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 27.4
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 34.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/screenshots/southwestern-energy-2026-06-20T194233.png
security:
- kind: domain-security
  name: Southwestern Energy Domain Security
  slug: southwestern-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: southwestern-energy
tags:
- Fortune 500
- Natural Gas
- Energy
- Oil And Gas
website: https://www.swn.com
---
