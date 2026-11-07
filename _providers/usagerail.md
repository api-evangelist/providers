---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
api_count: 1
apis:
- baseURL: https://api.usagerail.com
  baseurl_source: declared
  description: 'UsageRail API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: UsageRail API
  slug: usagerail-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/usagerail/plans/usagerail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usagerail-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usagerail/rules/usagerail-rules.yml
  title: ''
  type: Spectral
  url: rules/usagerail-rules.yml
- group: design
  href: https://artifacts.apis.io/usagerail/json-ld/usagerail-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usagerail-context.jsonld
- group: design
  href: https://artifacts.apis.io/usagerail/vocabulary/usagerail-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usagerail-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usagerail/data-model/usagerail-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usagerail-data-model.yml
- group: auth
  href: https://artifacts.apis.io/usagerail/authentication/usagerail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usagerail-authentication.yml
- group: design
  href: https://artifacts.apis.io/usagerail/conformance/usagerail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usagerail-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usagerail/llms/usagerail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usagerail-llms.txt
- group: other
  href: https://artifacts.apis.io/usagerail/hosts/usagerail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usagerail-hosts.yml
- group: other
  href: https://artifacts.apis.io/usagerail/vendors/usagerail-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usagerail-vendors.yml
- group: build
  href: https://artifacts.apis.io/usagerail/packages/usagerail-packages.yml
  title: ''
  type: SDKs
  url: packages/usagerail-packages.yml
- group: build
  href: https://artifacts.apis.io/usagerail/packages/usagerail-packages.yml
  title: ''
  type: Packages
  url: packages/usagerail-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usagerail.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://usagerail.com/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usagerail
- group: auth
  href: https://artifacts.apis.io/usagerail/security/usagerail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usagerail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usagerail.com
- group: docs
  title: ''
  type: Documentation
  url: https://usagerail.com/docs/server-api
- group: commercial
  title: ''
  type: Pricing
  url: https://usagerail.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usagerail.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.usagerail.com/login
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are HTML only and no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://usagerail.com/docs/server-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: UsageRail provides an API monetization platform for small teams, enabling them to issue API keys, enforce rate limits and quotas, and bill usage through Stripe integration. The service offers a developer portal, documentation, and tools for managing customers, keys, usage data, and plan changes, aiming to simplify API productization and revenue generation for SaaS providers.
json_schemas:
- name: GetV1ConsumersIdUsageResponse
  property_count: 6
  slug: usagerail-get-v1-consumers-id-usage-response
- name: PostV1ConsumersIdCheckoutRequest
  property_count: 5
  slug: usagerail-post-v1-consumers-id-checkout-request
- name: PostV1ConsumersIdCreditsAdjustRequest
  property_count: 2
  slug: usagerail-post-v1-consumers-id-credits-adjust-request
- name: PostV1ConsumersIdKeysResponse
  property_count: 4
  slug: usagerail-post-v1-consumers-id-keys-response
- name: PostV1ConsumersIdPlanRequest
  property_count: 3
  slug: usagerail-post-v1-consumers-id-plan-request
- name: PostV1ConsumersResponse
  property_count: 1
  slug: usagerail-post-v1-consumers-response
jsonld:
- class_count: 22
  name: Usagerail Context
  property_count: 30
  slug: usagerail-context
layout: provider
modified: '2026-11-02'
name: UsageRail
nav: Providers
network: true
overview: 'UsageRail is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Monetization, Software-as-a-Service, Billing, and Rate Limiting.


  The UsageRail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UsageRail''s developer surface includes authentication, getting-started guide, documentation, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Usagerail Plans Pricing
  plan_count: 4
  slug: usagerail-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: UsageRail API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 2
  slug: usagerail-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 29.8
    discoverability: 62.5
    operational_transparency: 2.6
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usagerail Authentication
  slug: usagerail-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Usagerail Domain Security
  slug: usagerail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usagerail
tags:
- Company
- API Monetization
- Software-as-a-Service
- Billing
- Rate Limiting
- Developer Tools
website: https://usagerail.com
---
