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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Commodity Futures Trading Commission Agentic Access
  operation_count: 7
  slug: commodity-futures-trading-commission-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'The CFTC oversees Swap Data Repositories (SDRs) that collect and maintain swap transaction records as required by the Dodd-Frank Act. SDRs publish certain real-time public data and the CFTC publishes '
  name: CFTC Swap Data Repositories
  slug: cftc-swap-data-repositories
- description: The CFTC publishes monthly Bank Participation reports and other aggregate large trader reports that complement the weekly COT data. These reports are released as PDFs and HTML tables on cftc.gov.
  name: CFTC Bank Participation and Large Trader Reports
  slug: cftc-large-trader-reporting
- baseURL: https://publicreporting.cftc.gov/resource
  baseurl_source: declared
  description: Commitments of Traders datasets
  name: Commodity Futures Trading Commission COT API
  slug: commodity-futures-trading-commission-cot-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CFTC Commitments of Traders (COT) SODA API
  slug: open-cftc-cot
- collection_type: open
  name: CFTC Commitments of Traders () SODA COT API
  slug: open-commodity-futures-trading-commission-cot-api
- collection_type: open
  name: CFTC Commitments of Traders () SODA COT Disaggregated API
  slug: open-commodity-futures-trading-commission-disaggregated-api
- collection_type: open
  name: CFTC Commitments of Traders () SODA COT Legacy API
  slug: open-commodity-futures-trading-commission-legacy-api
- collection_type: open
  name: CFTC Commitments of Traders () SODA COT Supplemental API
  slug: open-commodity-futures-trading-commission-supplemental-api
- collection_type: open
  name: CFTC Commitments of Traders () SODA COT TFF API
  slug: open-commodity-futures-trading-commission-tff-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commodity-futures-trading-commission-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commodity-futures-trading-commission-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commodity-futures-trading-commission
- group: company
  title: ''
  type: Website
  url: https://www.cftc.gov/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cftc-cot-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cftc-cot-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cftc-cot-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cftc-cot-rules.yml
- group: docs
  title: ''
  type: Documentation
  url: https://publicreporting.cftc.gov/
- group: docs
  title: ''
  type: Reference
  url: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cftc.gov/About/AbouttheCFTC/Privacy.html
created: '2024-12-03'
description: The Commodity Futures Trading Commission (CFTC) is the U.S. federal regulator for commodity futures and options markets. The CFTC publishes the weekly Commitments of Traders (COT) report and other public data through a Socrata Open Data API at publicreporting.cftc.gov, providing programmatic access to Legacy, Disaggregated, Traders in Financial Futures, and Supplemental Commodity Index Trader datasets, as well as swap data and large trader reports.
finops:
- name: Commodity Futures Trading Commission Finops
  service_category: API
  slug: commodity-futures-trading-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commodity-futures-trading-commission.png
json_schemas:
- name: CFTC Commitments of Traders Row
  property_count: 7
  slug: cftc-cot
jsonld:
- class_count: 0
  name: Cftc Cot Context
  property_count: 5
  slug: cftc-cot-context
layout: provider
modified: '2026-05-19'
name: Commodity Futures Trading Commission
nav: Providers
network: true
overview: 'Commodity Futures Trading Commission publishes 1 API on the [APIs.io](https://apis.io/) network: COT API. Tagged areas include CFTC, Commitments of Traders, Federal-Government, Financial, and Futures.


  The Commodity Futures Trading Commission catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Commodity Futures Trading Commission''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Commodity Futures Trading Commission Plans Pricing
  plan_count: 3
  slug: commodity-futures-trading-commission-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Commodity Futures Trading Commission Rate Limits
  slug: commodity-futures-trading-commission-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Commodity Futures Trading Commission API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: cftc-cot-rules
- effective_rule_count: 4
  extends: []
  name: Commodity Futures Trading Commission API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: commodity-futures-trading-commission-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 74.0
    catalog_earned_first_party: 0.0
    catalog_gap: 26.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 69.7
    contract_quality: 55.8
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 69.7
    operational_transparency: 7.9
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commodity-futures-trading-commission/refs/heads/main/screenshots/commodity-futures-trading-commission-2026-06-20T174817.png
security:
- kind: domain-security
  name: Commodity Futures Trading Commission Domain Security
  slug: commodity-futures-trading-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: commodity-futures-trading-commission
tags:
- CFTC
- Commitments of Traders
- Federal-Government
- Financial
- Futures
- Open Data
- SODA
- Trading
website: https://www.cftc.gov/
---
