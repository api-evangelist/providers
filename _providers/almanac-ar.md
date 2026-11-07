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
    error_semantics: documented
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Almanac commercial API for reports and datasets
  name: Almanac API
  slug: almanac-api
- baseURL: https://api.almanac.ar
  baseurl_source: declared
  description: 'API comercial de Almanac — Informe por CUIT (Reports/Account) + Datasets (catálogo público y descarga de snapshots). Autenticación por API key (`Authorization: Bearer alm_`, generada en https://almana'
  name: Almanac API V1 API
  slug: almanac-api-v1-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/almanac-ar/rules/almanac-ar-rules.yml
  title: ''
  type: Spectral
  url: rules/almanac-ar-rules.yml
- group: design
  href: https://artifacts.apis.io/almanac-ar/json-ld/almanac-ar-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/almanac-ar-context.jsonld
- group: design
  href: https://artifacts.apis.io/almanac-ar/vocabulary/almanac-ar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/almanac-ar-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/almanac-ar/conventions/almanac-ar-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/almanac-ar-conventions.yml
- group: design
  href: https://artifacts.apis.io/almanac-ar/conventions/almanac-ar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/almanac-ar-conventions.yml
- group: design
  href: https://artifacts.apis.io/almanac-ar/conformance/almanac-ar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/almanac-ar-conformance.yml
- group: design
  href: https://artifacts.apis.io/almanac-ar/data-model/almanac-ar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/almanac-ar-data-model.yml
- group: auth
  href: https://artifacts.apis.io/almanac-ar/security/almanac-ar-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/almanac-ar-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/almanac-ar/errors/almanac-ar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/almanac-ar-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/almanac-ar/well-known/almanac-ar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/almanac-ar-security.txt
- group: agent
  href: https://artifacts.apis.io/almanac-ar/well-known/almanac-ar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/almanac-ar-well-known.yml
- group: other
  href: https://artifacts.apis.io/almanac-ar/hosts/almanac-ar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/almanac-ar-hosts.yml
- group: other
  href: https://artifacts.apis.io/almanac-ar/vendors/almanac-ar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/almanac-ar-vendors.yml
- group: auth
  href: https://artifacts.apis.io/almanac-ar/security/almanac-ar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/almanac-ar-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/almanac-ar/security/almanac-ar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/almanac-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://almanac.ar/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://almanac.ar/developers
- group: docs
  title: ''
  type: Documentation
  url: https://almanac.ar/developers/api
- group: docs
  title: ''
  type: APIReference
  url: https://almanac.ar/developers/api
- group: start
  title: ''
  type: GettingStarted
  url: https://almanac.ar/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://almanac.ar/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://almanac.ar/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://almanac.ar/legal
created: '2026-11-01'
description: Almanac provides an AI‑native data catalog of official Argentine economic, financial and regulatory information. It aggregates sources such as BCRA, INDEC, CNV and MECON into a single searchable platform, offering datasets, metadata, SQL querying and alerts. The service aims to give developers and analysts reliable, up‑to‑date economic data for building applications and insights.
image: https://almanac.ar/og-image.png
json_schemas:
- name: BalanceResponse
  property_count: 2
  slug: almanac-ar-balance-response
- name: DatasetDetailResponse
  property_count: 19
  slug: almanac-ar-dataset-detail-response
- name: ReportPostResponse
  property_count: 8
  slug: almanac-ar-report-post-response
- name: ReportQuoteResponse
  property_count: 6
  slug: almanac-ar-report-quote-response
- name: ReportResult
  property_count: 4
  slug: almanac-ar-report-result
- name: SnapshotResponse
  property_count: 5
  slug: almanac-ar-snapshot-response
jsonld:
- class_count: 44
  name: Almanac Ar Context
  property_count: 100
  slug: almanac-ar-context
layout: provider
modified: '2026-11-01'
name: Almanac
nav: Providers
network: true
overview: 'Almanac publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Company.


  The Almanac catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Almanac''s developer surface includes documentation, API reference, getting-started guide, pricing, and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Almanac API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: almanac-ar-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 50.7
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 37.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Almanac Ar Domain Security
  slug: almanac-ar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Almanac Ar Vulnerability Disclosure
  slug: almanac-ar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: almanac-ar
tags:
- Company
website: https://almanac.ar/
---
