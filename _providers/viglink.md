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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Viglink Agentic Access
  operation_count: 16
  slug: viglink-agentic-access
  summary_line: 16 operations · 2 acting
api_count: 8
apis:
- description: The Account API from VigLink (Sovrn Commerce) — 1 operation(s) for account.
  name: VigLink (Sovrn Commerce) Account API
  slug: viglink-account-api
- description: The Ai Orchestration API from VigLink (Sovrn Commerce) — 1 operation(s) for ai orchestration.
  name: VigLink (Sovrn Commerce) Ai Orchestration API
  slug: viglink-ai-orchestration-api
- description: The Bid API from VigLink (Sovrn Commerce) — 1 operation(s) for bid.
  name: VigLink (Sovrn Commerce) Bid API
  slug: viglink-bid-api
- description: The Link API from VigLink (Sovrn Commerce) — 1 operation(s) for link.
  name: VigLink (Sovrn Commerce) Link API
  slug: viglink-link-api
- description: The Merchant Group Summaries API from VigLink (Sovrn Commerce) — 2 operation(s) for merchant group summaries.
  name: VigLink (Sovrn Commerce) Merchant Group Summaries API
  slug: viglink-merchant-group-summaries-api
- description: The Product Coupons API from VigLink (Sovrn Commerce) — 1 operation(s) for product coupons.
  name: VigLink (Sovrn Commerce) Product Coupons API
  slug: viglink-product-coupons-api
- description: The reports API from VigLink (Sovrn Commerce) — 8 operation(s) for reports.
  name: VigLink (Sovrn Commerce) reports API
  slug: viglink-reports-api
- description: The Sites API from VigLink (Sovrn Commerce) — 1 operation(s) for sites.
  name: VigLink (Sovrn Commerce) Sites API
  slug: viglink-sites-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/viglink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sovrn.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viglink-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/viglink-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/viglink-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/viglink-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viglink-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/viglink-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/viglink-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/viglink-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/viglink-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/viglink-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/viglink-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/viglink-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/viglink-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/viglink-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/viglink-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/viglink-merchant-summaries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/viglink-product-promo-codes-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/viglink-price-comparisons-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://sovrn.com/commerce/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sovrn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sovrn.com/docs/authorization
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sovrn.com/reference/link
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sovrn.com/docs/authorization
- group: operate
  title: ''
  type: Support
  url: https://knowledge.sovrn.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sovrn.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viglink
- group: start
  title: ''
  type: SignUp
  url: https://commerce.sovrn.com/
- group: start
  title: ''
  type: Login
  url: https://platform.sovrn.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sovrn.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sovrn.com/privacy-policy/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sovrn.com/
created: '2026-07-17'
description: VigLink pioneered automatic affiliate link monetization for publishers, turning ordinary product links into revenue-generating affiliate links across a network of tens of thousands of merchants. Founded in 2009 and backed by investors including Uncork Capital, VigLink was acquired by Sovrn in early 2018 and now operates as Sovrn Commerce. The product's public APIs still run on VigLink infrastructure (api.viglink.com, rest.viglink.com, viglink.io) and cover link monetization checks, real-time bid checks, campaigns, real-time revenue reporting, merchant summaries, product recommendations, promo codes, and price comparisons, documented on the Sovrn Developer Center alongside a hosted Commerce MCP server for AI agents.
image: https://www.sovrn.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: viglink-mcp.yml
  slug: viglink-mcpyml
modified: '2026-07-21'
name: VigLink (Sovrn Commerce)
nav: Providers
network: true
overview: 'VigLink (Sovrn Commerce) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Ai Orchestration API, Bid API, and 5 more. Tagged areas include Affiliate Marketing, Commerce, Monetization, Publishers, and Links.


  VigLink (Sovrn Commerce)''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
random_paper: 27
rate_limits:
- limit_count: 2
  name: Viglink Rate Limits
  slug: viglink-rate-limits
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 48.8
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Viglink Authentication
  slug: viglink-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Viglink Domain Security
  slug: viglink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Viglink Vulnerability Disclosure
  slug: viglink-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: viglink
tags:
- Affiliate Marketing
- Commerce
- Monetization
- Publishers
- Links
- Advertising
- Reporting
website: https://sovrn.com/commerce/
---
