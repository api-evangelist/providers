---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Rybbit Agentic Access
  operation_count: 10
  slug: rybbit-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 1
apis:
- baseURL: https://app.rybbit.io/api
  baseurl_source: declared
  description: Stats API for events and reporting per site.
  name: Rybbit Analytics API
  phrasing_intents:
  - id: listUsers
    intent: List the visitors tracked on a site
    question: Can I page through every user Rybbit has recorded for one of my sites?
  - id: getUser
    intent: Look up one visitor's profile
    question: How do I pull up the profile of a single visitor by their user ID?
  - id: listUserSessions
    intent: List every visit made by one user
    question: Which visits has one particular user made to my site over time?
  - id: getUserSessionCount
    intent: Count sessions per user on a site
    question: How many times has each user come back to my site?
  - id: getJourneys
    intent: See common navigation paths through a site
    question: What paths do visitors usually take from page to page on my site?
  phrasing_ops: 5
  slug: rybbit-analytics-api
- baseURL: https://app.rybbit.io/api
  baseurl_source: declared
  description: Public ingestion endpoint for pageviews and custom events.
  name: Rybbit Event Tracking API
  phrasing_intents:
  - id: trackEvent
    intent: Record a pageview or custom event
    question: How do I send a pageview to Rybbit from my server instead of the tracking script?
  phrasing_ops: 1
  slug: rybbit-event-tracking-api
- baseURL: https://app.rybbit.io/api
  baseurl_source: declared
  description: Session-level analytics and cohort retention.
  name: Rybbit Sessions API
  phrasing_intents:
  - id: listSessions
    intent: List sessions on a site
    question: How do I list all the visits to my site between two dates?
  - id: getSession
    intent: Replay the pageviews and events of one session
    question: What pages did a visitor view, in order, during one specific session?
  - id: listSessionLocations
    intent: Map where a site's sessions come from
    question: Where in the world are my site's visits coming from?
  - id: getRetention
    intent: Analyze cohort retention for a site
    question: How many visitors come back after their first visit, grouped by cohort?
  phrasing_ops: 4
  slug: rybbit-sessions-api
artifact_total: 23
collections:
- collection_type: open
  name: Rybbit Analytics API
  slug: open-rybbit-analytics-api
- collection_type: open
  name: Rybbit Analytics Event Tracking API
  slug: open-rybbit-event-tracking-api
- collection_type: open
  name: Rybbit Analytics Sessions API
  slug: open-rybbit-sessions-api
- collection_type: open
  name: Rybbit API
  slug: open-rybbit
common:
- group: other
  href: https://artifacts.apis.io/rybbit/capabilities/rybbit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/rybbit-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/rybbit-io/rybbit/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/rybbit/agentic-access/rybbit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rybbit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rybbit/security/rybbit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rybbit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/rybbit/security/rybbit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rybbit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rybbit/security/rybbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rybbit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rybbit/authentication/rybbit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rybbit-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://rybbit.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rybbit-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rybbit
- group: company
  title: ''
  type: Website
  url: https://www.rybbit.io
- group: docs
  title: ''
  type: Documentation
  url: https://rybbit.com/docs
- group: commercial
  href: https://artifacts.apis.io/rybbit/plans/rybbit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rybbit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/rybbit/rate-limits/rybbit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rybbit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rybbit/finops/rybbit-finops.yml
  title: ''
  type: FinOps
  url: finops/rybbit-finops.yml
- group: agent
  href: https://artifacts.apis.io/rybbit/well-known/rybbit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rybbit-well-known.yml
- group: auth
  href: https://artifacts.apis.io/rybbit/well-known/rybbit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rybbit-security.txt
- group: agent
  href: https://artifacts.apis.io/rybbit/mcp/rybbit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rybbit-mcp.yml
- group: build
  href: https://artifacts.apis.io/rybbit/mcp/rybbit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rybbit-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/rybbit/llms/rybbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rybbit-llms.txt
- group: auth
  href: https://artifacts.apis.io/rybbit/scopes/rybbit-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/rybbit-scopes.yml
- group: design
  href: https://artifacts.apis.io/rybbit/conventions/rybbit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rybbit-conventions.yml
- group: design
  href: https://artifacts.apis.io/rybbit/errors/rybbit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rybbit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rybbit/lifecycle/rybbit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rybbit-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/rybbit/changelog/rybbit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rybbit-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/rybbit-io/rybbit/releases
- group: build
  href: https://artifacts.apis.io/rybbit/packages/rybbit-packages.yml
  title: ''
  type: Packages
  url: packages/rybbit-packages.yml
