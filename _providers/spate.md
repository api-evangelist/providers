---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://help.spate.nyc/en/article/api-overview
  - https://www.spate.nyc/pricing
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Spate API surface is reached at api.spate.nyc. Its only publicly discoverable contract is a remote Model Context Protocol server at https://api.spate.nyc/mcp, which answers anonymous initialize an
  name: Spate API
  slug: spate-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://spate.nyc
- group: company
  title: ''
  type: About
  url: https://www.spate.nyc/company
- group: company
  title: ''
  type: Blog
  url: https://www.spate.nyc/resources/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.spate.nyc/en
- group: docs
  title: ''
  type: Documentation
  url: https://help.spate.nyc/en/article/api-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spate.nyc/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.spate.nyc/trial
- group: start
  title: ''
  type: Login
  url: https://app.spate.nyc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spate.nyc/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spate.nyc/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SPATENYC
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spate.nyc/
- group: operate
  title: ''
  type: SLA
  url: https://help.spate.nyc/en/article/sla-service-level-agreement
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spate-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spate-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spate-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spate-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/spate-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/spate-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spate-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/spate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spate-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spate-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spate-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spate-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spate-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spate-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Spate is an AI-powered consumer trend forecasting and market intelligence platform for beauty, wellness, and food and beverage brands. It analyzes hundreds of billions of search signals and hundreds of millions of social posts across TikTok, Instagram, Reddit, and Google to predict emerging trends, benchmark competitors, surface whitespace opportunities, and track viral content and sentiment. Used by 200+ brands including Sephora, L''Oreal, P&G, Unilever, and e.l.f. Beauty across marketing, R&D, sales, and retail teams. Spate operates a live remote Model Context Protocol server at https://api.spate.nyc/mcp that exposes four trend-intelligence tools to AI agents, plus a sales-provisioned Brand Data and Trend Data API sold as a subscription add-on. Neither surface has a published OpenAPI, developer portal, SDK, or self-serve API key: Spate states that API integrations are manually configured by its technical team.'
image: https://cdn.prod.website-files.com/687007b9a91ba29ace417424/68f11383d3f1743e47db90d4_OGImage.png
layout: provider
mcp_servers:
- description: ''
  name: spate-mcp.yml
  slug: spate-mcpyml
modified: '2026-08-13'
name: Spate
nav: Providers
network: true
overview: 'Spate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Market Intelligence, Trend Forecasting, and Consumer Insights.


  Spate''s developer surface includes engineering blog, documentation, pricing, signup flow, authentication, and 26 more developer resources.'
plans:
- name: Spate Plans Pricing
  plan_count: 0
  slug: spate-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 0
  name: Spate Rate Limits
  slug: spate-rate-limits
scopes:
- name: Spate Scopes
  scope_count: 0
  slug: spate-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.7
  delta: -3.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 33.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Spate Authentication
  slug: spate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Spate Domain Security
  slug: spate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spate Vulnerability Disclosure
  slug: spate-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Spate Trust Center
  slug: spate-trust-center
  summary_line: SOC 2, GDPR
slug: spate
tags:
- Company
- Enterprise Saas
- Market Intelligence
- Trend Forecasting
- Consumer Insights
- Social Listening
- Analytics
- Beauty
- MCP
- AI Agents
- Trend Data
- Consumer Packaged Goods
website: https://spate.nyc
---
