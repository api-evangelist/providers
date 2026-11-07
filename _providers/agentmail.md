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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Agentmail Agentic Access
  operation_count: 119
  slug: agentmail-agentic-access
  summary_line: 119 operations · 57 acting
api_count: 2
apis:
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The agent API from AgentMail — 2 operation(s) for agent.
  name: AgentMail Agent API
  slug: agentmail-agent-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The api-keys API from AgentMail — 2 operation(s) for api-keys.
  name: AgentMail API Keys API
  slug: agentmail-api-keys-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The auth API from AgentMail — 1 operation(s) for auth.
  name: AgentMail Auth API
  slug: agentmail-auth-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The domains API from AgentMail — 4 operation(s) for domains.
  name: AgentMail Domains API
  slug: agentmail-domains-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The drafts API from AgentMail — 3 operation(s) for drafts.
  name: AgentMail Drafts API
  slug: agentmail-drafts-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > api-keys API from AgentMail — 2 operation(s) for inboxes > api-keys.
  name: AgentMail inboxes > api-keys API
  slug: agentmail-inboxes-api-keys-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes API from AgentMail — 2 operation(s) for inboxes.
  name: AgentMail Inboxes API
  slug: agentmail-inboxes-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > drafts API from AgentMail — 4 operation(s) for inboxes > drafts.
  name: AgentMail inboxes > drafts API
  slug: agentmail-inboxes-drafts-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > events API from AgentMail — 1 operation(s) for inboxes > events.
  name: AgentMail inboxes > events API
  slug: agentmail-inboxes-events-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > lists API from AgentMail — 2 operation(s) for inboxes > lists.
  name: AgentMail inboxes > lists API
  slug: agentmail-inboxes-lists-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > messages API from AgentMail — 11 operation(s) for inboxes > messages.
  name: AgentMail inboxes > messages API
  slug: agentmail-inboxes-messages-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > metrics API from AgentMail — 2 operation(s) for inboxes > metrics.
  name: AgentMail inboxes > metrics API
  slug: agentmail-inboxes-metrics-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > threads API from AgentMail — 4 operation(s) for inboxes > threads.
  name: AgentMail inboxes > threads API
  slug: agentmail-inboxes-threads-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > webhooks API from AgentMail — 2 operation(s) for inboxes > webhooks.
  name: AgentMail inboxes > webhooks API
  slug: agentmail-inboxes-webhooks-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The lists API from AgentMail — 2 operation(s) for lists.
  name: AgentMail Lists API
  slug: agentmail-lists-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The metrics API from AgentMail — 2 operation(s) for metrics.
  name: AgentMail Metrics API
  slug: agentmail-metrics-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The organizations API from AgentMail — 1 operation(s) for organizations.
  name: AgentMail Organizations API
  slug: agentmail-organizations-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > api-keys API from AgentMail — 2 operation(s) for pods > api-keys.
  name: AgentMail pods > api-keys API
  slug: agentmail-pods-api-keys-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods API from AgentMail — 2 operation(s) for pods.
  name: AgentMail Pods API
  slug: agentmail-pods-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > domains API from AgentMail — 4 operation(s) for pods > domains.
  name: AgentMail pods > domains API
  slug: agentmail-pods-domains-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > drafts API from AgentMail — 3 operation(s) for pods > drafts.
  name: AgentMail pods > drafts API
  slug: agentmail-pods-drafts-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > inboxes API from AgentMail — 2 operation(s) for pods > inboxes.
  name: AgentMail pods > inboxes API
  slug: agentmail-pods-inboxes-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > lists API from AgentMail — 2 operation(s) for pods > lists.
  name: AgentMail pods > lists API
  slug: agentmail-pods-lists-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > metrics API from AgentMail — 2 operation(s) for pods > metrics.
  name: AgentMail pods > metrics API
  slug: agentmail-pods-metrics-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > threads API from AgentMail — 4 operation(s) for pods > threads.
  name: AgentMail pods > threads API
  slug: agentmail-pods-threads-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > webhooks API from AgentMail — 2 operation(s) for pods > webhooks.
  name: AgentMail pods > webhooks API
  slug: agentmail-pods-webhooks-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The threads API from AgentMail — 4 operation(s) for threads.
  name: AgentMail Threads API
  slug: agentmail-threads-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The webhooks API from AgentMail — 2 operation(s) for webhooks.
  name: AgentMail Webhooks API
  slug: agentmail-webhooks-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The accounts API from AgentMail — 3 operation(s) for accounts.
  name: AgentMail Accounts API
  slug: agentmail-accounts-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The apps API from AgentMail — 5 operation(s) for apps.
  name: AgentMail Apps API
  slug: agentmail-apps-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > accounts API from AgentMail — 2 operation(s) for inboxes > accounts.
  name: AgentMail inboxes > accounts API
  slug: agentmail-inboxes-accounts-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > calendar API from AgentMail — 6 operation(s) for inboxes > calendar.
  name: AgentMail inboxes > calendar API
  slug: agentmail-inboxes-calendar-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > files API from AgentMail — 3 operation(s) for inboxes > files.
  name: AgentMail inboxes > files API
  slug: agentmail-inboxes-files-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The inboxes > webhooks > polling API from AgentMail — 2 operation(s) for inboxes > webhooks > polling.
  name: AgentMail inboxes > webhooks > polling API
  slug: agentmail-inboxes-webhooks-polling-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > accounts API from AgentMail — 2 operation(s) for pods > accounts.
  name: AgentMail pods > accounts API
  slug: agentmail-pods-accounts-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The pods > webhooks > polling API from AgentMail — 2 operation(s) for pods > webhooks > polling.
  name: AgentMail pods > webhooks > polling API
  slug: agentmail-pods-webhooks-polling-api
