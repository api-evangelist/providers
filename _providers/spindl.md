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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Server-side custom event ingestion for attribution.
  name: Spindl Events API
  slug: spindl-events-api
- description: Redirect links mapping a Spindl link to a destination URL.
  name: Spindl Short Links API
  slug: spindl-short-links-api
- description: Publisher-facing onchain advertising API. Fetch targeted ad recommendations for a wallet address at a named placement, render the returned unit, and post impressions and clicks back to Spindl. Also se
  name: Spindl Ads API
  slug: spindl-ads-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spindl Server-to-Server Events API
  slug: open-spindl-events-api
- collection_type: open
  name: Spindl Server-to-Server Events Short Links API
  slug: open-spindl-short-links-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/spindl-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spindl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spindl-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/spindl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spindl-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spindl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spindl-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/spindl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spindl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spindl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spindl-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spindl-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/spindl-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spindl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spindl-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://spindl.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spindl.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spindl.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spindl.xyz/technical/start-here
- group: company
  title: ''
  type: Blog
  url: https://blog.spindl.xyz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spindl-xyz
- group: start
  title: ''
  type: SignUp
  url: https://app.spindl.xyz
- group: operate
  title: ''
  type: Support
  url: https://docs.spindl.xyz/contact-spindl
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spindl.xyz/privacy-policy
created: '2026-07-17'
description: Spindl is a Web3 growth platform providing onchain attribution, web3-native analytics, audiences, short links, referrals, and ads in one place, helping developers understand where their users come from and how they behave across onchain apps. It offers a JavaScript/HTML SDK, Android and iOS SDKs, and a Server-to-Server REST API for campaign and attribution management, short (redirect) links, server-side custom event ingestion, and daily data exports. Positioned as Web3's answer to Mixpanel and Amplitude, Spindl is used by teams including Uniswap, Base, Safe, and Morpho. A separate publisher-facing Ads API on e.spindlembed.com serves targeted onchain ad recommendations and records impressions and clicks, with a React BannerEmbed component and a hosted iframe as no-code alternatives. Spindl announced in January 2025 that it was joining Coinbase and now operates as a product team inside Base. Originally added to the API Evangelist network as a portfolio-lead stub, now enriched
  from its published developer documentation and live host probes.
image: https://spindl.xyz/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Spindl MCP Server
  slug: spindl-mcp-server
modified: '2026-08-13'
name: Spindl
nav: Providers
network: true
overview: 'Spindl publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, Short Links API, and Ads API. Tagged areas include Company, Crypto Web3, Attribution, Analytics, and Marketing.


  Spindl''s developer surface includes authentication, documentation, getting-started guide, engineering blog, signup flow, support, and 19 more developer resources.'
plans:
- name: Spindl Plans Pricing
  plan_count: 0
  slug: spindl-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Spindl Rate Limits
  slug: spindl-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 56.5
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.5
  provenance:
    conformance: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spindl/refs/heads/main/screenshots/spindl-2026-08-17T082027.png
security:
- kind: authentication
  name: Spindl Authentication
  slug: spindl-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Spindl Domain Security
  slug: spindl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spindl
tags:
- Company
- Crypto Web3
- Attribution
- Analytics
- Marketing
- Growth
- SDK
- Web3
website: https://spindl.xyz
---
