---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    idempotency: derived
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
  score: 39.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Refract API provides JSON:API endpoints for workspaces, accounts, posts, drafts, scheduling and webhooks. Documentation is at https://refract.social/docs/api. No machine‑readable contract (OpenAPI
  name: Refract API
  slug: refract-api
- description: 'Refract API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Refract API
  slug: refract-social-api
artifact_total: 14
asyncapis:
- description: ''
  name: Refract Social Webhooks
  slug: refract-social-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/refract-social/rate-limits/refract-social-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/refract-social-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/refract-social/plans/refract-social-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/refract-social-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/refract-social/rules/refract-social-rules.yml
  title: ''
  type: Spectral
  url: rules/refract-social-rules.yml
- group: design
  href: https://artifacts.apis.io/refract-social/json-ld/refract-social-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/refract-social-context.jsonld
- group: design
  href: https://artifacts.apis.io/refract-social/vocabulary/refract-social-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/refract-social-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/refract-social/asyncapi/refract-social-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/refract-social-webhooks.yml
- group: design
  href: https://artifacts.apis.io/refract-social/data-model/refract-social-data-model.yml
  title: ''
  type: DataModel
  url: data-model/refract-social-data-model.yml
- group: operate
  href: https://artifacts.apis.io/refract-social/changelog/refract-social-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/refract-social-changelog.yml
- group: design
  href: https://artifacts.apis.io/refract-social/conventions/refract-social-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/refract-social-conventions.yml
- group: design
  href: https://artifacts.apis.io/refract-social/conventions/refract-social-conventions.yml
  title: ''
  type: Conventions
  url: conventions/refract-social-conventions.yml
- group: design
  href: https://artifacts.apis.io/refract-social/conformance/refract-social-conformance.yml
  title: ''
  type: Conformance
  url: conformance/refract-social-conformance.yml
- group: agent
  href: https://artifacts.apis.io/refract-social/llms/refract-social-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/refract-social-llms.txt
- group: agent
  href: https://artifacts.apis.io/refract-social/well-known/refract-social-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/refract-social-well-known.yml
- group: other
  href: https://artifacts.apis.io/refract-social/hosts/refract-social-hosts.yml
  title: ''
  type: Hosts
  url: hosts/refract-social-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://refract.social/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://refract.social/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://refract.social/pricing
- group: start
  title: ''
  type: Login
  url: https://refract.social/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://refract.social/docs/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://refract.social/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/refract-social/security/refract-social-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/refract-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://refract.social
- group: docs
  title: ''
  type: Documentation
  url: https://refract.social/developers
coverage:
  checked: '2026-11-03'
  detail: The provider's documentation pages are public but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found after probing known locations.
  evidence:
  - status: 200
    url: https://refract.social/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Refract provides a social media scheduling platform that lets users write a post once and automatically generates native versions for up to twelve networks, including Bluesky and TikTok. Using its JSON:API, developers can manage workspaces, accounts, and posts, schedule content, handle webhooks, and access a command‑line interface. All plans include an MCP server for advanced integrations, and the service emphasizes AI‑drafted content and user‑approved scheduling.
image: https://refract.social/og/default.png
json_schemas:
- name: PostApiV1WorkspacesKoloCoffeeMediaResponse
  property_count: 3
  slug: refract-social-post-api-v1-workspaces-kolo-coffee-media-response
- name: PostApiV1WorkspacesKoloCoffeeNotesRequest
  property_count: 7
  slug: refract-social-post-api-v1-workspaces-kolo-coffee-notes-request
- name: PostApiV1WorkspacesKoloCoffeeNotesResponse
  property_count: 8
  slug: refract-social-post-api-v1-workspaces-kolo-coffee-notes-response
- name: PostApiV1WorkspacesKoloCoffeePostsPostAccountsAccountEditRes
  property_count: 3
  slug: refract-social-post-api-v1-workspaces-kolo-coffee-posts-post-accounts-account-edit-res
- name: PostWorkspacesWorkspaceAccountsWordpressRequest
  property_count: 9
  slug: refract-social-post-workspaces-workspace-accounts-wordpress-request
- name: PostWorkspacesWorkspacePostsRequest
  property_count: 5
  slug: refract-social-post-workspaces-workspace-posts-request
jsonld:
- class_count: 16
  name: Refract Social Context
  property_count: 40
  slug: refract-social-context
layout: provider
modified: '2026-11-03'
name: Refract
nav: Providers
network: true
overview: 'Refract is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Scheduling, Artificial Intelligence, Automation, and Company.


  The Refract catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Refract''s developer surface includes changelog, pricing, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Refract Social Plans Pricing
  plan_count: 4
  slug: refract-social-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Refract Social Rate Limits
  slug: refract-social-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Refract API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 1
  slug: refract-social-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 35.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 47.4
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Refract Social Domain Security
  slug: refract-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: refract-social
tags:
- Social Media
- Scheduling
- Artificial Intelligence
- Automation
- Company
website: https://refract.social
---
