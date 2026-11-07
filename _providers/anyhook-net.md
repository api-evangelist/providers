---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Anyhook Net Agentic Access
  operation_count: 25
  slug: anyhook-net-agentic-access
  summary_line: 25 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The AnyHook API API from AnyHook — 1 operation(s) for anyhook api.
  name: AnyHook AnyHook API
  slug: anyhook-net-anyhook-api-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Api Keys API from AnyHook — 2 operation(s) for api keys.
  name: AnyHook Api Keys API
  slug: anyhook-net-api-keys-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Apps API from AnyHook — 8 operation(s) for apps.
  name: AnyHook Apps API
  slug: anyhook-net-apps-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Claim API from AnyHook — 1 operation(s) for claim.
  name: AnyHook Claim API
  slug: anyhook-net-claim-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Connect API from AnyHook — 1 operation(s) for connect.
  name: AnyHook Connect API
  slug: anyhook-net-connect-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Events API from AnyHook — 3 operation(s) for events.
  name: AnyHook Events API
  slug: anyhook-net-events-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Quickstart API from AnyHook — 1 operation(s) for quickstart.
  name: AnyHook Quickstart API
  slug: anyhook-net-quickstart-api
- baseURL: https://anyhook.net
  baseurl_source: declared
  description: The Usage API from AnyHook — 1 operation(s) for usage.
  name: AnyHook Usage API
  slug: anyhook-net-usage-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/anyhook-net/agentic-access/anyhook-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anyhook-net-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/anyhook-net/rate-limits/anyhook-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anyhook-net-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/anyhook-net/rules/anyhook-net-rules.yml
  title: ''
  type: Spectral
  url: rules/anyhook-net-rules.yml
- group: design
  href: https://artifacts.apis.io/anyhook-net/json-ld/anyhook-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anyhook-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/anyhook-net/vocabulary/anyhook-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anyhook-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anyhook-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anyhook-net/data-model/anyhook-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anyhook-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/anyhook-net/authentication/anyhook-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anyhook-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/anyhook-net/errors/anyhook-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anyhook-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anyhook-net/conformance/anyhook-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anyhook-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anyhook-net/llms/anyhook-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anyhook-net-llms.txt
- group: build
  href: https://artifacts.apis.io/anyhook-net/mcp/anyhook-net-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anyhook-net-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anyhook-net/mcp/anyhook-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anyhook-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anyhook-net/well-known/anyhook-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anyhook-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/anyhook-net/hosts/anyhook-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anyhook-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/anyhook-net/vendors/anyhook-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anyhook-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anyhook.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anyhook.net/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://anyhook.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anyhook.net/llms.txt
- group: auth
  href: https://artifacts.apis.io/anyhook-net/security/anyhook-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anyhook-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anyhook.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anyhook.net/dashboard
- group: company
  title: ''
  type: Blog
  url: https://anyhook.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anyhook.net/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://anyhook.net/sign-up
created: '2026-11-01'
description: AnyHook provides a durable webhook relay service that stores every webhook event even when your server is down, allowing one‑click replay, inspection, and reliable delivery across integrations such as Stripe, Shopify, GitHub, Slack, and more. It offers free and paid plans with configurable retention periods, timeouts, and overage handling, ensuring events are never lost and can be replayed for debugging or recovery.
image: https://anyhook.net/opengraph-image-35z9bs?6ac94fb41b1c72dd
json_schemas:
- name: ApiKey
  property_count: 5
  slug: anyhook-net-api-key
- name: App
  property_count: 12
  slug: anyhook-net-app
- name: EventDetail
  property_count: 17
  slug: anyhook-net-event-detail
- name: Event
  property_count: 15
  slug: anyhook-net-event
jsonld:
- class_count: 5
  name: Anyhook Net Context
  property_count: 31
  slug: anyhook-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at anyhook.net.
  name: AnyHook MCP Server
  slug: anyhook-net-mcp-yml
modified: '2026-11-01'
name: AnyHook
nav: Providers
network: true
overview: 'AnyHook publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including AnyHook API, Api Keys API, Apps API, and 5 more. Tagged areas include Webhook, Integration, Reliability, Developer Tools, and event-replay.


  The AnyHook catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AnyHook''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Anyhook Net Plans Pricing
  plan_count: 0
  slug: anyhook-net-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Anyhook Net Rate Limits
  slug: anyhook-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AnyHook API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 3
  slug: anyhook-net-rules
scopes:
- name: Anyhook Net Scopes
  scope_count: 0
  slug: anyhook-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 32.6
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anyhook Net Authentication
  slug: anyhook-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anyhook Net Domain Security
  slug: anyhook-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: anyhook-apps-create
  slug: anyhook-net-apps-create
- name: anyhook-events-list
  slug: anyhook-net-events-list
slug: anyhook-net
tags:
- Webhook
- Integration
- Reliability
- Developer Tools
- event-replay
website: https://anyhook.net/
---
