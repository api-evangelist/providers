---
access_model:
  confidence: high
  label: Paid with free trial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://sitefire.ai/pricing
  - https://sitefire.ai/docs/quick-start.md
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sitefire Agentic Access
  operation_count: 2
  slug: sitefire-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Book Demo API from Sitefire — 2 operation(s) for book demo.
  name: Sitefire Book Demo API
  slug: sitefire-book-demo-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sitefire Book-a-Demo Book Demo API
  slug: open-sitefire-book-demo-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sitefire-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sitefire-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sitefire-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sitefire-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sitefire-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://sitefire.ai/docs/index.md
- group: start
  title: ''
  type: Quickstart
  url: https://sitefire.ai/docs/quick-start.md
- group: company
  title: ''
  type: Blog
  url: https://sitefire.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://sitefire.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sitefire.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.sitefire.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sitefire.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sitefire.ai/data-privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@sitefire.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sitefire-ai
- group: company
  title: ''
  type: Website
  url: https://sitefire.ai
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sitefire-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sitefire-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sitefire-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sitefire-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sitefire-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sitefire-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sitefire-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sitefire.ai/data-privacy
- group: design
  title: ''
  type: DataModel
  url: data-model/sitefire-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sitefire-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sitefire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sitefire-rate-limits.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/sitefire-robots.txt
created: '2026-07-17'
description: Sitefire is a Generative Engine Optimization (GEO) platform — the marketing suite for the agentic web and a self-described System of Record for AI visibility. It monitors how AI models (ChatGPT, Gemini, Perplexity, DeepSeek, Google AI Mode and AI Overviews) mention and cite a brand across tracked topics, diagnoses why content is or isn't cited using its 4C content classification, and generates actionable briefings plus AI-optimized articles that publish directly to CMS platforms such as Webflow and Framer. Sitefire connects to analytics (GA4, Cloudflare, AWS CloudFront) to measure AI referral and crawler traffic, and exposes its data and content workflows to AI agents through an official hosted MCP server (Spark) and a published Agent Skills bundle. A small public, unauthenticated REST API books product demos. Sitefire is a Y Combinator (W2026) company.
image: https://sitefire.ai/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: Sitefire MCP (Spark)
  slug: sitefire-mcp-spark
modified: '2026-08-13'
name: Sitefire
nav: Providers
network: true
overview: 'Sitefire publishes 1 API on the [APIs.io](https://apis.io/) network: Book Demo API. Tagged areas include Company, Generative Engine Optimization, AI Visibility, Marketing, and SEO.


  Sitefire''s developer surface includes changelog, documentation, quickstart, engineering blog, pricing, signup flow, support, and 23 more developer resources.'
plans:
- name: Sitefire Plans Pricing
  plan_count: 3
  slug: sitefire-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 8
  name: Sitefire Rate Limits
  slug: sitefire-rate-limits
scopes:
- name: Sitefire Scopes
  scope_count: 5
  slug: sitefire-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sitefire/refs/heads/main/screenshots/sitefire-2026-08-17T081906.png
security:
- kind: authentication
  name: Sitefire Authentication
  slug: sitefire-authentication
  summary_line: oauth2/none · 2 schemes
- kind: domain-security
  name: Sitefire Domain Security
  slug: sitefire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sitefire
tags:
- Company
- Generative Engine Optimization
- AI Visibility
- Marketing
- SEO
- Analytics
- Artificial Intelligence
- Content Generation
- MCP
- Agents
website: https://sitefire.ai
---
