---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for BetterImage.io social card generator
  name: BetterImage API
  slug: betterimage-api
- description: 'BetterImage.io API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BetterImage.io API
  slug: betterimage-io-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/betterimage-io/plans/betterimage-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/betterimage-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/betterimage-io/rules/betterimage-io-rules.yml
  title: ''
  type: Spectral
  url: rules/betterimage-io-rules.yml
- group: design
  href: https://artifacts.apis.io/betterimage-io/json-ld/betterimage-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/betterimage-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/betterimage-io/vocabulary/betterimage-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/betterimage-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/betterimage-io/data-model/betterimage-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/betterimage-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/betterimage-io/conformance/betterimage-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/betterimage-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/betterimage-io/llms/betterimage-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betterimage-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/betterimage-io/well-known/betterimage-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betterimage-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/betterimage-io/hosts/betterimage-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterimage-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/betterimage-io/vendors/betterimage-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betterimage-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/betterimage-io/packages/betterimage-io-packages.yml
  title: ''
  type: SDKs
  url: packages/betterimage-io-packages.yml
- group: build
  href: https://artifacts.apis.io/betterimage-io/packages/betterimage-io-packages.yml
  title: ''
  type: Packages
  url: packages/betterimage-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterimage.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterimage.io/privacy
- group: start
  title: ''
  type: Login
  url: https://betterimage.io/users/log-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://betterimage.io/social-card-templates/changelog
- group: auth
  href: https://artifacts.apis.io/betterimage-io/security/betterimage-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterimage-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterimage.io/
coverage:
  checked: '2026-11-02'
  detail: API reference page https://betterimage.io/api provides documentation but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://betterimage.io/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BetterImage.io provides a free social card generator allowing users to design cards for various platforms, export them in multiple sizes, and create link previews, YouTube thumbnails, squares, stories, and pins without requiring signup. The service focuses on quick, customizable social media visuals for product drops, blog posts, and other content, emphasizing ease of use and no registration barriers.
image: https://betterimage.io/images/og-default-d0f25bc729a5c51ed89469b42ab4c0f0.png?vsn=d
json_schemas:
- name: GetApiV1TemplatesResponse
  property_count: 5
  slug: betterimage-io-get-api-v1-templates-response
- name: GetApiV1UsageResponse
  property_count: 7
  slug: betterimage-io-get-api-v1-usage-response
- name: PostApiV1ImagesRequest
  property_count: 2
  slug: betterimage-io-post-api-v1-images-request
jsonld:
- class_count: 3
  name: Betterimage Io Context
  property_count: 13
  slug: betterimage-io-context
layout: provider
modified: '2026-11-02'
name: BetterImage.io
nav: Providers
network: true
overview: 'BetterImage.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media and Image Generation.


  The BetterImage.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BetterImage.io''s developer surface includes changelog and 17 more developer resources.'
plans:
- name: Betterimage Io Plans Pricing
  plan_count: 2
  slug: betterimage-io-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Betterimage Io Rate Limits
  slug: betterimage-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: BetterImage.io API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: betterimage-io-rules
scopes:
- name: Betterimage Io Scopes
  scope_count: 0
  slug: betterimage-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 69.8
    catalog_earned_first_party: 20.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 39.5
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betterimage Io Authentication
  slug: betterimage-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Betterimage Io Domain Security
  slug: betterimage-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betterimage-io
tags:
- Social Media
- Image Generation
website: https://betterimage.io/
---
