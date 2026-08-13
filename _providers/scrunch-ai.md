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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Scrunch Ai Agentic Access
  operation_count: 33
  slug: scrunch-ai-agentic-access
  summary_line: 33 operations · 16 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The agent-traffic API from Scrunch AI — 1 operation(s) for agent-traffic.
  name: Scrunch AI agent-traffic API
  slug: scrunch-ai-agent-traffic-api
- description: The ai-referrals API from Scrunch AI — 3 operation(s) for ai-referrals.
  name: Scrunch AI ai-referrals API
  slug: scrunch-ai-ai-referrals-api
- description: The axp-render API from Scrunch AI — 1 operation(s) for axp-render.
  name: Scrunch AI axp-render API
  slug: scrunch-ai-axp-render-api
- description: The Brands API from Scrunch AI — 6 operation(s) for brands.
  name: Scrunch AI Brands API
  slug: scrunch-ai-brands-api
- description: The orchestration API from Scrunch AI — 2 operation(s) for orchestration.
  name: Scrunch AI orchestration API
  slug: scrunch-ai-orchestration-api
- description: The Page Audits API from Scrunch AI — 2 operation(s) for page audits.
  name: Scrunch AI Page Audits API
  slug: scrunch-ai-page-audits-api
- description: The Prompts API from Scrunch AI — 2 operation(s) for prompts.
  name: Scrunch AI Prompts API
  slug: scrunch-ai-prompts-api
- description: The Query API from Scrunch AI — 1 operation(s) for query.
  name: Scrunch AI Query API
  slug: scrunch-ai-query-api
- description: The Responses API from Scrunch AI — 1 operation(s) for responses.
  name: Scrunch AI Responses API
  slug: scrunch-ai-responses-api
- description: The sitemap API from Scrunch AI — 4 operation(s) for sitemap.
  name: Scrunch AI sitemap API
  slug: scrunch-ai-sitemap-api
arazzos:
- description: Create a brand, add a competitor and persona, seed a tracking prompt, and verify the prompt library.
  name: Scrunch - Onboard a brand and seed tracking
  slug: scrunch-ai-onboard-and-track
- description: Submit pages to the Optimize-and-Deploy pipeline and poll for completion.
  name: Scrunch - Optimize and deploy pages, then poll
  slug: scrunch-ai-optimize-and-deploy
- description: List brands, pick one, and pull aggregated AI visibility metrics for it.
  name: Scrunch - Resolve a brand and query AI visibility
  slug: scrunch-ai-query-visibility
artifact_total: 19
asyncapis:
- description: ''
  name: Scrunch Ai Webhooks
  slug: scrunch-ai-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/scrunch-ai-data-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://scrunch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.scrunch.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.scrunch.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.scrunch.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.scrunch.com/getting-started/quickstart-query
- group: auth
  title: ''
  type: Authentication
  url: authentication/scrunch-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scrunch-ai-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scrunch-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scrunch-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scrunch-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scrunch-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scrunch-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scrunchai.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scrunch-ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scrunch-ai-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/scrunch-ai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/scrunch-ai-onboard-and-track.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/scrunch-ai-query-visibility.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/scrunch-ai-optimize-and-deploy.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scrunch-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrunch-ai-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scrunch-ai-well-known.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scrunch-ai
- group: company
  title: ''
  type: Blog
  url: https://scrunch.com/blog
- group: operate
  title: ''
  type: Support
  url: https://scrunch.com/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://scrunch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.scrunchai.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.scrunchai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrunch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrunch.com/privacy
created: '2026-07-17'
description: 'Scrunch AI (scrunch.com) is an AI customer experience platform for AI search visibility and optimization - often called Answer Engine Optimization (AEO/GEO). It monitors and optimizes how a brand shows up across AI assistants and answer engines (ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews, Copilot): tracking brand presence, position, sentiment, citations, and competitor share of voice; measuring AI bot and agent crawl traffic; auditing pages for AI search readiness; and running an Optimize-and-Deploy pipeline that audits, optimizes, and publishes machine-readable page versions through its Agent Experience Platform (AXP). Scrunch exposes a REST Data API (api.scrunchai.com/v1, Bearer API keys with query/configure/create-brand scopes), a hosted MCP server ("Scrunchie") for Claude, ChatGPT, Cursor and other clients, and Looker Studio / Data Studio connectors. Backed by Homebrew and Mayfield.'
image: https://cdn.sanity.io/images/3lyosn52/production/3846d0bcd45fb4d64491c6d548d181d696aaa339-1200x753.png?rect=0,62,1200,630&w=1200&h=630&q=75&fit=crop&auto=format
layout: provider
mcp_servers:
- description: ''
  name: scrunch-ai-mcp.yml
  slug: scrunch-ai-mcpyml
modified: '2026-07-21'
name: Scrunch AI
nav: Providers
network: true
overview: 'Scrunch AI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including agent-traffic API, ai-referrals API, axp-render API, and 7 more. Tagged areas include Company, AI, AI Search, Answer Engine Optimization, and Generative Engine Optimization.


  The Scrunch AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scrunch AI''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 25 more developer resources.'
random_paper: 45
scopes:
- name: Scrunch Ai Scopes
  scope_count: 3
  slug: scrunch-ai-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 53.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 68.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Scrunch Ai Authentication
  slug: scrunch-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scrunch Ai Domain Security
  slug: scrunch-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scrunch-ai
tags:
- Company
- AI
- AI Search
- Answer Engine Optimization
- Generative Engine Optimization
- Brand Visibility
- Analytics
- SEO
- Agent Experience
- MCP
website: https://scrunch.com
---
