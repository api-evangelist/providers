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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 67.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: The Hog Agentic Access
  operation_count: 52
  slug: the-hog-agentic-access
  summary_line: 52 operations · 44 acting
api_count: 8
apis:
- description: The Company Search API from The Hog — 1 operation(s) for company search.
  name: The Hog Company Search API
  slug: the-hog-company-search-api
- description: The Deep Research API from The Hog — 1 operation(s) for deep research.
  name: The Hog Deep Research API
  slug: the-hog-deep-research-api
- description: The Enrichments API from The Hog — 2 operation(s) for enrichments.
  name: The Hog Enrichments API
  slug: the-hog-enrichments-api
- description: The Monitors API from The Hog — 4 operation(s) for monitors.
  name: The Hog Monitors API
  slug: the-hog-monitors-api
- description: The Operations API from The Hog — 2 operation(s) for operations.
  name: The Hog Operations API
  slug: the-hog-operations-api
- description: The People Search API from The Hog — 2 operation(s) for people search.
  name: The Hog People Search API
  slug: the-hog-people-search-api
- description: The Scrapers API from The Hog — 34 operation(s) for scrapers.
  name: The Hog Scrapers API
  slug: the-hog-scrapers-api
- description: The Search API from The Hog — 2 operation(s) for search.
  name: The Hog Search API
  slug: the-hog-search-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.thehog.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thehog.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thehog.ai/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thehog.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://thehog.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://thehog.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.thehog.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thehog.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thehog.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/The-Hog
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-hog-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-hog-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/the-hog-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-hog-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-hog-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-hog-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/the-hog-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-hog-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-hog-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-hog-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-hog-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-hog-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-hog-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-hog-agentic-access.yml
created: '2026-07-17'
description: The Hog is a real-time web intelligence API for AI agents and go-to-market teams, founded in 2025 (Y Combinator F25) by Hudson Liao and Paulo Nascimento in San Francisco. One credit-based REST API unifies company and people search, contact enrichment, LLM-powered deep research, multi-platform web and social scraping (LinkedIn, X, Reddit, Instagram, TikTok, YouTube, Facebook), SEO intelligence, and recurring signal monitors. Fast calls return synchronously; long-running jobs run asynchronously with polling, organization-scoped idempotency keys, cursor pagination, request-id tracing, and a consistent JSON error envelope. A hosted OAuth MCP server and a local stdio MCP package expose the same capabilities to agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-hog.png
layout: provider
mcp_servers:
- description: ''
  name: the-hog-mcp.yml
  slug: the-hog-mcpyml
modified: '2026-07-21'
name: The Hog
nav: Providers
network: true
overview: 'The Hog publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Company Search API, Deep Research API, Enrichments API, and 5 more. Tagged areas include Company, GTM Intelligence, Sales Intelligence, Data Enrichment, and Web Scraping.


  The Hog''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: The Hog Rate Limits
  slug: the-hog-rate-limits
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.6
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 50.5
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: The Hog Authentication
  slug: the-hog-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: The Hog Domain Security
  slug: the-hog-domain-security
  summary_line: TLSv1.3 · DMARC
slug: the-hog
tags:
- Company
- GTM Intelligence
- Sales Intelligence
- Data Enrichment
- Web Scraping
- People Data
- Company Data
- Deep Research
- Social Monitoring
- MCP
- AI Agents
- Y Combinator
website: https://platform.thehog.ai/
---
