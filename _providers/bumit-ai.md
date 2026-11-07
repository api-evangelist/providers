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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Trust infrastructure API for Swiss business verification.
  name: BUMIT API
  slug: bumit-api
- baseURL: https://bumit.ai
  baseurl_source: declared
  description: Trust infrastructure for business and autonomous transactions. BUMIT verifies Swiss businesses using authoritative evidence and returns deterministic, machine-readable decisions, reason codes, freshne
  name: BUMIT API V1 API
  slug: bumit-api-v1-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/bumit-ai/rules/bumit-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bumit-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bumit-ai/json-ld/bumit-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bumit-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bumit-ai/vocabulary/bumit-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bumit-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bumit-ai/conformance/bumit-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bumit-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/bumit-ai/data-model/bumit-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bumit-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/bumit-ai/errors/bumit-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bumit-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bumit-ai/llms/bumit-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bumit-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bumit-ai/well-known/bumit-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bumit-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bumit-ai/hosts/bumit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bumit-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bumit-ai/vendors/bumit-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bumit-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bumit.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://bumit.ai/support
- group: operate
  title: ''
  type: StatusPage
  url: https://bumit.ai/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bumit.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://bumit.ai/integrations/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://bumit.ai/docs
- group: auth
  href: https://artifacts.apis.io/bumit-ai/security/bumit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bumit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bumit.ai/
created: '2026-11-03'
description: BUMIT provides a trust infrastructure for business transactions, focusing on deterministic verification of Swiss companies. It offers REST/JSON APIs that return structured checks, provenance, and deterministic decisions on compliance, sanctions, and regulatory status. The platform integrates authoritative evidence sources and deterministic rule sets to deliver transparent outcomes for KYB and risk assessment use cases.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_32e24b3qst8c0a1rj8y4h04g3r/df271b5325e304ff362db4e3b5cd3f17_1793514545052.png
json_schemas:
- name: BusinessVerificationResponse
  property_count: 15
  slug: bumit-ai-business-verification-response
- name: CompanyEventsResponse
  property_count: 16
  slug: bumit-ai-company-events-response
- name: CompanyResult
  property_count: 8
  slug: bumit-ai-company-result
- name: CompanySanctionsResponse
  property_count: 24
  slug: bumit-ai-company-sanctions-response
- name: CompanySearchResult
  property_count: 9
  slug: bumit-ai-company-search-result
- name: DiscoveryIndex
  property_count: 12
  slug: bumit-ai-discovery-index
jsonld:
- class_count: 38
  name: Bumit Ai Context
  property_count: 187
  slug: bumit-ai-context
layout: provider
modified: '2026-11-03'
name: BUMIT
nav: Providers
network: true
overview: 'BUMIT publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Company, Trust, Verification, and Swiss.


  The BUMIT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BUMIT''s developer surface includes support, getting-started guide, API reference, and 15 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: BUMIT API Rules
  rule_count: 46
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 4
  slug: bumit-ai-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bumit Ai Domain Security
  slug: bumit-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bumit-ai
tags:
- Company
- Trust
- Verification
- Swiss
website: https://bumit.ai/
---
