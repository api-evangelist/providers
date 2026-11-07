---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://platform.rise.ai
  baseurl_source: declared
  description: 'Rise.ai API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Rise.ai API
  slug: rise-ai-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/rise-ai/rules/rise-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/rise-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/rise-ai/json-ld/rise-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rise-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/rise-ai/vocabulary/rise-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rise-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rise-ai/data-model/rise-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rise-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/rise-ai/authentication/rise-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rise-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/rise-ai/conformance/rise-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rise-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rise-ai/llms/rise-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rise-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/rise-ai/well-known/rise-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rise-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/rise-ai/hosts/rise-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rise-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/rise-ai/vendors/rise-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rise-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/rise-ai/packages/rise-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/rise-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/rise-ai/packages/rise-ai-packages.yml
  title: ''
  type: Packages
  url: packages/rise-ai-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.rise.ai/
- group: auth
  href: https://artifacts.apis.io/rise-ai/security/rise-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rise-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rise.ai/
coverage:
  checked: '2026-10-28'
  detail: Provider's developer docs are rendered as HTML via JavaScript, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://dev.rise.ai/authentication/api-key
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: 'Rise.ai is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostOauth2TokenRequest
  property_count: 4
  slug: rise-ai-post-oauth2-token-request
jsonld:
- class_count: 1
  name: Rise Ai Context
  property_count: 4
  slug: rise-ai-context
layout: provider
modified: '2026-10-28'
name: Rise.ai
nav: Providers
network: true
overview: 'Rise.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Rise.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rise.ai''s developer surface includes authentication, documentation, and 13 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Rise.ai API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: rise-ai-rules
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.2
    catalog_earned_first_party: 0.0
    catalog_gap: 73.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 18.1
    developer_ergonomics: 23.8
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 17.6
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rise-ai/rise-ai-2026-11-03T142319.png
security:
- kind: authentication
  name: Rise Ai Authentication
  slug: rise-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Rise Ai Domain Security
  slug: rise-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rise-ai
tags:
- Company
website: https://rise.ai/
---
