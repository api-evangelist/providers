---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cogny Agentic Access
  operation_count: 15
  slug: cogny-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.cogny.com/v1
  baseurl_source: declared
  description: AI-powered growth report generation with streaming responses.
  name: Cogny Reports API
  phrasing_intents:
  - id: listReports
    intent: List growth reports
    question: Which growth reports have I generated so far in Cogny?
  - id: createReport
    intent: Start an AI-generated growth report
    question: How do I ask a plain-English question and get an AI growth report from my warehouse data?
  - id: getReport
    intent: Check a report's status
    question: Is my growth report finished yet or still generating?
  - id: cancelReport
    intent: Cancel a report in progress
    question: Can I stop a growth report that's taking too long to generate?
  - id: streamReport
    intent: Stream live progress of a report
    question: Can I watch a report's queries, insights and charts appear live as it's being generated?
  - id: getReportContent
    intent: Get a finished report's content
    question: Where do I fetch the full findings of a completed growth report?
  phrasing_ops: 6
  slug: cogny-reports-api
- baseURL: https://api.cogny.com/v1
  baseurl_source: declared
  description: AI-generated growth tickets (recommendations) management.
  name: Cogny Tickets API
  phrasing_intents:
  - id: listTickets
    intent: List growth tickets
    question: Which growth tickets are open for my team right now?
  - id: getTicket
    intent: Get one growth ticket
    question: How do I look up the details of a single growth ticket?
  - id: updateTicket
    intent: Update a growth ticket
    question: Can I reassign a single growth ticket to someone else on my team?
  - id: bulkUpdateTickets
    intent: Update many tickets at once
    question: Is there a way to change a whole batch of tickets in one call?
  - id: dismissTicket
    intent: Dismiss a growth ticket
    question: How do I dismiss a growth ticket that isn't relevant to us?
  - id: getTicketStats
    intent: Get growth ticket statistics
    question: What do my growth tickets look like in aggregate?
  - id: exportTickets
    intent: Export growth tickets to a file
    question: Can I download my growth tickets as a file to share outside the app?
  phrasing_ops: 7
  slug: cogny-tickets-api
- baseURL: https://api.cogny.com/v1
  baseurl_source: declared
  description: Connected data-warehouse resources.
  name: Cogny Warehouses API
  phrasing_intents:
  - id: listWarehouses
    intent: List connected data warehouses
    question: Which data warehouses have I connected to Cogny?
  phrasing_ops: 1
  slug: cogny-warehouses-api
- baseURL: https://api.cogny.com/v1
  baseurl_source: declared
  description: Webhook subscription configuration.
  name: Cogny Webhooks API
  phrasing_intents:
  - id: createWebhook
    intent: Subscribe a URL to webhook events
    question: How do I get notified at my own endpoint when something happens in Cogny?
  phrasing_ops: 1
  slug: cogny-webhooks-api
artifact_total: 23
asyncapis:
- description: ''
  name: Cogny Webhooks
  slug: cogny-webhooks
collections:
- collection_type: open
  name: Cogny Reports API
  slug: open-cogny-reports-api
- collection_type: open
  name: Cogny Reports Tickets API
  slug: open-cogny-tickets-api
- collection_type: open
  name: Cogny Reports Warehouses API
  slug: open-cogny-warehouses-api
- collection_type: open
  name: Cogny Reports Webhooks API
  slug: open-cogny-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/cogny/plans/cogny-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cogny-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cogny/rate-limits/cogny-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cogny-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cogny.com/pricing
- group: other
  href: https://artifacts.apis.io/cogny/capabilities/cogny-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cogny-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.cogny.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cogny.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cogny.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cogny.com/docs/api-overview-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://cogny.com/solo
- group: company
  title: ''
  type: Blog
  url: https://cogny.com/blog
- group: operate
  title: ''
  type: Support
  url: https://cogny.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cognyai
- group: commercial
  title: ''
  type: Pricing
  url: https://cogny.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cogny.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cogny.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cogny.com/privacy
- group: agent
  href: https://artifacts.apis.io/cogny/llms/cogny-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cogny-llms.txt
- group: agent
  href: https://artifacts.apis.io/cogny/well-known/cogny-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cogny-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cogny/mcp/cogny-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cogny-mcp.yml
- group: build
  href: https://artifacts.apis.io/cogny/mcp/cogny-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cogny-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/cogny/packages/cogny-packages.yml
  title: ''
  type: Packages
  url: packages/cogny-packages.yml