- group: build
  href: https://artifacts.apis.io/rybbit/packages/rybbit-packages.yml
  title: ''
  type: SDKs
  url: packages/rybbit-packages.yml
- group: design
  href: https://artifacts.apis.io/rybbit/conformance/rybbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rybbit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://rybbit.com/security
- group: auth
  title: ''
  type: Security
  url: https://rybbit.com/security
- group: start
  href: https://artifacts.apis.io/rybbit/sandbox/rybbit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rybbit-sandbox.yml
- group: design
  href: https://artifacts.apis.io/rybbit/components/rybbit-components.yml
  title: ''
  type: Components
  url: components/rybbit-components.yml
- group: design
  href: https://artifacts.apis.io/rybbit/data-model/rybbit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rybbit-data-model.yml
- group: other
  href: https://artifacts.apis.io/rybbit/overlays/rybbit-analytics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rybbit-analytics-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/rybbit/overlays/rybbit-sessions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rybbit-sessions-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/rybbit/overlays/rybbit-event-tracking-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rybbit-event-tracking-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rybbit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rybbit.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rybbit.com/docs/api/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://rybbit.com/docs/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://rybbit.com/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/DEhGb4hYBj
- group: commercial
  title: ''
  type: Pricing
  url: https://rybbit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.rybbit.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.rybbit.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rybbit.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rybbit.com/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rybbit-io/rybbit
created: '2026-06-21'
description: Rybbit is an open-source, privacy-friendly web and product analytics platform positioned as a cookieless alternative to Google Analytics and Plausible. It ingests pageviews, custom events, autocaptured interactions, performance samples and JavaScript errors through a lightweight tracking script and an HTTP /api/track endpoint, and exposes a Bearer-key-authenticated Stats and Management API covering sites, sessions, users, goals, funnels, web vitals, session replays, organizations and teams. Since v2.8.0 Rybbit also runs a first-party hosted Model Context Protocol server at https://app.rybbit.io/api/mcp — 38 tools behind an OAuth 2.1 authorization server with PKCE, dynamic client registration and a 29-scope resource:action permission model — making it directly callable by AI agents. Rybbit publishes no OpenAPI. It can be self-hosted under AGPL-3.0, which ships the identical REST and MCP surface, or consumed as a managed cloud service.
finops:
- has_sources: true
  method: derived
  name: Rybbit Finops
  primary_unit: 100k monthly pageviews
  service_category: ''
  slug: rybbit-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rybbit.png
layout: provider
mcp_servers:
- description: Rybbit ships a first-party HOSTED (remote) Model Context Protocol server as part of the product — the same server code is in the AGPL-3.0 repository, so a self-hosted instance exposes it at <BASE_URL>
  name: Rybbit MCP Server
  slug: rybbit
modified: '2026-08-13'
name: Rybbit
nav: Providers
network: true
overview: 'Rybbit publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Analytics API, Event Tracking API, and Sessions API. Tagged areas include Analytics, Web Analytics, Product Analytics, Privacy, and Open Source.


  The Rybbit catalog on APIs.io includes 1 Spectral governance ruleset.


  Rybbit''s developer surface includes authentication, engineering blog, documentation, changelog, sandbox, API reference, getting-started guide, and 42 more developer resources.'
plans:
- name: Rybbit Plans Pricing
  plan_count: 3
  slug: rybbit-plans-pricing
- name: Rybbit Price Estimates
  plan_count: 0
  slug: rybbit-price-estimates
random_paper: 4
rate_limits:
- limit_count: 5
  name: Rybbit Rate Limits
  slug: rybbit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Rybbit API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: rybbit-rules
scopes:
- name: Rybbit Scopes
  scope_count: 29
  slug: rybbit-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 48.2
    developer_ergonomics: 74.4
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rybbit/rybbit-2026-08-17T080417.png
security:
- kind: authentication
  name: Rybbit Authentication
  slug: rybbit-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Rybbit Domain Security
  slug: rybbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rybbit Vulnerability Disclosure
  slug: rybbit-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Rybbit Trust Center
  slug: rybbit-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: Analyze sessions and cohort retention for a Rybbit site
  slug: rybbit-analyze-sessions
- name: Connect an agent to Rybbit's hosted MCP server
  slug: rybbit-connect-mcp
- name: Profile identified users and their journeys in Rybbit
  slug: rybbit-profile-users
- name: Send pageviews and custom events to Rybbit
  slug: rybbit-send-events
slug: rybbit
tags:
- Analytics
- Web Analytics
- Product Analytics
- Privacy
- Open Source
- Cookieless
website: https://www.rybbit.io
---
