---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP JSON-RPC API providing music catalog and licensing operations.
  name: AINSOF MCP
  slug: ainsof-mcp
- baseURL: https://mcp.ainsof.io
  baseurl_source: declared
  description: 'AINSOF API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AINSOF API
  slug: ainsof-io-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/ainsof-io/plans/ainsof-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ainsof-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ainsof-io/rules/ainsof-io-rules.yml
  title: ''
  type: Spectral
  url: rules/ainsof-io-rules.yml
- group: design
  href: https://artifacts.apis.io/ainsof-io/json-ld/ainsof-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ainsof-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/ainsof-io/vocabulary/ainsof-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ainsof-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ainsof-io/data-model/ainsof-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ainsof-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ainsof-io/authentication/ainsof-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ainsof-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/ainsof-io/conformance/ainsof-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ainsof-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ainsof-io/llms/ainsof-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ainsof-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/ainsof-io/well-known/ainsof-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ainsof-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/ainsof-io/hosts/ainsof-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ainsof-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/ainsof-io/vendors/ainsof-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ainsof-io-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://ainsof.io/docs/get-started/
- group: auth
  href: https://artifacts.apis.io/ainsof-io/security/ainsof-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ainsof-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ainsof.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ainsof.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://ainsof.io/docs/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://ainsof.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ainsof.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ainsof.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://ainsof.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://ainsof.io/help
coverage:
  checked: '2026-11-01'
  detail: API reference page is HTML rendered without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://ainsof.io/docs/api-reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AINSOF provides AI‑enhanced music search, licensing, and scoring tools for creators, agencies, and developers. Their platform offers a searchable catalog of licensed tracks, sound effects, and stems, plus an MCP API that supports both REST and JSON‑RPC interfaces for integration into applications, video workflows, and AI agents. The service includes a developer portal, pricing plans, documentation, and support resources, enabling users to quickly obtain API keys and start building music‑powered experiences.
image: https://ainsof.io/og-v2.jpg
json_schemas:
- name: PostCreateResponse
  property_count: 9
  slug: ainsof-io-post-create-response
- name: PostCutResponse
  property_count: 13
  slug: ainsof-io-post-cut-response
- name: PostFindResponse
  property_count: 9
  slug: ainsof-io-post-find-response
- name: PostMixRequest
  property_count: 11
  slug: ainsof-io-post-mix-request
- name: PostMixResponse
  property_count: 9
  slug: ainsof-io-post-mix-response
- name: PutResponse
  property_count: 5
  slug: ainsof-io-put-response
jsonld:
- class_count: 19
  name: Ainsof Io Context
  property_count: 67
  slug: ainsof-io-context
layout: provider
modified: '2026-11-01'
name: AINSOF
nav: Providers
network: true
overview: 'AINSOF is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Artificial Intelligence, Licensing, and Media.


  The AINSOF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AINSOF''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Ainsof Io Plans Pricing
  plan_count: 4
  slug: ainsof-io-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: AINSOF API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 2
  slug: ainsof-io-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 27.2
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 40.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ainsof Io Authentication
  slug: ainsof-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ainsof Io Domain Security
  slug: ainsof-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: ainsof-io
tags:
- Music
- Artificial Intelligence
- Licensing
- Media
website: https://ainsof.io/
---
