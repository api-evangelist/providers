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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dynamoi Com Agentic Access
  operation_count: 4
  slug: dynamoi-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://dynamoi.com
  baseurl_source: declared
  description: The Data API from Dynamoi — 4 operation(s) for data.
  name: Dynamoi Data API
  slug: dynamoi-com-data-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/dynamoi-com/agentic-access/dynamoi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dynamoi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dynamoi-com/plans/dynamoi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamoi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dynamoi-com/rules/dynamoi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dynamoi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dynamoi-com/json-ld/dynamoi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynamoi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dynamoi-com/vocabulary/dynamoi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dynamoi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dynamoi-com/data-model/dynamoi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dynamoi-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/dynamoi-com/cli/dynamoi-com-cli.yml
  title: ''
  type: CLI
  url: cli/dynamoi-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/dynamoi-com/authentication/dynamoi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamoi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dynamoi-com/errors/dynamoi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dynamoi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dynamoi-com/conformance/dynamoi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynamoi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dynamoi-com/llms/dynamoi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynamoi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dynamoi-com/well-known/dynamoi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynamoi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dynamoi-com/hosts/dynamoi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynamoi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynamoi-com/vendors/dynamoi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynamoi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dynamoi-com/packages/dynamoi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dynamoi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dynamoi-com/packages/dynamoi-com-packages.yml
  title: ''
  type: Packages
  url: packages/dynamoi-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dynamoi.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://dynamoi.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dynamoi.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://dynamoi.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://dynamoi.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://dynamoi.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://dynamoi.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://dynamoi.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dynamoi.com/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/dynamoi-com/security/dynamoi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamoi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dynamoi.com/
created: '2026-11-06'
description: Dynamoi is a music promotion platform that provides automated Spotify and YouTube ad campaigns for independent artists, labels, and creators. The service offers free Smart Links, real‑time analytics, and managed advertising options starting at $25 per month. Founded in 2021, Dynamoi serves worldwide artists looking to grow their streaming presence across major platforms.
image: https://dynamoi.com/og/home-constellation.jpg
json_schemas:
- name: PaidDataBundle
  property_count: 5
  slug: dynamoi-com-paid-data-bundle
jsonld:
- class_count: 5
  name: Dynamoi Com Context
  property_count: 28
  slug: dynamoi-com-context
layout: provider
modified: '2026-11-06'
name: Dynamoi
nav: Providers
network: true
overview: 'Dynamoi publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Data API. Tagged areas include Music Promotion, Spotify, YouTube, Distribution, and Analytics.


  The Dynamoi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dynamoi''s developer surface includes CLI, authentication, support, documentation, changelog, pricing, getting-started guide, and 20 more developer resources.'
plans:
- name: Dynamoi Com Plans Pricing
  plan_count: 3
  slug: dynamoi-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Dynamoi API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 1
  slug: dynamoi-com-rules
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 71.2
    catalog_earned_first_party: 12.0
    catalog_gap: 43.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 60.1
    developer_ergonomics: 59.5
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
  name: Dynamoi Com Authentication
  slug: dynamoi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dynamoi Com Domain Security
  slug: dynamoi-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dynamoi-com
tags:
- Music Promotion
- Spotify
- YouTube
- Distribution
- Analytics
- Independent Artists
- Labels
website: https://dynamoi.com/
---
