---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.v2.dealmachine.com
  baseurl_source: declared
  description: 'DealMachine API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DealMachine API
  slug: dealmachine-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Dealmachine Com Webhooks
  slug: dealmachine-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/dealmachine-com/rate-limits/dealmachine-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dealmachine-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dealmachine-com/plans/dealmachine-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dealmachine-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dealmachine-com/rules/dealmachine-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dealmachine-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dealmachine-com/json-ld/dealmachine-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dealmachine-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dealmachine-com/vocabulary/dealmachine-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dealmachine-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dealmachine-com/asyncapi/dealmachine-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dealmachine-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dealmachine-com/data-model/dealmachine-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealmachine-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/dealmachine-com/cli/dealmachine-com-cli.yml
  title: ''
  type: CLI
  url: cli/dealmachine-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/dealmachine-com/changelog/dealmachine-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dealmachine-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/dealmachine-com/conventions/dealmachine-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dealmachine-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dealmachine-com/authentication/dealmachine-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dealmachine-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dealmachine-com/conformance/dealmachine-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealmachine-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dealmachine-com/llms/dealmachine-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealmachine-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dealmachine-com/well-known/dealmachine-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealmachine-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/dealmachine-com/well-known/dealmachine-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealmachine-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealmachine-com/hosts/dealmachine-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealmachine-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealmachine-com/vendors/dealmachine-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealmachine-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealmachine.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.next.dealmachine.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dealmachine.com/
- group: start
  title: ''
  type: SignUp
  url: https://dealmachine.com/sign-up?redirect_url=%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealmachine.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://dealmachine.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://dealmachine.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://api.docs.dealmachine.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dealmachine.com/
- group: auth
  href: https://artifacts.apis.io/dealmachine-com/security/dealmachine-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealmachine-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealmachine.com/
created: '2026-11-05'
description: DealMachine provides property and owner data tools for real‑estate investors, enabling them to search properties, skip‑trace owners, and build lead lists. The platform combines public records with proprietary analytics to streamline acquisition workflows and support investment decisions.
image: https://www.dealmachine.com/brand/store-listing/mobile-2026/google-play/feature-graphic.png
json_schemas:
- name: GetV1AccountResponse
  property_count: 13
  slug: dealmachine-com-get-v1-account-response
- name: GetV1PlansResponse
  property_count: 2
  slug: dealmachine-com-get-v1-plans-response
- name: PostV1ListsListidItemsRequest
  property_count: 3
  slug: dealmachine-com-post-v1-lists-listid-items-request
- name: PostV1PhonesDncResponse
  property_count: 3
  slug: dealmachine-com-post-v1-phones-dnc-response
- name: PostV1PropertiesSearchCountRequest
  property_count: 4
  slug: dealmachine-com-post-v1-properties-search-count-request
- name: PostV1ProspectsProspect8812NotesResponse
  property_count: 1
  slug: dealmachine-com-post-v1-prospects-prospect8812-notes-response
jsonld:
- class_count: 26
  name: Dealmachine Com Context
  property_count: 61
  slug: dealmachine-com-context
layout: provider
modified: '2026-11-05'
name: DealMachine
nav: Providers
network: true
overview: 'DealMachine is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Data, Software-as-a-Service, Lead Generation, and Property Search.


  The DealMachine catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DealMachine''s developer surface includes CLI, changelog, authentication, support, signup flow, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Dealmachine Com Plans Pricing
  plan_count: 1
  slug: dealmachine-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Dealmachine Com Rate Limits
  slug: dealmachine-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: DealMachine API Rules
  rule_count: 48
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 6
  slug: dealmachine-com-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 34.0
    developer_ergonomics: 47.6
    discoverability: 73.2
    operational_transparency: 71.1
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dealmachine Com Authentication
  slug: dealmachine-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dealmachine Com Domain Security
  slug: dealmachine-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dealmachine-com
tags:
- Real Estate
- Data
- Software-as-a-Service
- Lead Generation
- Property Search
website: https://dealmachine.com/
---
