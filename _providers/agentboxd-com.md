---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 76
  human_in_the_loop: 4
  name: Agentboxd Com Agentic Access
  operation_count: 137
  slug: agentboxd-com-agentic-access
  summary_line: 137 operations · 76 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: aSIM agent cards, keys and the agent directory.
  name: agentboxd-com Agent network API
  slug: agentboxd-com-agent-network-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: An agent creating its own workspace, and a person claiming it.
  name: agentboxd-com Agent self-signup API
  slug: agentboxd-com-agent-self-signup-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Everyone your agents have exchanged mail with, with notes and labels, and the addresses your sends skip (suppressions).
  name: agentboxd-com Contacts API
  slug: agentboxd-com-contacts-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Your own domains for sending and receiving.
  name: agentboxd-com Domains API
  slug: agentboxd-com-domains-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Messages a person reviews before they go out, and scheduled sends.
  name: agentboxd-com Drafts API
  slug: agentboxd-com-drafts-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: The realtime event stream over WebSocket.
  name: agentboxd-com Events API
  slug: agentboxd-com-events-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: 'Email addresses for agents: create, list, pause and delete them.'
  name: agentboxd-com Inboxes API
  slug: agentboxd-com-inboxes-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Documents your agents draw on for AI reply drafts.
  name: agentboxd-com Knowledge API
  slug: agentboxd-com-knowledge-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Allow and block lists for receiving, sending and replying.
  name: agentboxd-com Lists API
  slug: agentboxd-com-lists-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Send, reply, forward, read and label mail; wait for mail; claim it from a work queue.
  name: agentboxd-com Messages API
  slug: agentboxd-com-messages-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Sending, delivery and bounce numbers.
  name: agentboxd-com Metrics API
  slug: agentboxd-com-metrics-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: The Other API from agentboxd-com — 3 operation(s) for other.
  name: agentboxd-com Other API
  slug: agentboxd-com-other-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Full-text search over messages.
  name: agentboxd-com Search API
  slug: agentboxd-com-search-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: 'Sign in with Agentboxd: identity tokens, sign-in apps and identities without a mailbox.'
  name: agentboxd-com Shakehand API
  slug: agentboxd-com-shakehand-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Conversations, per inbox or across all of them.
  name: agentboxd-com Threads API
  slug: agentboxd-com-threads-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: The emergency stop and human on call.
  name: agentboxd-com Trust API
  slug: agentboxd-com-trust-api
- baseURL: https://api.agentboxd.com
  baseurl_source: declared
  description: Signed HTTP notifications for new mail and other events.
  name: agentboxd-com Webhooks API
  slug: agentboxd-com-webhooks-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/agentboxd-com/agentic-access/agentboxd-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentboxd-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/agentboxd-com/rate-limits/agentboxd-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentboxd-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/agentboxd-com/rules/agentboxd-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentboxd-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentboxd-com/json-ld/agentboxd-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentboxd-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentboxd-com/vocabulary/agentboxd-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentboxd-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentboxd-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentboxd-com/data-model/agentboxd-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentboxd-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentboxd-com/conventions/agentboxd-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentboxd-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentboxd-com/conventions/agentboxd-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentboxd-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agentboxd.com/security
- group: design
  href: https://artifacts.apis.io/agentboxd-com/errors/agentboxd-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentboxd-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentboxd-com/conformance/agentboxd-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentboxd-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentboxd-com/llms/agentboxd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentboxd-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentboxd-com/well-known/agentboxd-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentboxd-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agentboxd-com/well-known/agentboxd-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentboxd-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentboxd-com/hosts/agentboxd-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentboxd-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://agentboxd.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentboxd.com/changelog
- group: auth
  href: https://artifacts.apis.io/agentboxd-com/security/agentboxd-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentboxd-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agentboxd-com/security/agentboxd-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentboxd-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentboxd-com/security/agentboxd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentboxd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentboxd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentboxd.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://agentboxd.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentboxd.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://agentboxd.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://agentboxd.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentboxd
- group: operate
  title: ''
  type: Roadmap
  url: https://agentboxd.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://agentboxd.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://agentboxd.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentboxd.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentboxd.com/privacy
created: '2026-10-30'
description: Agentboxd provides email inboxes and sign‑in services for AI agents. Its Homingbox product offers AI agents a dedicated email address via a single API call, supporting AI triage, draft approvals, webhooks, WebSockets, SMTP, and MCP. The Shakehand product lets AI agents sign into applications. Additional offerings include aSIM, a SIM card for AI agents. The service is EU‑hosted, currently in public beta, free to start with paid plans forthcoming.
image: https://agentboxd.com/icon-512.png
jsonld:
- class_count: 1
  name: Agentboxd Com Context
  property_count: 1
  slug: agentboxd-com-context
layout: provider
modified: '2026-10-30'
name: agentboxd-com
nav: Providers
network: true
overview: 'agentboxd-com publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent network API, Agent self-signup API, Contacts API, and 14 more. Tagged areas include Artificial Intelligence, Email, Messaging, and Beta.


  The agentboxd-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agentboxd-com''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Agentboxd Com Plans Pricing
  plan_count: 0
  slug: agentboxd-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Agentboxd Com Rate Limits
  slug: agentboxd-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: agentboxd-com API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: agentboxd-com-rules
scopes:
- name: Agentboxd Com Scopes
  scope_count: 0
  slug: agentboxd-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 50.0
    catalog_earned_first_party: 8.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.5
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 54.8
    developer_ergonomics: 26.7
    discoverability: 57.1
    operational_transparency: 39.5
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentboxd-com/agentboxd-com-2026-11-03T120352.png
security:
- kind: authentication
  name: Agentboxd Com Authentication
  slug: agentboxd-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentboxd Com Domain Security
  slug: agentboxd-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentboxd Com Vulnerability Disclosure
  slug: agentboxd-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Agentboxd Com Trust Center
  slug: agentboxd-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: create-inbox
  slug: agentboxd-com-create-inbox
slug: agentboxd-com
tags:
- Artificial Intelligence
- Email
- Messaging
- Beta
website: https://agentboxd.com/
---
