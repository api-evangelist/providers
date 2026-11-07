---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AgentReady API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentReady API
  slug: agentready-market-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/agentready-market/plans/agentready-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentready-market-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentready-market/rules/agentready-market-rules.yml
  title: ''
  type: Spectral
  url: rules/agentready-market-rules.yml
- group: design
  href: https://artifacts.apis.io/agentready-market/json-ld/agentready-market-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentready-market-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentready-market/vocabulary/agentready-market-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentready-market-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentready-market/data-model/agentready-market-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentready-market-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentready-market/conformance/agentready-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentready-market-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentready-market/llms/agentready-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentready-market-llms.txt
- group: other
  href: https://artifacts.apis.io/agentready-market/a2a/agentready-market-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentready-market-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentready-market/well-known/agentready-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentready-market-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentready-market/hosts/agentready-market-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentready-market-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentready-market/vendors/agentready-market-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentready-market-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentready-market/packages/agentready-market-packages.yml
  title: ''
  type: SDKs
  url: packages/agentready-market-packages.yml
- group: build
  href: https://artifacts.apis.io/agentready-market/packages/agentready-market-packages.yml
  title: ''
  type: Packages
  url: packages/agentready-market-packages.yml
- group: auth
  href: https://artifacts.apis.io/agentready-market/security/agentready-market-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentready-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentready.market/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agentready.market/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentready.market/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.agentready.market/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentready.market/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.agentready.market/research
- group: operate
  title: ''
  type: Support
  url: https://www.agentready.market/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentready.market/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentready.market/privacy
created: '2026-11-01'
description: AgentReady provides an AI‑agent readiness audit for e‑commerce stores, scoring how well an autonomous agent can discover, understand and purchase on a site. The free scan gives a /100 score, identifies gaps, and offers a Pro plan with unlimited scans, detailed roadmaps, and monitoring. The service is operated by Villepinte Studio in the Netherlands and is not affiliated with other similarly named products.
image: https://www.agentready.market/static/scanner/og.a7cc16c6288e.png
json_schemas:
- name: GetApiScanResponse
  property_count: 7
  slug: agentready-market-get-api-scan-response
- name: GetApiV1ScanScanidBriefMdResponse
  property_count: 1
  slug: agentready-market-get-api-v1-scan-scanid-brief-md-response
- name: GetApiV1ScanScanidResponse
  property_count: 3
  slug: agentready-market-get-api-v1-scan-scanid-response
- name: PostApiReportsRequest
  property_count: 1
  slug: agentready-market-post-api-reports-request
- name: PostApiReportsResponse
  property_count: 9
  slug: agentready-market-post-api-reports-response
jsonld:
- class_count: 5
  name: Agentready Market Context
  property_count: 17
  slug: agentready-market-context
layout: provider
modified: '2026-11-01'
name: AgentReady
nav: Providers
network: true
overview: 'AgentReady is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, E-Commerce, Audit, Software-as-a-Service, and Netherlands.


  The AgentReady catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentReady''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Agentready Market Plans Pricing
  plan_count: 2
  slug: agentready-market-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AgentReady API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentready-market-rules
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 35.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentready Market Domain Security
  slug: agentready-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentready-market
tags:
- Artificial Intelligence
- E-Commerce
- Audit
- Software-as-a-Service
- Netherlands
website: https://www.agentready.market/
---
