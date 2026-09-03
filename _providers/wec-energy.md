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
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: Web and mobile API powering the WEC Energy Group customer self-service portal. Enables customers to view account information, pay bills, manage alerts, view energy usage history, and report outages. A
  name: WEC Energy Group Customer Portal API
  slug: wec-energy-group-customer-portal-api
- description: 'Green Button is a standardized API for accessing customer energy usage data. Based on the ESPI (Energy Services Provider Interface) standard, it allows customers to authorize third-party applications '
  name: Green Button Energy Usage Data API
  slug: green-button-energy-usage-data-api
- description: Real-time electricity outage information for We Energies service territory in Wisconsin. Provides geographic outage data, estimated restoration times, and affected customer counts. Powers the public-f
  name: We Energies Outage Map API
  slug: we-energies-outage-map-api
- description: Customer account and billing API for Peoples Gas, serving natural gas customers in the Chicago metropolitan area. Supports account management, bill payment, usage history, and service requests.
  name: Peoples Gas Customer Service API
  slug: peoples-gas-customer-service-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wec-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wecenergygroup.com
- group: start
  title: ''
  type: Customer Portal
  url: https://www.we-energies.com/
- group: start
  title: ''
  type: Peoples Gas Portal
  url: https://www.peoplesgas.com/
- group: start
  title: ''
  type: Wisconsin Public Service Portal
  url: https://www.wisconsinpublicservice.com/
- group: company
  title: ''
  type: Press Room
  url: https://www.wecenergygroup.com/newsroom/
- group: company
  title: ''
  type: Investor Relations
  url: https://www.wecenergygroup.com/investor-relations/
- group: company
  title: ''
  type: Careers
  url: https://careers.wecenergygroup.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.wecenergygroup.com/sustainability/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.we-energies.com/help/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wecenergygroup.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wec-energy-group
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/WECEnergyGroup
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wec-energy-vocabulary.yml
created: '2024'
description: 'WEC Energy Group (NYSE: WEC) is one of the nation''s premier energy companies, serving 4.4 million customers across Wisconsin, Illinois, Michigan, and Minnesota with electricity and natural gas service. The company operates through regional utilities including We Energies, Wisconsin Public Service, Peoples Gas, North Shore Gas, Minnesota Energy Resources, Michigan Gas Utilities, and Upper Michigan Energy Resources. WEC Energy Group offers customer-facing digital services including account management portals, mobile apps, and Green Button energy usage data access.'
examples:
- key_count: 13
  name: Wec Energy Usage Example
  slug: wec-energy-usage-example
finops:
- name: Wec Energy Finops
  service_category: Energy / Utility
  slug: wec-energy-finops
image: https://www.wecenergygroup.com/images/wec-logo.png
json_schemas:
- name: WEC Energy Group Customer Account
  property_count: 16
  slug: wec-energy-account
- name: WEC Energy Group Outage Event
  property_count: 11
  slug: wec-energy-outage
- name: WEC Energy Group Energy Usage Data
  property_count: 10
  slug: wec-energy-usage
json_structures:
- name: Wec Energy Account Structure
  property_count: 0
  slug: wec-energy-account-structure
jsonld:
- class_count: 0
  name: Wec Energy Context
  property_count: 23
  slug: wec-energy-context
layout: provider
modified: '2026-07-25'
name: WEC Energy Group
nav: Providers
network: true
overview: 'WEC Energy Group publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electric Utility, Fortune 500, Green Button, and Illinois.


  The WEC Energy Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Wec Energy Plans Pricing
  plan_count: 1
  slug: wec-energy-plans-pricing
press:
- date: '2026-05-25'
  title: WEC Energy Group posts 2025 results
  url: https://www.prnewswire.com/news-releases/wec-energy-group-posts-2025-results-302679311.html
- date: '2026-05-25'
  title: Exhibit 99.1
  url: https://www.sec.gov/Archives/edgar/data/783325/000078332526000049/a2026q1wecearningsreleasee.htm
- date: '2026-05-25'
  title: Planned Data Centers Drive Up WEC Proposed Capex
  url: https://www.industrialinfo.com/news/article/planned-data-centers-drive-up-wec-proposed-capex-again--353394
- date: '2026-05-25'
  title: WEC Energy Group outlines $37.5B growth plan
  url: https://www.stocktitan.net/sec-filings/WEC/8-k-wec-energy-group-inc-reports-material-event-7785f9bfac06.html
- date: '2026-05-25'
  title: WEC Energy Group announces plan to increase dividend by ...
  url: https://investor.wecenergygroup.com/investors/news-releases/press-release-details/2025/WEC-Energy-Group-announces-plan-to-increase-dividend-by-6-7-percent/default.aspx
random_paper: 6
rate_limits:
- limit_count: 1
  name: Wec Energy Rate Limits
  slug: wec-energy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WEC Energy Group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wec-energy-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 55.6
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wec-energy/refs/heads/main/screenshots/wec-energy-2026-06-20T201339.png
security:
- kind: domain-security
  name: Wec Energy Domain Security
  slug: wec-energy-domain-security
  summary_line: TLSv1.2 · DMARC
slug: wec-energy
tags:
- Energy
- Electric Utility
- Fortune 500
- Green Button
- Illinois
- Michigan
- Minnesota
- Natural Gas
- NYSE
- Utility
- Wisconsin
website: https://www.wecenergygroup.com
---
