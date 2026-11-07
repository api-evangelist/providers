---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote MCP server that lets an AI assistant (Claude, ChatGPT, Cursor or any client supporting remote MCP) build, preview, edit and publish DimensionKit scorecards. Connecting takes only the server URL
  name: DimensionKit MCP Server
  slug: dimensionkit-mcp-server
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/dimensionkit-com/rate-limits/dimensionkit-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dimensionkit-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dimensionkit-com/plans/dimensionkit-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dimensionkit-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dimensionkit-com/components/dimensionkit-com-components.yml
  title: ''
  type: Components
  url: components/dimensionkit-com-components.yml
- group: design
  href: https://artifacts.apis.io/dimensionkit-com/conventions/dimensionkit-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dimensionkit-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/dimensionkit-com/conventions/dimensionkit-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dimensionkit-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/security/dimensionkit-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dimensionkit-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/authentication/dimensionkit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dimensionkit-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/scopes/dimensionkit-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dimensionkit-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/dimensionkit-com/lifecycle/dimensionkit-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dimensionkit-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dimensionkit-com/conformance/dimensionkit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dimensionkit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dimensionkit-com/llms/dimensionkit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dimensionkit-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dimensionkit-com/mcp/dimensionkit-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dimensionkit-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/well-known/dimensionkit-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dimensionkit-com-security.txt
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/well-known/dimensionkit-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dimensionkit-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dimensionkit-com/well-known/dimensionkit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dimensionkit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dimensionkit-com/hosts/dimensionkit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dimensionkit-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/dimensionkit-com/integrations/dimensionkit-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dimensionkit-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dimensionkit-com/vendors/dimensionkit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dimensionkit-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dimensionkit-com/packages/dimensionkit-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dimensionkit-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dimensionkit-com/packages/dimensionkit-com-packages.yml
  title: ''
  type: Packages
  url: packages/dimensionkit-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/security/dimensionkit-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dimensionkit-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dimensionkit-com/security/dimensionkit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimensionkit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dimensionkit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dimensionkit.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://dimensionkit.com/docs/mcp/connecting/
- group: company
  title: ''
  type: Blog
  url: https://dimensionkit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dimensionkit.com/pricing
- group: company
  title: ''
  type: About
  url: https://dimensionkit.com/about
- group: start
  title: ''
  type: Login
  url: https://app.dimensionkit.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.dimensionkit.com/admin/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dimensionkit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dimensionkit.com/privacy
created: '2026-11-05'
description: DimensionKit turns an expert's framework into an interactive, scored assessment (scorecard) built by the AI assistant the user already uses. Creators connect DimensionKit to Claude, ChatGPT, Cursor or any assistant that supports remote MCP via the server URL https://app.dimensionkit.com/mcp; the assistant writes the dimensions, scored questions and tiers and previews them before publishing. Visitors get a personalised result (and can answer from a plain-text version with their own AI), while the creator captures the lead, answers and per-dimension scores. Built by Worbee EOOD in Bulgaria, EU; in open beta and free during the beta.
image: https://dimensionkit.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.dimensionkit.com requiring OAuth; 17 tools listed.
  name: DimensionKit MCP Server
  slug: dimensionkit-mcp-server
modified: '2026-11-05'
name: DimensionKit
nav: Providers
network: true
overview: 'DimensionKit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Assessment, Scorecards, Lead Generation, and MCP.


  DimensionKit''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Dimensionkit Com Plans Pricing
  plan_count: 3
  slug: dimensionkit-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Dimensionkit Com Rate Limits
  slug: dimensionkit-com-rate-limits
scopes:
- name: Dimensionkit Com Scopes
  scope_count: 2
  slug: dimensionkit-com-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dimensionkit Com Authentication
  slug: dimensionkit-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dimensionkit Com Domain Security
  slug: dimensionkit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dimensionkit Com Vulnerability Disclosure
  slug: dimensionkit-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dimensionkit-com
tags:
- Company
- Assessment
- Scorecards
- Lead Generation
- MCP
- Artificial Intelligence
- Quizzes
website: https://dimensionkit.com/
---