- group: build
  href: https://artifacts.apis.io/cogny/packages/cogny-packages.yml
  title: ''
  type: SDKs
  url: packages/cogny-packages.yml
- group: build
  href: https://artifacts.apis.io/cogny/cli/cogny-cli.yml
  title: ''
  type: CLI
  url: cli/cogny-cli.yml
- group: auth
  href: https://artifacts.apis.io/cogny/authentication/cogny-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cogny-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cogny/scopes/cogny-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cogny-scopes.yml
- group: design
  href: https://artifacts.apis.io/cogny/conventions/cogny-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cogny-conventions.yml
- group: design
  href: https://artifacts.apis.io/cogny/errors/cogny-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/cogny-error-codes.yml
- group: design
  href: https://artifacts.apis.io/cogny/lifecycle/cogny-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cogny-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cogny/conformance/cogny-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cogny-conformance.yml
- group: design
  href: https://artifacts.apis.io/cogny/asyncapi/cogny-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cogny-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cogny/data-model/cogny-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cogny-data-model.yml
- group: start
  href: https://artifacts.apis.io/cogny/sandbox/cogny-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cogny-sandbox.yml
- group: other
  href: https://artifacts.apis.io/cogny/overlays/cogny-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cogny-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cogny/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cogny/skills/cogny-published-skills.yml
  title: ''
  type: AgentSkill
  url: skills/cogny-published-skills.yml
- group: agent
  href: https://artifacts.apis.io/cogny/agentic-access/cogny-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cogny-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cogny/security/cogny-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cogny-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/cogny/plans/cogny-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cogny-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cogny/rate-limits/cogny-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cogny-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/cogny/security/cogny-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cogny-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cogny/security/cogny-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cogny-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cogny/security/cogny-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cogny-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cogny/security/cogny-trust-center.yml
  title: ''
  type: Compliance
  url: security/cogny-trust-center.yml
created: '2026-07-17'
description: 'Cogny is a Stockholm-based AI marketing platform (Cogny AB) that runs marketing analytics and automation on autopilot for marketers and data teams. It connects ad accounts and data warehouses (Google BigQuery, Google Ads, Meta Ads, LinkedIn, GA4, Search Console, TikTok, X, Mailchimp and more) to any MCP-capable coding agent, exposing ~50 Model Context Protocol tools plus a REST API for AI-generated growth reports (with SSE streaming) and growth tickets. Cogny is deeply agent-native: a one-command install manifest (SKILL.md), an auth.md registration handshake that issues anonymous cogny_lite_* API keys with no browser bounce, an @cogny/cli, a public library of 53 first-party Agent Skills, and machine-readable llms.txt and .well-known discovery surfaces.'
finops:
- has_sources: true
  method: derived
  name: Cogny Finops
  primary_unit: subscription
  service_category: ''
  slug: cogny-finops
  template: false
image: https://app.cogny.com/logo512.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.cogny.com over HTTP.
  name: Cogny MCP Server
  slug: cogny
modified: '2026-08-13'
name: Cogny
nav: Providers
network: true
overview: 'Cogny publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Reports API, Tickets API, Warehouses API, and 1 more. Tagged areas include Company, Ai Enterprise Software, Marketing, Marketing Analytics, and Marketing Automation.


  The Cogny catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cogny''s developer surface includes pricing, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 36 more developer resources.'
plans:
- name: Cogny Plans Pricing
  plan_count: 5
  slug: cogny-plans-pricing
- name: Cogny Price Estimates
  plan_count: 0
  slug: cogny-price-estimates
random_paper: 16
rate_limits:
- limit_count: 4
  name: Cogny Rate Limits
  slug: cogny-rate-limits
scopes:
- name: Cogny Scopes
  scope_count: 8
  slug: cogny-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 55.6
    developer_ergonomics: 85.7
    discoverability: 65.0
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cogny/cogny-2026-07-25T210014.png
security:
- kind: authentication
  name: Cogny Authentication
  slug: cogny-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Cogny Domain Security
  slug: cogny-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cogny Vulnerability Disclosure
  slug: cogny-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cogny Trust Center
  slug: cogny-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: cogny
  slug: cogny-SKILL
- name: Generate and stream a growth report
  slug: cogny-create-and-stream-report
- name: Triage growth tickets
  slug: cogny-triage-growth-tickets
slug: cogny
tags:
- Company
- Ai Enterprise Software
- Marketing
- Marketing Analytics
- Marketing Automation
- MCP
- Agents
- Data Warehouse
- Advertising
website: https://www.cogny.com/
---