- baseURL: https://api.agentmail.to
  baseurl_source: declared
  description: The webhooks > polling API from AgentMail — 2 operation(s) for webhooks > polling.
  name: AgentMail webhooks > polling API
  slug: agentmail-webhooks-polling-api
artifact_total: 79
asyncapis:
- description: ''
  name: API Reference
  slug: agentmail-websockets-asyncapi
collections:
- collection_type: open
  name: API Reference agent API
  slug: open-agentmail-agent-api
- collection_type: open
  name: API Reference agent api-keys API
  slug: open-agentmail-api-keys-api
- collection_type: open
  name: API Reference agent auth API
  slug: open-agentmail-auth-api
- collection_type: open
  name: API Reference agent domains API
  slug: open-agentmail-domains-api
- collection_type: open
  name: API Reference agent drafts API
  slug: open-agentmail-drafts-api
- collection_type: open
  name: API Reference agent inboxes > api-keys API
  slug: open-agentmail-inboxes-api-keys-api
- collection_type: open
  name: API Reference agent inboxes API
  slug: open-agentmail-inboxes-api
- collection_type: open
  name: API Reference agent inboxes > drafts API
  slug: open-agentmail-inboxes-drafts-api
- collection_type: open
  name: API Reference agent inboxes > events API
  slug: open-agentmail-inboxes-events-api
- collection_type: open
  name: API Reference agent inboxes > lists API
  slug: open-agentmail-inboxes-lists-api
- collection_type: open
  name: API Reference agent inboxes > messages API
  slug: open-agentmail-inboxes-messages-api
- collection_type: open
  name: API Reference agent inboxes > metrics API
  slug: open-agentmail-inboxes-metrics-api
- collection_type: open
  name: API Reference agent inboxes > threads API
  slug: open-agentmail-inboxes-threads-api
- collection_type: open
  name: API Reference agent inboxes > webhooks API
  slug: open-agentmail-inboxes-webhooks-api
- collection_type: open
  name: API Reference agent lists API
  slug: open-agentmail-lists-api
- collection_type: open
  name: API Reference agent metrics API
  slug: open-agentmail-metrics-api
- collection_type: open
  name: API Reference agent organizations API
  slug: open-agentmail-organizations-api
- collection_type: open
  name: API Reference agent pods > api-keys API
  slug: open-agentmail-pods-api-keys-api
- collection_type: open
  name: API Reference agent pods API
  slug: open-agentmail-pods-api
- collection_type: open
  name: API Reference agent pods > domains API
  slug: open-agentmail-pods-domains-api
- collection_type: open
  name: API Reference agent pods > drafts API
  slug: open-agentmail-pods-drafts-api
- collection_type: open
  name: API Reference agent pods > inboxes API
  slug: open-agentmail-pods-inboxes-api
- collection_type: open
  name: API Reference agent pods > lists API
  slug: open-agentmail-pods-lists-api
- collection_type: open
  name: API Reference agent pods > metrics API
  slug: open-agentmail-pods-metrics-api
- collection_type: open
  name: API Reference agent pods > threads API
  slug: open-agentmail-pods-threads-api
- collection_type: open
  name: API Reference agent pods > webhooks API
  slug: open-agentmail-pods-webhooks-api
- collection_type: open
  name: API Reference agent threads API
  slug: open-agentmail-threads-api
- collection_type: open
  name: API Reference agent webhooks API
  slug: open-agentmail-webhooks-api
common:
- group: operate
  href: https://artifacts.apis.io/agentmail/rate-limits/agentmail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentmail-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentmail/plans/agentmail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentmail-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentmail.to/
- group: other
  href: https://artifacts.apis.io/agentmail/capabilities/agentmail-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agentmail-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agentmail.to
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentmail.to
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentmail.to/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentmail.to/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.agentmail.to/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentmail.to/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.agentmail.to
- group: operate
  title: ''
  type: Support
  url: https://docs.agentmail.to/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentmail-to
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.agentmail.to/changelog
- group: docs
  href: https://artifacts.apis.io/agentmail/openapi/_original/agentmail-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/agentmail-openapi-original.yml
