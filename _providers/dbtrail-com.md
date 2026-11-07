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
    mcp_server: documented
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
  score: 17.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API documented at https://dbtrail.com/docs/, providing access to analytical replica features.
  name: DBTrail API
  slug: dbtrail-api
- description: 'DBTrail API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DBTrail API
  slug: dbtrail-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/dbtrail-com/rules/dbtrail-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dbtrail-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dbtrail-com/vocabulary/dbtrail-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dbtrail-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dbtrail-com/conformance/dbtrail-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dbtrail-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dbtrail-com/hosts/dbtrail-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dbtrail-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dbtrail-com/vendors/dbtrail-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dbtrail-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dbtrail.com/docs/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dbtrail.com/docs/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dbtrail.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/dbtrail/dbtrail/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://dbtrail.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/dbtrail-com/security/dbtrail-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dbtrail-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dbtrail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dbtrail.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://blog.dbtrail.com/
created: '2026-11-05'
description: DBTrail provides a zero‑ETL analytical replica for MySQL, RDS and Aurora databases. It creates Parquet copies that capture every change, enabling time‑travel queries, row‑level undo, and fast analytics via DuckDB without impacting production workloads.
layout: provider
modified: '2026-11-05'
name: DBTrail
nav: Providers
network: true
overview: 'DBTrail is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Analytics, ETL, MySQL, and DuckDB.


  The DBTrail catalog on APIs.io includes 1 Spectral governance ruleset.


  DBTrail''s developer surface includes pricing, changelog, getting-started guide, documentation, engineering blog, and 9 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: DBTrail API Rules
  rule_count: 22
  severity_counts:
    error: 20
    hint: 0
    info: 1
    warn: 1
  slug: dbtrail-com-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dbtrail Com Domain Security
  slug: dbtrail-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dbtrail-com
tags:
- Database
- Analytics
- ETL
- MySQL
- DuckDB
website: https://dbtrail.com/
---
