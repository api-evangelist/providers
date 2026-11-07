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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dibatto Com Agentic Access
  operation_count: 9
  slug: dibatto-com-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- baseURL: https://dibatto.com/api
  baseurl_source: declared
  description: The Episodes API from Dibatto — 4 operation(s) for episodes.
  name: Dibatto Episodes API
  slug: dibatto-com-episodes-api
- baseURL: https://dibatto.com/api
  baseurl_source: declared
  description: The Shows API from Dibatto — 3 operation(s) for shows.
  name: Dibatto Shows API
  slug: dibatto-com-shows-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/dibatto-com/agentic-access/dibatto-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dibatto-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/dibatto-com/rate-limits/dibatto-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dibatto-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dibatto-com/plans/dibatto-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dibatto-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/rules/dibatto-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dibatto-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/json-ld/dibatto-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dibatto-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dibatto-com/vocabulary/dibatto-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dibatto-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dibatto-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/data-model/dibatto-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dibatto-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/conventions/dibatto-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dibatto-com-conventions.yml
- group: operate
  href: https://artifacts.apis.io/dibatto-com/lifecycle/dibatto-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dibatto-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/lifecycle/dibatto-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dibatto-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/errors/dibatto-com-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dibatto-com-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/errors/dibatto-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dibatto-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dibatto-com/conformance/dibatto-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dibatto-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dibatto-com/overlays/dibatto-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dibatto-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dibatto-com/llms/dibatto-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dibatto-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dibatto-com/well-known/dibatto-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dibatto-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dibatto-com/hosts/dibatto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dibatto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dibatto-com/vendors/dibatto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dibatto-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/johnarndt
- group: auth
  href: https://artifacts.apis.io/dibatto-com/authentication/dibatto-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dibatto-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dibatto-com/security/dibatto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dibatto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dibatto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dibatto.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://dibatto.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://dibatto.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dibatto.com/app
- group: company
  title: ''
  type: About
  url: https://dibatto.com/about
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dibatto.com/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dibatto.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dibatto.com/legal/privacy
created: '2026-11-05'
description: Dibatto is a recording studio for argument podcasts, operated by Soxoa LLC. Hosts build an interruptible AI co-host with its own voice, stance and personality, Dibatto researches the host's beat into a daily or weekly news rundown, the host records the argument live using full-duplex voice, and the wrap produces a transcript, chapters, show notes, titles, quotes and a coaching card, then a public episode page and podcast RSS feed. It publishes a Studio API (OpenAPI) and a gated MCP server for developers.
image: https://dibatto.com/og.png
json_schemas:
- name: EpisodeDeskResponse
  property_count: 7
  slug: dibatto-com-episode-desk-response
- name: EpisodeListResponse
  property_count: 2
  slug: dibatto-com-episode-list-response
- name: EpisodeResponse
  property_count: 1
  slug: dibatto-com-episode-response
- name: RundownResponse
  property_count: 1
  slug: dibatto-com-rundown-response
- name: ShowResponse
  property_count: 1
  slug: dibatto-com-show-response
- name: ShowsResponse
  property_count: 1
  slug: dibatto-com-shows-response
jsonld:
- class_count: 11
  name: Dibatto Com Context
  property_count: 21
  slug: dibatto-com-context
layout: provider
modified: '2026-11-05'
name: Dibatto
nav: Providers
network: true
overview: 'Dibatto publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Episodes API and Shows API. Tagged areas include Company, Podcasts, Artificial Intelligence, Voice, and Audio.


  The Dibatto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dibatto''s developer surface includes authentication, documentation, pricing, and 28 more developer resources.'
plans:
- name: Dibatto Com Plans Pricing
  plan_count: 4
  slug: dibatto-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Dibatto Com Rate Limits
  slug: dibatto-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Dibatto API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: dibatto-com-rules
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 32.7
    discoverability: 73.2
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
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
  name: Dibatto Com Authentication
  slug: dibatto-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dibatto Com Domain Security
  slug: dibatto-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: dibatto-prepare-episode
  slug: dibatto-com-prepare-episode
- name: dibatto-review-episode
  slug: dibatto-com-review-episode
slug: dibatto-com
tags:
- Company
- Podcasts
- Artificial Intelligence
- Voice
- Audio
- Content Creation
- MCP
website: https://dibatto.com/
---
