---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-09-04'
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
  slug: rybbit-analytics-api
- baseURL: https://app.rybbit.io/api
  baseurl_source: declared
  description: Public ingestion endpoint for pageviews and custom events.
  name: Rybbit Event Tracking API
  slug: rybbit-event-tracking-api
- baseURL: https://app.rybbit.io/api
  baseurl_source: declared
  description: Session-level analytics and cohort retention.
  name: Rybbit Sessions API
  slug: rybbit-sessions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: commercial
  title: ''
  type: License
  url: https://github.com/rybbit-io/rybbit/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rybbit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rybbit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rybbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rybbit-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/rybbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rybbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rybbit-finops.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rybbit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rybbit-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rybbit-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rybbit-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rybbit-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rybbit-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rybbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rybbit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rybbit-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rybbit-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/rybbit-io/rybbit/releases
- group: build
  title: ''
  type: Packages
  url: packages/rybbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rybbit-packages.yml
- group: design
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
  title: ''
  type: Sandbox
  url: sandbox/rybbit-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/rybbit-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rybbit-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rybbit-analytics-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/rybbit-sessions-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/rybbit-event-tracking-api-overlay.yaml
- group: agent
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
- name: Rybbit Finops
  service_category: Analytics
  slug: rybbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rybbit.png
layout: provider
mcp_servers:
- description: Rybbit ships a first-party HOSTED (remote) Model Context Protocol server as part of the product — the same server code is in the AGPL-3.0 repository, so a self-hosted instance exposes it at <BASE_URL>
  name: Rybbit MCP Server
  slug: rybbit-mcp-server
modified: '2026-08-13'
name: Rybbit
nav: Providers
network: true
overview: 'Rybbit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Analytics API, Event Tracking API, and Sessions API. Tagged areas include Analytics, Web Analytics, Product Analytics, Privacy, and Open-Source.


  Rybbit''s developer surface includes authentication, engineering blog, documentation, changelog, sandbox, API reference, getting-started guide, and 41 more developer resources.'
plans:
- name: Rybbit Plans Pricing
  plan_count: 5
  slug: rybbit-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Rybbit Rate Limits
  slug: rybbit-rate-limits
scopes:
- name: Rybbit Scopes
  scope_count: 29
  slug: rybbit-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: strong
  composite: 65.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 74.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 66.6
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rybbit/refs/heads/main/screenshots/rybbit-2026-08-17T080417.png
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
slug: rybbit
tags:
- Analytics
- Web Analytics
- Product Analytics
- Privacy
- Open-Source
- Cookieless
website: https://www.rybbit.io
---
