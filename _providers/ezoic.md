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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ezoic Agentic Access
  operation_count: 3
  slug: ezoic-agentic-access
  summary_line: 3 operations
api_count: 5
apis:
- description: The Access API from ezoic — 1 operation(s) for access.
  name: ezoic Access API
  slug: ezoic-access-api
- description: The Products API from ezoic — 1 operation(s) for products.
  name: ezoic Products API
  slug: ezoic-products-api
- description: The Purchases API from ezoic — 1 operation(s) for purchases.
  name: ezoic Purchases API
  slug: ezoic-purchases-api
- description: The Big Data Analytics (BDA) REST API pulls the same reports and analytics data a publisher sees in the Ezoic dashboard — predefined reports that ship with the account and custom reports the publisher
  name: ezoic Big Data Analytics API
  slug: ezoic-big-data-analytics-api
- description: The CDN REST API clears and purges cached content on the Ezoic CDN — a single URL, a batch of URLs in groups of 100, a comma-separated set of surrogate keys, or a whole domain — plus a ping liveness c
  name: ezoic CDN API
  slug: ezoic-cdn-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ezoic Subscriptions Server-to-Server REST Access API
  slug: open-ezoic-access-api
- collection_type: open
  name: Ezoic Subscriptions Server-to-Server REST Access Products API
  slug: open-ezoic-products-api
- collection_type: open
  name: Ezoic Subscriptions Server-to-Server REST Access Purchases API
  slug: open-ezoic-purchases-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ezoic-subscriptions-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ezoic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ezoic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ezoic.com/docs/subscriptions/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ezoic.com/docs/ezoicads/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://support.ezoic.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.ezoic.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ezoic.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ezoic
- group: operate
  title: ''
  type: StatusPage
  url: https://ezoicstatus.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ezoic.com/docs/ezoic-legacy-features/legacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ezoic.com/pricing
- group: start
  title: ''
  type: Login
  url: https://pubdash.ezoic.com/
- group: start
  title: ''
  type: SignUp
  url: https://admin.bidsystem.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ezoic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ezoic.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ezoic-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ezoic-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ezoic-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ezoic-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ezoic-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ezoic-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ezoic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ezoic-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/ezoic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ezoic-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezoic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ezoic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ezoic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ezoic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ezoic-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ezoic-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ezoic-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ezoic-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ezoic.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ezoic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezoic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ezoic.com/
created: '2026-07-17'
description: 'Ezoic is a website monetization and audience-growth platform for publishers, and a performance advertising marketplace for brands. Publishers integrate EzoicAds (via JavaScript, mobile SDKs for Android/iOS/Flutter/React Native/Unity, or framework SDKs for Angular/React/Vue) to run native, sticky, video, anchor, rewarded, and interstitial ad formats across 5,000+ premium sites. Beyond ads, Ezoic offers first-party Identity (ezID), Visitor Accounts (ezAuth), Ezoic Subscriptions (paywalls, donations, and a server-to-server REST API for verifying reader access), a Web Games ad SDK, and Custom Events into its Big Data Analytics platform. Its developer surface is a single API gateway (api-gateway.ezoic.com) fronting three services enabled individually from the dashboard and sharing one developerKey — Big Data Analytics for reports, segments and custom data; CDN for cache clearing and purging; and Subscriptions for server-side reader entitlement checks. Ezoic also runs three hosted
  MCP servers: a read-only Analytics server over OAuth, an anonymous Setup Assistant listed in the official MCP Registry as com.ezoic/setup, and an OAuth-gated endpoint on bidsystem.ai, its performance advertising platform for brands.'
image: https://www.ezoic.com/wp-content/uploads/2021/03/ezoic-logo.png
layout: provider
mcp_servers:
- description: ''
  name: ezoic MCP Server
  slug: ezoic-mcp-server
modified: '2026-08-13'
name: ezoic
nav: Providers
network: true
overview: 'ezoic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Access API, Products API, Purchases API, and 2 more. Tagged areas include Company, Advertising, AdTech, Publisher Monetization, and Analytics.


  ezoic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Ezoic Plans Pricing
  plan_count: 3
  slug: ezoic-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Ezoic Rate Limits
  slug: ezoic-rate-limits
scopes:
- name: Ezoic Scopes
  scope_count: 0
  slug: ezoic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.7
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 30.3
    contract_quality: 57.6
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 36.8
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezoic/refs/heads/main/screenshots/ezoic-2026-07-25T214052.png
security:
- kind: authentication
  name: Ezoic Authentication
  slug: ezoic-authentication
  summary_line: apiKey/oauth2 · 6 schemes
- kind: domain-security
  name: Ezoic Domain Security
  slug: ezoic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ezoic Vulnerability Disclosure
  slug: ezoic-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ezoic
tags:
- Company
- Advertising
- AdTech
- Publisher Monetization
- Analytics
- Reporting
- Subscription
- Paywalls
- Identity
- CDN
- Caching
- MCP
- Authentication
- Agents
website: https://www.ezoic.com/
---
