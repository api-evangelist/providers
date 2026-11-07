---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Dubai Data API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dubai Data API
  slug: datadubai-ae-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/datadubai-ae/rules/datadubai-ae-rules.yml
  title: ''
  type: Spectral
  url: rules/datadubai-ae-rules.yml
- group: design
  href: https://artifacts.apis.io/datadubai-ae/vocabulary/datadubai-ae-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datadubai-ae-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datadubai-ae/conformance/datadubai-ae-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datadubai-ae-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datadubai-ae/llms/datadubai-ae-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadubai-ae-llms.txt
- group: agent
  href: https://artifacts.apis.io/datadubai-ae/well-known/datadubai-ae-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datadubai-ae-well-known.yml
- group: other
  href: https://artifacts.apis.io/datadubai-ae/hosts/datadubai-ae-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datadubai-ae-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datadubai.ae/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datadubai.ae/developers/
- group: auth
  href: https://artifacts.apis.io/datadubai-ae/security/datadubai-ae-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadubai-ae-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datadubai.ae/
created: '2026-11-04'
description: Dubai Data provides a public data platform on the Dubai property market, aggregating registered sales, prices, yields and other real‑estate metrics from the Dubai Land Department. The service offers open methodology, downloadable datasets in JSON and CSV, and interactive tools for market analysis, helping investors, developers and the public understand trends across Dubai’s real‑estate sector.
image: https://datadubai.ae/og-default.png
layout: provider
modified: '2026-11-04'
name: Dubai Data
nav: Providers
network: true
overview: 'Dubai Data is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Data Platform, Dubai, and Property Market.


  The Dubai Data catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: Dubai Data API Rules
  rule_count: 22
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 2
  slug: datadubai-ae-rules
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datadubai Ae Domain Security
  slug: datadubai-ae-domain-security
  summary_line: TLSv1.3
slug: datadubai-ae
tags:
- Company
- Real Estate
- Data Platform
- Dubai
- Property Market
- Open Data
website: https://datadubai.ae/
---
