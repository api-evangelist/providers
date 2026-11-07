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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 61
  human_in_the_loop: 2
  name: Anjal App Agentic Access
  operation_count: 112
  slug: anjal-app-agentic-access
  summary_line: 112 operations · 61 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Multiple accepted addresses per inbox. Add a custom-domain alias to change the outbound From without losing thread history.
  name: Anjal Addresses API
  slug: anjal-app-addresses-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: The Cadences API from Anjal — 7 operation(s) for cadences.
  name: Anjal Cadences API
  slug: anjal-app-cadences-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Bring your own sending domain. Returns DNS records, verification state, and a BIND zone file export.
  name: Anjal Domains API
  slug: anjal-app-domains-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Compose messages across multiple agent turns and send atomically.
  name: Anjal Drafts API
  slug: anjal-app-drafts-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Email mailboxes that can send, receive, and store threads.
  name: Anjal Inboxes API
  slug: anjal-app-inboxes-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Profile lookup, connection requests, keyword post search. Each call is logged and counted against a per-session daily quota (LinkedIn rate-limits per account, not per IP).
  name: Anjal LinkedIn — Outreach API
  slug: anjal-app-linkedin-outreach-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: The LinkedIn — Posts API from Anjal — 4 operation(s) for linkedin — posts.
  name: Anjal LinkedIn — Posts API
  slug: anjal-app-linkedin-posts-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Deterministic historical search across past-24h | past-week | past-month. Synchronous — returns the full hit list inline with the same structured output shape as signals (post + author + classificatio
  name: Anjal LinkedIn — Searches API
  slug: anjal-app-linkedin-searches-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Login on behalf of the customer (email + password, with PIN or mobile-app verification challenge support), or import existing cookies. Cookies are AES-256-GCM encrypted at rest. Each session is tenant
  name: Anjal LinkedIn — Sessions API
  slug: anjal-app-linkedin-sessions-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Deterministic real-time intent watchers. Every signal is a keyword plus a plain-English firing rule (e.g. "Flag as ready when the author is a founder complaining about cold email — skip vendors and ag
  name: Anjal LinkedIn — Signals API
  slug: anjal-app-linkedin-signals-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Named groups of recipient addresses per inbox.
  name: Anjal Lists API
  slug: anjal-app-lists-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Send, reply, forward, list, and download messages.
  name: Anjal Messages API
  slug: anjal-app-messages-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Programmatic counters scoped by workspace or inbox.
  name: Anjal Metrics API
  slug: anjal-app-metrics-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Super-admin only — platform operator endpoints.
  name: Anjal Tenants API
  slug: anjal-app-tenants-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: HTTP callbacks fired on every inbox event.
  name: Anjal Webhooks API
  slug: anjal-app-webhooks-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Real-time event stream. The agentmail.to spec-compatible wire protocol.
  name: Anjal WebSocket API
  slug: anjal-app-websocket-api
- baseURL: https://anjal.app
  baseurl_source: declared
  description: Isolated containers under a tenant. Hand scoped keys to your resellers so their customers cannot see each other.
  name: Anjal Workspaces API
  slug: anjal-app-workspaces-api
artifact_total: 33
asyncapis:
- description: ''
  name: Anjal App Webhooks
  slug: anjal-app-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/anjal-app/agentic-access/anjal-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anjal-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/anjal-app/rate-limits/anjal-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anjal-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/anjal-app/plans/anjal-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anjal-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/rules/anjal-app-rules.yml
  title: ''
  type: Spectral
  url: rules/anjal-app-rules.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/json-ld/anjal-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anjal-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/anjal-app/vocabulary/anjal-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anjal-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anjal-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/asyncapi/anjal-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/anjal-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/data-model/anjal-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anjal-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/anjal-app/cli/anjal-app-cli.yml
  title: ''
  type: CLI
  url: cli/anjal-app-cli.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/conventions/anjal-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/anjal-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/conventions/anjal-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anjal-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/anjal-app/authentication/anjal-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anjal-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/lifecycle/anjal-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anjal-app-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/errors/anjal-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anjal-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anjal-app/conformance/anjal-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anjal-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anjal-app/llms/anjal-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anjal-app-llms.txt
- group: other
  href: https://artifacts.apis.io/anjal-app/hosts/anjal-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anjal-app-hosts.yml
- group: build
  href: https://artifacts.apis.io/anjal-app/packages/anjal-app-packages.yml
  title: ''
  type: Packages
  url: packages/anjal-app-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://anjal.app/kb/sdk
- group: auth
  href: https://artifacts.apis.io/anjal-app/security/anjal-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anjal-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anjal.app/
- group: docs
  title: ''
  type: Documentation
  url: https://anjal.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anjal.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://anjal.app/download
- group: company
  title: ''
  type: Blog
  url: https://anjal.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kamskans
- group: commercial
  title: ''
  type: Pricing
  url: https://anjal.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://anjal.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anjal.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anjal.app/privacy
created: '2026-11-01'
description: Anjal provides email infrastructure designed for AI agents, allowing users to connect their preferred AI (Claude, ChatGPT, Codex, etc.) to manage inboxes on custom domains. It offers multi‑tenant workspaces, secure mail protection with prompt‑injection scanning, and a REST API plus TypeScript SDK for developers to integrate email handling into autonomous agents.
image: https://anjal.app/og-image.png?v=2
json_schemas:
- name: CadenceStepInput
  property_count: 8
  slug: anjal-app-cadence-step-input
- name: DraftInput
  property_count: 9
  slug: anjal-app-draft-input
- name: LinkedInSignalMatch
  property_count: 12
  slug: anjal-app-linked-in-signal-match
- name: LinkedInSignal
  property_count: 22
  slug: anjal-app-linked-in-signal
- name: Message
  property_count: 23
  slug: anjal-app-message
- name: WebhookEvent
  property_count: 0
  slug: anjal-app-webhook-event
jsonld:
- class_count: 34
  name: Anjal App Context
  property_count: 157
  slug: anjal-app-context
layout: provider
modified: '2026-11-01'
name: Anjal
nav: Providers
network: true
overview: 'Anjal publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Cadences API, Domains API, and 14 more. Tagged areas include Email, Artificial Intelligence, Agents, Software-as-a-Service, and Email API.


  The Anjal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Anjal''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Anjal App Plans Pricing
  plan_count: 3
  slug: anjal-app-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Anjal App Rate Limits
  slug: anjal-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Anjal API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: anjal-app-rules
scopes:
- name: Anjal App Scopes
  scope_count: 0
  slug: anjal-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 66.9
    developer_ergonomics: 43.5
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
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
  name: Anjal App Authentication
  slug: anjal-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Anjal App Domain Security
  slug: anjal-app-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: email-and-linkedin
  slug: anjal-app-email-and-linkedin
slug: anjal-app
tags:
- Email
- Artificial Intelligence
- Agents
- Software-as-a-Service
- Email API
website: https://anjal.app/
---