- group: docs
  href: https://artifacts.apis.io/agentmail/asyncapi/agentmail-websockets-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/agentmail-websockets-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.agentmail.to/webhooks-overview
- group: other
  href: https://artifacts.apis.io/agentmail/overlays/agentmail-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentmail-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/agentmail/authentication/agentmail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentmail-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agentmail/agentic-access/agentmail-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentmail-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/agentmail/security/agentmail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentmail-domain-security.yml
- group: build
  href: https://artifacts.apis.io/agentmail/packages/agentmail-packages.yml
  title: ''
  type: Packages
  url: packages/agentmail-packages.yml
- group: build
  href: https://artifacts.apis.io/agentmail/packages/agentmail-packages.yml
  title: ''
  type: SDKs
  url: packages/agentmail-packages.yml
- group: build
  href: https://artifacts.apis.io/agentmail/cli/agentmail-cli.yml
  title: ''
  type: CLI
  url: cli/agentmail-cli.yml
- group: agent
  href: https://artifacts.apis.io/agentmail/mcp/agentmail-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentmail-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentmail/llms/agentmail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentmail-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentmail/well-known/agentmail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentmail-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentmail/well-known/agentmail-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/agentmail-api-catalog.json
- group: design
  href: https://artifacts.apis.io/agentmail/conformance/agentmail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentmail-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.agentmail.to/documentation/resources/security-privacy/soc-2-compliance
- group: auth
  href: https://artifacts.apis.io/agentmail/security/agentmail-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentmail-trust-center.yml
- group: design
  href: https://artifacts.apis.io/agentmail/errors/agentmail-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentmail-error-codes.yml
- group: design
  href: https://artifacts.apis.io/agentmail/lifecycle/agentmail-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentmail-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agentmail/conventions/agentmail-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentmail-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentmail/conventions/agentmail-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentmail-conventions.yml
- group: operate
  href: https://artifacts.apis.io/agentmail/changelog/agentmail-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentmail-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentmail/data-model/agentmail-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentmail-data-model.yml
- group: agent
  href: https://artifacts.apis.io/agentmail/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'AgentMail is an API-first email platform that gives AI agents their own email inboxes to autonomously send, receive, reply to, and act on email. Unlike traditional transactional email APIs built for one-way notifications, AgentMail is designed for two-way threaded conversations: agents create inboxes on demand, read and semantically search messages, manage threads and drafts for human-in-the-loop review, apply labels and allow/block lists, and react to inbound mail in real time over webhooks or WebSockets. It ships a REST API (OpenAPI 3.1), an AsyncAPI 2.6 WebSocket surface, Python/Node/Go SDKs, a CLI, a hosted MCP server, and IMAP/SMTP bridges, with API-key permissions, idempotency, multi-tenant pods, custom domains, and SOC 2 Type I/II compliance.'
finops:
- has_sources: true
  method: derived
  name: Agentmail Finops
  primary_unit: subscription
  service_category: ''
  slug: agentmail-finops
  template: false
image: https://www.agentmail.to/logo.png
layout: provider
mcp_servers:
- description: 'Email inboxes for AI agents: send, receive, reply, search, and manage threaded email over MCP.'
  name: AgentMail
  slug: agentmail
modified: '2026-07-17'
name: AgentMail
nav: Providers
network: true
overview: 'AgentMail publishes 37 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, API Keys API, Auth API, and 34 more. Tagged areas include Company, Artificial Intelligence, Email, AI Agents, and Inbox.


  The AgentMail catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AgentMail''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 31 more developer resources.'
plans:
- name: Agentmail Plans Pricing
  plan_count: 4
  slug: agentmail-plans-pricing
- name: Agentmail Price Estimates
  plan_count: 0
  slug: agentmail-price-estimates
random_paper: 10
rate_limits:
- limit_count: 3
  name: Agentmail Rate Limits
  slug: agentmail-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: AgentMail API Rules
  rule_count: 54
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 11
  slug: agentmail-rules
score:
  band: strong
  composite: 64.7
  coverage:
    artifact_dirs: 34
    catalog_earned: 70.5
    catalog_earned_first_party: 24.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 78.9
    contract_governance: 24.2
    contract_quality: 60.9
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 57.9
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 66
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agentmail/agentmail-2026-07-25T195240.png
security:
- kind: authentication
  name: Agentmail Authentication
  slug: agentmail-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentmail Domain Security
  slug: agentmail-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Agentmail Trust Center
  slug: agentmail-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II
skill_count: 3
skills:
- name: Human-in-the-loop draft review
  slug: agentmail-human-in-the-loop-draft
- name: agentmail
  slug: agentmail-official-skill
- name: Send an email and handle the reply
  slug: agentmail-send-and-reply
slug: agentmail
tags:
- Company
- Artificial Intelligence
- Email
- AI Agents
- Inbox
- Messaging
- Webhook
- WebSocket
- SMTP
- IMAP
- MCP
- Developer Tools
- Real-Time
website: https://www.agentmail.to/
---
