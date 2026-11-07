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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cryptosieve Com Agentic Access
  operation_count: 4
  slug: cryptosieve-com-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: AI Business Agent Backend providing SaaS query, YouTube transcript, and chat endpoints.
  name: CryptoSieve API
  slug: cryptosieve-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/cryptosieve-com/agentic-access/cryptosieve-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptosieve-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cryptosieve-com/rules/cryptosieve-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptosieve-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptosieve-com/json-ld/cryptosieve-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cryptosieve-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptosieve-com/vocabulary/cryptosieve-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptosieve-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cryptosieve-com/data-model/cryptosieve-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cryptosieve-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cryptosieve-com/errors/cryptosieve-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cryptosieve-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cryptosieve-com/conformance/cryptosieve-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptosieve-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/cryptosieve-com/hosts/cryptosieve-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptosieve-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptosieve-com/vendors/cryptosieve-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptosieve-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cryptosieve-com/security/cryptosieve-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptosieve-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptosieve.com/
created: '2026-11-04'
description: CryptoSieve provides an advanced Bollinger Band screener and crypto scanner to find breakout opportunities across multiple timeframes and exchanges. Users can set alerts for tight BBW signals, leveraging powerful analytics to monitor the crypto market efficiently.
jsonld:
- class_count: 4
  name: Cryptosieve Com Context
  property_count: 11
  slug: cryptosieve-com-context
layout: provider
modified: '2026-11-04'
name: CryptoSieve
nav: Providers
network: true
overview: 'CryptoSieve is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Screener, Bollinger-Band, Crypto-Analytics, and Alerts.


  The CryptoSieve catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: CryptoSieve API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: cryptosieve-com-rules
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptosieve Com Domain Security
  slug: cryptosieve-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cryptosieve-com
tags:
- Cryptocurrency
- Screener
- Bollinger-Band
- Crypto-Analytics
- Alerts
website: https://cryptosieve.com/
---
