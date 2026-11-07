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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation is provided at the company website, but no machine‑readable contract (OpenAPI/GraphQL/etc.) was found.
  name: Ceki.me API
  slug: ceki-me-api-2
- baseURL: https://api.ceki.me
  baseurl_source: declared
  description: 'Ceki.me API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Ceki.me API
  slug: ceki-me-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/ceki-me/plans/ceki-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ceki-me-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ceki-me/rules/ceki-me-rules.yml
  title: ''
  type: Spectral
  url: rules/ceki-me-rules.yml
- group: design
  href: https://artifacts.apis.io/ceki-me/json-ld/ceki-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ceki-me-context.jsonld
- group: design
  href: https://artifacts.apis.io/ceki-me/vocabulary/ceki-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ceki-me-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ceki-me/data-model/ceki-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ceki-me-data-model.yml
- group: design
  href: https://artifacts.apis.io/ceki-me/conformance/ceki-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ceki-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ceki-me/llms/ceki-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ceki-me-llms.txt
- group: auth
  href: https://artifacts.apis.io/ceki-me/well-known/ceki-me-browser-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ceki-me-browser-security.txt
- group: agent
  href: https://artifacts.apis.io/ceki-me/well-known/ceki-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ceki-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/ceki-me/hosts/ceki-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceki-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/ceki-me/vendors/ceki-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceki-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ceki.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ceki.me/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ceki.me/pricing
- group: start
  title: ''
  type: Login
  url: https://ceki.me/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ceki-me
- group: docs
  title: ''
  type: Documentation
  url: https://ceki.me/docs/index.html
- group: auth
  href: https://artifacts.apis.io/ceki-me/security/ceki-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceki-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ceki.me/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract was found on the provider's documented hosts.
  evidence:
  - status: 404
    url: https://api.ceki.me/openapi.json
  - status: 404
    url: https://api.ceki.me/openapi.yaml
  - status: 404
    url: https://ceki.me/docs/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Ceki.me offers a free task tracker, time tracker and calendar with AI agents. It provides an AI‑powered marketplace where idle Chrome browsers are rented to earn USDT, and AI or human agents can be hired. The platform enables collaborative productivity, passive income, and flexible hiring, targeting worldwide users.
image: https://ceki.me/logo_dark-fb.png
json_schemas:
- name: PostApiAgentRegisterRequest
  property_count: 6
  slug: ceki-me-post-api-agent-register-request
- name: PostApiAgentRegisterResponse
  property_count: 6
  slug: ceki-me-post-api-agent-register-response
- name: PostApiAgentVerifyEmailRequest
  property_count: 2
  slug: ceki-me-post-api-agent-verify-email-request
- name: PostApiLoginRequest
  property_count: 2
  slug: ceki-me-post-api-login-request
- name: PostApiLoginrequestRequest
  property_count: 1
  slug: ceki-me-post-api-loginrequest-request
jsonld:
- class_count: 5
  name: Ceki Me Context
  property_count: 8
  slug: ceki-me-context
layout: provider
modified: '2026-11-04'
name: Ceki.me
nav: Providers
network: true
overview: 'Ceki.me is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Marketplace, Collaboration, and Time Tracking.


  The Ceki.me catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ceki.me''s developer surface includes pricing, documentation, and 17 more developer resources.'
plans:
- name: Ceki Me Plans Pricing
  plan_count: 6
  slug: ceki-me-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Ceki.me API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: ceki-me-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.9
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 13.2
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ceki Me Domain Security
  slug: ceki-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ceki-me
tags:
- Artificial Intelligence
- Productivity
- Marketplace
- Collaboration
- Time Tracking
website: https://ceki.me/
---
