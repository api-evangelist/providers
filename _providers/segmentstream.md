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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Hosted Model Context Protocol server exposing SegmentStream's marketing measurement, attribution, budget-optimization, and BigQuery query capabilities as agent-callable tools (read-only reporting by d
  name: SegmentStream MCP
  slug: segmentstream-mcp
artifact_total: 5
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
created: '2026-07-17'
description: SegmentStream is a marketing measurement platform that gives AI agents an attribution, budget-optimization, and incrementality-testing "brain." It consolidates first-party and third-party marketing data in Google BigQuery and applies ML-powered, cross-channel attribution across 20+ ad platforms (Google Ads, Meta, TikTok, LinkedIn, Microsoft, Snapchat, Pinterest, Reddit, Criteo, and more), then recommends budget reallocation via marginal-ROAS analysis and validates impact with geo-holdout incrementality experiments. Every capability is exposed as a tool through a hosted Model Context Protocol (MCP) server, so Claude, ChatGPT, Cursor, and any MCP client can query attribution reports, manage configuration, and run BigQuery SQL over a workspace. Backed by Techstars.
image: https://segmentstream.com/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: segmentstream-mcp.yml
  slug: segmentstream-mcpyml
modified: '2026-07-21'
name: SegmentStream
nav: Providers
network: true
overview: 'SegmentStream publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Analytics, Attribution, Marketing Measurement, and Advertising.


  SegmentStream''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 36.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
  summary_line: SOC 2 (aligned with principles, monitored via Drata; not a stated attestation), GDPR, UK GDPR, CCPA, PIPEDA, LGPD, Swiss DPA
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
