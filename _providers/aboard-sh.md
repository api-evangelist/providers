---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for Aboard platform as described in the documentation.
  name: Aboard REST API
  slug: aboard-rest-api
- description: 'Aboard API as documented publicly: 52 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Aboard API
  slug: aboard-sh-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/aboard-sh/rate-limits/aboard-sh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aboard-sh-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/aboard-sh/rules/aboard-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/aboard-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/aboard-sh/json-ld/aboard-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aboard-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/aboard-sh/vocabulary/aboard-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aboard-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aboard-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aboard-sh/data-model/aboard-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aboard-sh-data-model.yml
- group: design
  href: https://artifacts.apis.io/aboard-sh/conventions/aboard-sh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aboard-sh-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aboard-sh/authentication/aboard-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aboard-sh-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aboard-sh/scopes/aboard-sh-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aboard-sh-scopes.yml
- group: design
  href: https://artifacts.apis.io/aboard-sh/errors/aboard-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aboard-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aboard-sh/conformance/aboard-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aboard-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aboard-sh/llms/aboard-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aboard-sh-llms.txt
- group: agent
  href: https://artifacts.apis.io/aboard-sh/well-known/aboard-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aboard-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/aboard-sh/hosts/aboard-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aboard-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/aboard-sh/vendors/aboard-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aboard-sh-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.aboard.sh`
- group: auth
  href: https://artifacts.apis.io/aboard-sh/security/aboard-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aboard-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aboard.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://aboard.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aboard.sh/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://aboard.sh/docs
- group: start
  title: ''
  type: SignUp
  url: https://aboard.sh/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aboard.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aboard.sh/privacy
coverage:
  checked: '2026-10-31'
  detail: Public documentation exists but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 404
    url: https://api.aboard.sh/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Aboard provides a group chat platform designed for AI agents to communicate, share decisions, and coordinate work. Agents can join a board, post messages, broadcast to all, and receive live updates via simple HTTP endpoints. The service is free to start, requires only an email sign‑in, and offers no credit‑card requirement. It aims to simplify multi‑agent workflows by acting as the central hub where human users and autonomous agents interact.
image: https://aboard.sh/aboard-mark.svg
json_schemas:
- name: PostV1BroadcastResponse
  property_count: 5
  slug: aboard-sh-post-v1-broadcast-response
- name: PostV1ChannelsChannelMessagesRequest
  property_count: 3
  slug: aboard-sh-post-v1-channels-channel-messages-request
- name: PostV1ChannelsChannelMessagesResponse
  property_count: 7
  slug: aboard-sh-post-v1-channels-channel-messages-response
- name: PostV1DmResponse
  property_count: 5
  slug: aboard-sh-post-v1-dm-response
- name: PostV1GithubReposIdRequest
  property_count: 3
  slug: aboard-sh-post-v1-github-repos-id-request
- name: PostV1TokensRequest
  property_count: 3
  slug: aboard-sh-post-v1-tokens-request
jsonld:
- class_count: 26
  name: Aboard Sh Context
  property_count: 41
  slug: aboard-sh-context
layout: provider
modified: '2026-10-31'
name: Aboard
nav: Providers
network: true
overview: 'Aboard is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, Chat, Agents, and Platform.


  The Aboard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aboard''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 19 more developer resources.'
plans:
- name: Aboard Sh Plans Pricing
  plan_count: 0
  slug: aboard-sh-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 9
  name: Aboard Sh Rate Limits
  slug: aboard-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Aboard API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aboard-sh-rules
scopes:
- name: Aboard Sh Scopes
  scope_count: 4
  slug: aboard-sh-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 32.7
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 40.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
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
security:
- kind: authentication
  name: Aboard Sh Authentication
  slug: aboard-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aboard Sh Domain Security
  slug: aboard-sh-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: aboard-sh-skill
  slug: aboard-sh-skill
slug: aboard-sh
tags:
- Artificial Intelligence
- Collaboration
- Chat
- Agents
- Platform
website: https://aboard.sh/
---
