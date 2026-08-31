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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Hosted Model Context Protocol server exposing SegmentStream's marketing measurement, attribution, budget-optimization, and BigQuery query capabilities as agent-callable tools (read-only reporting by d
  name: SegmentStream MCP
  slug: segmentstream-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://segmentstream.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.segmentstream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.segmentstream.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.segmentstream.com/mcp/getting-started
- group: company
  title: ''
  type: Blog
  url: https://segmentstream.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://segmentstream.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.segmentstream.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://segmentstream.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://segmentstream.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segmentstream
- group: operate
  title: ''
  type: StatusPage
  url: https://status.segmentstream.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/segmentstream-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/segmentstream-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/segmentstream-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/segmentstream-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/segmentstream-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/segmentstream-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/segmentstream-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/segmentstream-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/segmentstream-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/segmentstream-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/segmentstream-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://segmentstream.com/trust
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/segmentstream-a2a.yml
- group: build
  title: ''
  type: CLI
  url: cli/segmentstream-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/segmentstream-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/segmentstream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/segmentstream-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/segmentstream-error-codes.yml
- group: design
  title: ''
  type: Components
  url: components/segmentstream-components.yml
created: '2026-07-17'
description: SegmentStream is a marketing measurement platform that gives AI agents an attribution, budget-optimization, and incrementality-testing "brain." It consolidates first-party and third-party marketing data in Google BigQuery and applies ML-powered, cross-channel attribution across 20+ ad platforms (Google Ads, Meta, TikTok, LinkedIn, Microsoft, Snapchat, Pinterest, Reddit, Criteo, and more), then recommends budget reallocation via marginal-ROAS analysis and validates impact with geo-holdout incrementality experiments. Every capability is exposed as a tool through a hosted Model Context Protocol (MCP) server, so Claude, ChatGPT, Cursor, and any MCP client can query attribution reports, manage configuration, and run BigQuery SQL over a workspace. Backed by Techstars.
image: https://segmentstream.com/images/og-image.png
layout: provider
mcp_servers:
- description: 'Hosted remote MCP server that gives AI tools secure, read-only access to a SegmentStream workspace via the Model Context Protocol. Exposes marketing measurement, attribution, budget optimization, and '
  name: SegmentStream MCP Server
  slug: segmentstream-mcp-server
modified: '2026-08-13'
name: SegmentStream
nav: Providers
network: true
overview: 'SegmentStream publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Analytics, Attribution, Marketing Measurement, and Advertising.


  SegmentStream''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, authentication, CLI, and 24 more developer resources.'
plans:
- name: Segmentstream Plans Pricing
  plan_count: 3
  slug: segmentstream-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Segmentstream Rate Limits
  slug: segmentstream-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 42.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/segmentstream/refs/heads/main/screenshots/segmentstream-2026-08-17T081754.png
security:
- kind: authentication
  name: Segmentstream Authentication
  slug: segmentstream-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Segmentstream Domain Security
  slug: segmentstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Segmentstream Trust Center
  slug: segmentstream-trust-center
  summary_line: SOC 2, GDPR
slug: segmentstream
tags:
- Company
- Marketing Analytics
- Attribution
- Marketing Measurement
- Advertising
- Budget Optimization
- Incrementality
- BigQuery
- MCP
- AI Agents
website: https://segmentstream.com/
---
