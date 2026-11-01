---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lotsofsounds Com Agentic Access
  operation_count: 7
  slug: lotsofsounds-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.lotsofsounds.com
  baseurl_source: declared
  description: Public sample endpoints - no API key required
  name: lotsofsounds-com Samples API
  slug: lotsofsounds-com-samples-api
- baseURL: https://api.lotsofsounds.com
  baseurl_source: declared
  description: Browse, search, and download sounds
  name: lotsofsounds-com Sounds API
  slug: lotsofsounds-com-sounds-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/lotsofsounds-com/agentic-access/lotsofsounds-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lotsofsounds-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lotsofsounds-com/rate-limits/lotsofsounds-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lotsofsounds-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lotsofsounds-com/plans/lotsofsounds-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lotsofsounds-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/rules/lotsofsounds-com-rules.yml
  title: ''
  type: Spectral
  url: rules/lotsofsounds-com-rules.yml
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/json-ld/lotsofsounds-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lotsofsounds-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/vocabulary/lotsofsounds-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lotsofsounds-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/data-model/lotsofsounds-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lotsofsounds-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/conventions/lotsofsounds-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lotsofsounds-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/lotsofsounds-com/authentication/lotsofsounds-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lotsofsounds-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/errors/lotsofsounds-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lotsofsounds-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lotsofsounds-com/conformance/lotsofsounds-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lotsofsounds-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lotsofsounds-com/llms/lotsofsounds-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lotsofsounds-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/lotsofsounds-com/well-known/lotsofsounds-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lotsofsounds-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/lotsofsounds-com/hosts/lotsofsounds-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lotsofsounds-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lotsofsounds-com/vendors/lotsofsounds-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lotsofsounds-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lotsofsounds
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.lotsofsounds.com</span
- group: auth
  href: https://artifacts.apis.io/lotsofsounds-com/security/lotsofsounds-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lotsofsounds-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lotsofsounds.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lotsofsounds.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.lotsofsounds.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lotsofsounds.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lotsofsounds.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.lotsofsounds.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.lotsofsounds.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lotsofsounds.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lotsofsounds.com/privacy
created: '2026-10-30'
description: Lots of Sounds provides a free CC0 sound effects library and a RESTful API for developers to search, stream, and download royalty‑free audio. The platform offers over 10,000 sounds across categories, with tools for audio conversion, trimming, and waveform generation. Plans include a free tier and paid options starting at $15/month for higher limits and commercial use. The company focuses on open licensing and easy integration for podcasts, games, videos, and AI agents.
image: https://www.lotsofsounds.com/og?title=Lots%20of%20Sounds%3A%20Free%20CC0%20Sound%20Effects%2C%20Soundboard%20%26%20Sound%20Effects%20API
json_schemas:
- name: Pagination
  property_count: 4
  slug: lotsofsounds-com-pagination
- name: PopularSound
  property_count: 0
  slug: lotsofsounds-com-popular-sound
- name: Sound
  property_count: 0
  slug: lotsofsounds-com-sound
- name: SoundSummary
  property_count: 7
  slug: lotsofsounds-com-sound-summary
jsonld:
- class_count: 3
  name: Lotsofsounds Com Context
  property_count: 12
  slug: lotsofsounds-com-context
layout: provider
modified: '2026-10-30'
name: lotsofsounds-com
nav: Providers
network: true
overview: 'lotsofsounds-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Samples API and Sounds API. Tagged areas include Company, Audio, API, Free, and CC0.


  The lotsofsounds-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lotsofsounds-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 20 more developer resources.'
plans:
- name: Lotsofsounds Com Plans Pricing
  plan_count: 3
  slug: lotsofsounds-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Lotsofsounds Com Rate Limits
  slug: lotsofsounds-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: lotsofsounds-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: lotsofsounds-com-rules
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 79.8
    catalog_earned_first_party: 20.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 65.2
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lotsofsounds Com Authentication
  slug: lotsofsounds-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lotsofsounds Com Domain Security
  slug: lotsofsounds-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lotsofsounds-com
tags:
- Company
- Audio
- API
- Free
- CC0
website: https://lotsofsounds.com/
---
