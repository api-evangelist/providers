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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The Affiliate API from Classic — 5 operation(s) for affiliate.
  name: Classic Affiliate API
  slug: classic-affiliate-api
- description: The Auth API from Classic — 2 operation(s) for auth.
  name: Classic Auth API
  slug: classic-auth-api
- description: The Supported Assets API from Classic — 3 operation(s) for supported assets.
  name: Classic Supported Assets API
  slug: classic-supported-assets-api
- description: The Supported Chains API from Classic — 2 operation(s) for supported chains.
  name: Classic Supported Chains API
  slug: classic-supported-chains-api
- description: The Swaps API from Classic — 3 operation(s) for swaps.
  name: Classic Swaps API
  slug: classic-swaps-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://og.shapeshift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.shapeshift.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.shapeshift.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.shapeshift.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shapeshift
- group: company
  title: ''
  type: Blog
  url: https://shapeshift.com/blog
- group: operate
  title: ''
  type: Support
  url: https://shapeshift.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shapeshift.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shapeshift.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/classic-shapeshift-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/classic-shapeshift-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/classic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/classic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/classic-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/classic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/classic-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/classic-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/classic-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/classic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/classic-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/classic-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/classic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/classic-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Classic (a.k.a. "OG") is the legacy ShapeShift crypto swap interface at classic.shapeshift.com, now redirecting to og.shapeshift.com. ShapeShift is a self-custody, multichain crypto platform and DEX aggregator. Its Public API (api.shapeshift.com) exposes supported assets and chains (identified with CAIP-19/CAIP-2), indicative swap rates and executable swap quotes, swap-status tracking, and an affiliate/partner program authenticated with Sign-In With Ethereum (EIP-4361, returning a JWT bearer token). Surfaced as a portfolio company of Pantera Capital and enriched into the API Evangelist network.
image: https://github.com/shapeshift.png
layout: provider
mcp_servers:
- description: ''
  name: classic-mcp.yml
  slug: classic-mcpyml
modified: '2026-07-18'
name: Classic
nav: Providers
network: true
overview: 'Classic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Affiliate API, Auth API, Supported Assets API, and 2 more. Tagged areas include Company, Crypto, Cryptocurrency, DEX Aggregator, and Swaps.


  Classic''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 19 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 38.8
  delta: -3.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.7
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/classic/refs/heads/main/screenshots/classic-2026-07-25T205521.png
security:
- kind: authentication
  name: Classic Authentication
  slug: classic-authentication
  summary_line: siwe/http-bearer-jwt · 3 schemes
- kind: domain-security
  name: Classic Domain Security
  slug: classic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: classic
tags:
- Company
- Crypto
- Cryptocurrency
- DEX Aggregator
- Swaps
- Blockchain
- Wallet
- Self-Custody
website: https://og.shapeshift.com/
---
