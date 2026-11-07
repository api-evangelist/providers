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
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Spoken Md Agentic Access
  operation_count: 10
  slug: spoken-md-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Podcast transcripts as clean markdown. Built for AI agents.
  name: Podcast Transcripts API
  slug: podcast-transcripts-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: Podcast transcripts as clean markdown. Built for AI agents. Use the demo key `pt_demo` to try it free (demo episode only).
  name: Podcast Transcripts API .well-known API
  slug: podcast-transcripts-api-well-known-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/spoken-md/plans/spoken-md-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spoken-md-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/rules/spoken-md-rules.yml
  title: ''
  type: Spectral
  url: rules/spoken-md-rules.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/json-ld/spoken-md-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spoken-md-context.jsonld
- group: design
  href: https://artifacts.apis.io/spoken-md/vocabulary/spoken-md-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spoken-md-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/data-model/spoken-md-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spoken-md-data-model.yml
- group: auth
  href: https://artifacts.apis.io/spoken-md/authentication/spoken-md-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spoken-md-authentication.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/errors/spoken-md-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spoken-md-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/conformance/spoken-md-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spoken-md-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spoken-md/llms/spoken-md-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spoken-md-llms.txt
- group: agent
  href: https://artifacts.apis.io/spoken-md/well-known/spoken-md-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spoken-md-well-known.yml
- group: other
  href: https://artifacts.apis.io/spoken-md/hosts/spoken-md-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spoken-md-hosts.yml
- group: other
  href: https://artifacts.apis.io/spoken-md/vendors/spoken-md-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spoken-md-vendors.yml
- group: build
  href: https://artifacts.apis.io/spoken-md/packages/spoken-md-packages.yml
  title: ''
  type: SDKs
  url: packages/spoken-md-packages.yml
- group: build
  href: https://artifacts.apis.io/spoken-md/packages/spoken-md-packages.yml
  title: ''
  type: Packages
  url: packages/spoken-md-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spoken.md/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spoken.md/privacy.html
- group: docs
  title: ''
  type: APIReference
  url: https://spoken.md/podcast-transcript-api
- group: auth
  href: https://artifacts.apis.io/spoken-md/security/spoken-md-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spoken-md-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spoken.md/
- group: commercial
  title: ''
  type: Pricing
  url: https://spoken.md/#pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://spoken.md/#how-it-works
- group: operate
  title: ''
  type: Support
  url: https://spoken.md/#contact
created: '2026-10-31'
description: Spoken.md provides a Podcast Transcript API that returns clean Markdown with real speaker names. Users can fetch a single episode or an entire show’s back catalog without a subscription, enabling AI agents to process podcast content easily.
image: https://spoken.md/og-image.png
json_schemas:
- name: EpisodeRef
  property_count: 3
  slug: spoken-md-episode-ref
- name: Follow
  property_count: 6
  slug: spoken-md-follow
- name: NewEpisode
  property_count: 4
  slug: spoken-md-new-episode
- name: SearchResult
  property_count: 5
  slug: spoken-md-search-result
jsonld:
- class_count: 5
  name: Spoken Md Context
  property_count: 12
  slug: spoken-md-context
layout: provider
modified: '2026-10-31'
name: spoken-md
nav: Providers
network: true
overview: 'spoken-md publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Podcast Transcripts API and Podcast Transcripts API .well-known API. Tagged areas include Podcasts, Transcripts, Markdown, and Artificial Intelligence.


  The spoken-md catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  spoken-md''s developer surface includes authentication, API reference, pricing, getting-started guide, support, and 17 more developer resources.'
plans:
- name: Spoken Md Plans Pricing
  plan_count: 6
  slug: spoken-md-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Spoken Md Rate Limits
  slug: spoken-md-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: spoken-md API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 1
  slug: spoken-md-rules
scopes:
- name: Spoken Md Scopes
  scope_count: 0
  slug: spoken-md-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 67.5
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spoken-md/spoken-md-2026-11-03T143643.png
security:
- kind: authentication
  name: Spoken Md Authentication
  slug: spoken-md-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Spoken Md Domain Security
  slug: spoken-md-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: spoken-md
  slug: spoken-md-agents
slug: spoken-md
tags:
- Podcasts
- Transcripts
- Markdown
- Artificial Intelligence
website: https://spoken.md/
---
