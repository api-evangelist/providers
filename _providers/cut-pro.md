---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Cut.Pro API as documented publicly: 48 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cut.Pro API
  slug: cut-pro-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/cut-pro/rate-limits/cut-pro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cut-pro-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cut-pro/plans/cut-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cut-pro-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cut-pro/rules/cut-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/cut-pro-rules.yml
- group: design
  href: https://artifacts.apis.io/cut-pro/json-ld/cut-pro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cut-pro-context.jsonld
- group: design
  href: https://artifacts.apis.io/cut-pro/vocabulary/cut-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cut-pro-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cut-pro/data-model/cut-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cut-pro-data-model.yml
- group: design
  href: https://artifacts.apis.io/cut-pro/conventions/cut-pro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cut-pro-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cut-pro/authentication/cut-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cut-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/cut-pro/conformance/cut-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cut-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cut-pro/llms/cut-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cut-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/cut-pro/well-known/cut-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cut-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/cut-pro/hosts/cut-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cut-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/cut-pro/vendors/cut-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cut-pro-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cut.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cut.pro/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://cut.pro/en/changelog
- group: company
  title: ''
  type: Blog
  url: https://cut.pro/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://cut.pro/pt-BR/help/c/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://cut.pro/docs/reference
- group: auth
  href: https://artifacts.apis.io/cut-pro/security/cut-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cut-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cut.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://cut.pro/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cut.pro/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/cutpro
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://cut.pro/docs/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Brazil's leading AI-powered video clipping platform, a 100% Brazilian company that automatically turns long videos, live streams and podcasts into viral short clips with 99%+ accurate subtitles and auto-publishing to TikTok, Instagram Reels and more. It serves Brazil, Latin America, the United States and worldwide, offering free start and advanced AI features.
image: https://cut.pro/og-image.png
json_schemas:
- name: GetWorkspaceResponse
  property_count: 4
  slug: cut-pro-get-workspace-response
- name: PostGenerationsRequest
  property_count: 4
  slug: cut-pro-post-generations-request
- name: PostPersonasIdShotsProductResponse
  property_count: 7
  slug: cut-pro-post-personas-id-shots-product-response
- name: PostPostsRequest
  property_count: 3
  slug: cut-pro-post-posts-request
- name: PostVideosUploadCompleteRequest
  property_count: 3
  slug: cut-pro-post-videos-upload-complete-request
- name: PostVideosUploadResponse
  property_count: 5
  slug: cut-pro-post-videos-upload-response
jsonld:
- class_count: 70
  name: Cut Pro Context
  property_count: 70
  slug: cut-pro-context
layout: provider
modified: '2026-11-04'
name: Cut.Pro
nav: Providers
network: true
overview: 'Cut.Pro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Clipping, and Social Media.


  The Cut.Pro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cut.Pro''s developer surface includes authentication, changelog, engineering blog, getting-started guide, API reference, documentation, pricing, and 17 more developer resources.'
plans:
- name: Cut Pro Plans Pricing
  plan_count: 4
  slug: cut-pro-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Cut Pro Rate Limits
  slug: cut-pro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Cut.Pro API Rules
  rule_count: 45
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 4
  slug: cut-pro-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cut Pro Authentication
  slug: cut-pro-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cut Pro Domain Security
  slug: cut-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cut-pro
tags:
- Company
- Artificial Intelligence
- Video
- Clipping
- Social Media
- Brazil
website: https://cut.pro/
---
