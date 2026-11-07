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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Weirapp Io Agentic Access
  operation_count: 58
  slug: weirapp-io-agentic-access
  summary_line: 58 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.weirapp.io
  baseurl_source: declared
  description: 'Introspection: who this key belongs to, what credit it has left, and what its tier allows. These endpoints are free — they never consume credits.'
  name: weirapp-io Account API
  slug: weirapp-io-account-api
- baseURL: https://api.weirapp.io
  baseurl_source: declared
  description: Saved queries that run on a schedule and report only what is new. Results are deduplicated by content, so an edited or re-posted item never alerts twice.
  name: weirapp-io Monitors API
  slug: weirapp-io-monitors-api
- baseURL: https://api.weirapp.io
  baseurl_source: declared
  description: 'Reddit-specific operations: communities, comment trees, and scoped search.'
  name: weirapp-io Reddit API
  slug: weirapp-io-reddit-api
- baseURL: https://api.weirapp.io
  baseurl_source: declared
  description: Liveness and readiness. Unauthenticated.
  name: weirapp-io System API
  slug: weirapp-io-system-api
- baseURL: https://api.weirapp.io
  baseurl_source: declared
  description: Signed deliveries when a monitor finds something, instead of polling. Every attempt is recorded, including ones that are about to be retried.
  name: weirapp-io Webhooks API
  slug: weirapp-io-webhooks-api
- baseURL: https://api.weirapp.io
  baseurl_source: declared
  description: 'X-specific operations: posts, threads, quotes, and edit history; profiles, timelines, followers, and account search; Lists and Spaces; and search with composable filters.'
  name: weirapp-io X API
  slug: weirapp-io-x-api
artifact_total: 13
asyncapis:
- description: ''
  name: Weirapp Io Webhooks
  slug: weirapp-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/weirapp-io/agentic-access/weirapp-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/weirapp-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/weirapp-io/plans/weirapp-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weirapp-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/weirapp-io/rules/weirapp-io-rules.yml
  title: ''
  type: Spectral
  url: rules/weirapp-io-rules.yml
- group: design
  href: https://artifacts.apis.io/weirapp-io/vocabulary/weirapp-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weirapp-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/weirapp-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/weirapp-io/asyncapi/weirapp-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/weirapp-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/weirapp-io/conventions/weirapp-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/weirapp-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/weirapp-io/authentication/weirapp-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weirapp-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/weirapp-io/errors/weirapp-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/weirapp-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/weirapp-io/conformance/weirapp-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weirapp-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/weirapp-io/llms/weirapp-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weirapp-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/weirapp-io/well-known/weirapp-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/weirapp-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/weirapp-io/hosts/weirapp-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weirapp-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weirapp.io/terms
- group: start
  title: ''
  type: Sandbox
  url: https://weirapp.io/dashboard/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weirapp.io/privacy
- group: auth
  href: https://artifacts.apis.io/weirapp-io/security/weirapp-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weirapp-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weirapp.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.weirapp.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.weirapp.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.weirapp.io/quickstart
- group: company
  title: ''
  type: Blog
  url: https://weirapp.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://weirapp.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://weirapp.io/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://weirapp.io/status
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.weirapp.io/openapi.json
  - status: null
    url: https://docs.weirapp.io/mcp
  - status: 401
    url: https://api.weirapp.io/mcp
  - status: 401
    url: https://api.weirapp.io/v1/graphql
  - status: 200
    url: https://weirapp.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Weir provides a public API and MCP server delivering Reddit and X (Twitter) data, enabling developers and AI agents to search posts, read threads, profiles, and receive alerts on mentions. The service offers a free tier with 5,000 credits monthly and pay‑as‑you‑go pricing, supporting multiple languages and integrations with AI assistants like Claude and ChatGPT.
image: https://weirapp.io/opengraph-image
layout: provider
modified: '2026-10-31'
name: weirapp-io
nav: Providers
network: true
overview: 'weirapp-io publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Monitors API, Reddit API, and 3 more. Tagged areas include Company, Data, Social Media, and MCP.


  The weirapp-io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  weirapp-io''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Weirapp Io Plans Pricing
  plan_count: 6
  slug: weirapp-io-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: weirapp-io API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: weirapp-io-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 37.4
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Weirapp Io Authentication
  slug: weirapp-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Weirapp Io Domain Security
  slug: weirapp-io-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-reddit-post
  slug: weirapp-io-get-reddit-post
slug: weirapp-io
tags:
- Company
- Data
- Social Media
- MCP
website: https://weirapp.io/
---
