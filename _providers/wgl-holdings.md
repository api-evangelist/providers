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
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: WGL Energy Services is an unregulated retail energy subsidiary of WGL Holdings that sells natural gas and electricity to commercial, industrial, and residential customers in Maryland, Virginia, Delawa
  name: WGL Energy Services
  slug: wgl-energy-services
- description: WGL Midstream, Inc. is a subsidiary of Washington Gas Resources engaged in acquiring and optimizing natural gas storage and transportation assets. It focuses on midstream energy services including gas
  name: WGL Midstream
  slug: wgl-midstream
- description: Hampshire Gas Company owns and operates interests in natural gas storage facilities in and around Hampshire County, West Virginia. It provides underground natural gas storage services that support pip
  name: Hampshire Gas
  slug: hampshire-gas
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wgl-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wgl
- group: company
  title: ''
  type: Website
  url: https://www.wglholdings.com
- group: other
  title: ''
  type: Parent Company
  url: https://www.altagas.ca
- group: other
  title: ''
  type: Washington Gas
  url: https://www.washingtongas.com
- group: other
  title: ''
  type: WGL Energy
  url: https://www.wglenergy.com
- group: other
  title: ''
  type: Sustainability
  url: https://sustainability.wglholdings.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/WGL_Holdings
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/vocabulary/wgl-holdings-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/json-ld/wgl-holdings-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/wgl-holdings/refs/heads/main/json-schema/wgl-holdings-customer-account-schema.json
created: '2026-03-24'
description: WGL Holdings was an integrated energy holding company headquartered in Washington, D.C., serving over 1 million customers across the District of Columbia, Maryland, and Virginia. Its operations spanned regulated natural gas distribution (Washington Gas), retail energy marketing (WGL Energy Services), commercial energy systems, and midstream energy services (WGL Midstream, Hampshire Gas). WGL Holdings was acquired by AltaGas on July 6, 2018, and continues to operate as a subsidiary.
finops:
- name: Wgl Holdings Finops
  service_category: API
  slug: wgl-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wgl-holdings.png
json_schemas:
- name: WGL Holdings Customer Account
  property_count: 10
  slug: wgl-holdings-customer-account
json_structures:
- name: Wgl Holdings Customer Account Structure
  property_count: 0
  slug: wgl-holdings-customer-account-structure
jsonld:
- class_count: 39
  name: Wgl Holdings Context
  property_count: 0
  slug: wgl-holdings-context
layout: provider
modified: '2026-07-25'
name: WGL Holdings
nav: Providers
network: true
overview: 'WGL Holdings publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Natural Gas, Utilities, Electricity, and Retail Energy.


  The WGL Holdings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Wgl Holdings Plans Pricing
  plan_count: 3
  slug: wgl-holdings-plans-pricing
press:
- date: '2026-05-25'
  title: Ronald Blauch - WGL Holdings Inc
  url: https://www.linkedin.com/in/ronald-blauch-84b339122
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/0001561894/000156189424000038/hasi-20240404.htm
- date: '2026-05-25'
  title: Dissecting Corporate Culture Using Generative AI
  url: https://www.ecgi.global/sites/default/files/Paper%3A%20Dissecting%20Corporate%20Culture%20Using%20Generative%20AI%20%20%E2%80%93%20Insights%20from%20Analyst%20Reports.pdf
- date: '2026-05-25'
  title: Visteon Set to Join S&P MidCap 400
  url: https://www.prnewswire.com/news-releases/visteon-set-to-join-sp-midcap-400-300676803.html
- date: '2026-05-25'
  title: Climate and Energy
  url: https://www.asyousow.org/our-work/climate-and-energy
random_paper: 13
rate_limits:
- limit_count: 5
  name: Wgl Holdings Rate Limits
  slug: wgl-holdings-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WGL Holdings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wgl-holdings-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.0
  delta: 1.3
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Wgl Holdings Domain Security
  slug: wgl-holdings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wgl-holdings
tags:
- Energy
- Natural Gas
- Utilities
- Electricity
- Retail Energy
- Midstream
- Fortune 1000
website: https://www.wglholdings.com
---
