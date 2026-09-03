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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Scrunch Ai Agentic Access
  operation_count: 39
  slug: scrunch-ai-agentic-access
  summary_line: 39 operations · 18 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The agent-traffic API from Scrunch AI — 1 operation(s) for agent-traffic.
  name: Scrunch AI agent-traffic API
  slug: scrunch-ai-agent-traffic-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The ai-referrals API from Scrunch AI — 3 operation(s) for ai-referrals.
  name: Scrunch AI ai-referrals API
  slug: scrunch-ai-ai-referrals-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The axp-render API from Scrunch AI — 1 operation(s) for axp-render.
  name: Scrunch AI axp-render API
  slug: scrunch-ai-axp-render-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Brands API from Scrunch AI — 6 operation(s) for brands.
  name: Scrunch AI Brands API
  slug: scrunch-ai-brands-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The orchestration API from Scrunch AI — 2 operation(s) for orchestration.
  name: Scrunch AI orchestration API
  slug: scrunch-ai-orchestration-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Page Audits API from Scrunch AI — 2 operation(s) for page audits.
  name: Scrunch AI Page Audits API
  slug: scrunch-ai-page-audits-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Prompts API from Scrunch AI — 2 operation(s) for prompts.
  name: Scrunch AI Prompts API
  slug: scrunch-ai-prompts-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Query API from Scrunch AI — 1 operation(s) for query.
  name: Scrunch AI Query API
  slug: scrunch-ai-query-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Responses API from Scrunch AI — 1 operation(s) for responses.
  name: Scrunch AI Responses API
  slug: scrunch-ai-responses-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The sitemap API from Scrunch AI — 4 operation(s) for sitemap.
  name: Scrunch AI sitemap API
  slug: scrunch-ai-sitemap-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Signals API from Scrunch AI — 6 operation(s) exposing Scrunch's nightly detection sweep as a queryable feed of statistically-tested level changes and trends in AI visibility metrics (presence_rate
  name: Scrunch AI Signals API
  slug: scrunch-ai-signals-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Collections API from Scrunch AI — 1 operation(s) for collections.
  name: Scrunch AI Collections API
  slug: scrunch-ai-collections-api
- baseURL: https://api.scrunchai.com/v1
  baseurl_source: declared
  description: The Scrunch Data API API from Scrunch AI — 1 operation(s) for scrunch data api.
  name: Scrunch AI Scrunch Data API
  slug: scrunch-ai-scrunch-data-api-api
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
artifact_total: 37
asyncapis:
- description: ''
  name: Scrunch Ai Webhooks
  slug: scrunch-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scrunch Data agent-traffic API
  slug: open-scrunch-ai-agent-traffic-api
- collection_type: open
  name: Scrunch Data agent-traffic ai-referrals API
  slug: open-scrunch-ai-ai-referrals-api
- collection_type: open
  name: Scrunch Data agent-traffic axp-render API
  slug: open-scrunch-ai-axp-render-api
- collection_type: open
  name: Scrunch Data agent-traffic Brands API
  slug: open-scrunch-ai-brands-api
- collection_type: open
  name: Scrunch Data agent-traffic orchestration API
  slug: open-scrunch-ai-orchestration-api
- collection_type: open
  name: Scrunch Data agent-traffic Page Audits API
  slug: open-scrunch-ai-page-audits-api
- collection_type: open
  name: Scrunch Data agent-traffic Prompts API
  slug: open-scrunch-ai-prompts-api
- collection_type: open
  name: Scrunch Data agent-traffic Query API
  slug: open-scrunch-ai-query-api
- collection_type: open
  name: Scrunch Data agent-traffic Responses API
  slug: open-scrunch-ai-responses-api
- collection_type: open
  name: Scrunch Data Signals API
  slug: open-scrunch-ai-signals-api
- collection_type: open
  name: Scrunch Data agent-traffic sitemap API
  slug: open-scrunch-ai-sitemap-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/scrunch-ai-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/scrunch-ai-signals-api-overlay.yaml
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/scrunch-ai-tool-crosswalk.yml
- group: build
  title: ''
  type: Examples
  url: examples/scrunch-ai-examples.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scrunch-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scrunch-ai-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/scrunch-ai-components.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scrunch-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.scrunchai.com/
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
description: 'Scrunch AI (scrunch.com) is an AI customer experience platform for AI search visibility and optimization - often called Answer Engine Optimization (AEO/GEO). It monitors and optimizes how a brand shows up across AI assistants and answer engines (ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews, Copilot): tracking brand presence, position, sentiment, citations, and competitor share of voice; measuring AI bot and agent crawl traffic; auditing pages for AI search readiness; and running an Optimize-and-Deploy pipeline that audits, optimizes, and publishes machine-readable page versions through its Agent Experience Platform (AXP). Scrunch exposes a REST Data API (api.scrunchai.com/v1, Bearer API keys with query/configure/create-brand scopes), a hosted MCP server ("Scrunchie") for Claude, ChatGPT, Cursor and other clients, and Looker Studio / Data Studio connectors. The Data API also exposes a Signals surface - a nightly detection sweep of statistically-tested level changes
  and trends, with stable signal fingerprints and team reactions. Backed by Homebrew and Mayfield; acquired by Sitecore in June 2026 and operating as a standalone platform.'
image: https://cdn.sanity.io/images/3lyosn52/production/3846d0bcd45fb4d64491c6d548d181d696aaa339-1200x753.png?rect=0,62,1200,630&w=1200&h=630&q=75&fit=crop&auto=format
layout: provider
mcp_servers:
- description: ''
  name: Scrunch AI MCP Server
  slug: scrunch-ai-mcp-server
modified: '2026-08-13'
name: Scrunch AI
nav: Providers
network: true
overview: 'Scrunch AI publishes 13 APIs on the [APIs.io](https://apis.io/) network, including agent-traffic API, ai-referrals API, axp-render API, and 10 more. Tagged areas include Company, Artificial Intelligence, AI Search, Answer Engine Optimization, and Generative Engine Optimization.


  The Scrunch AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scrunch AI''s developer surface includes documentation, API reference, getting-started guide, authentication, code examples, engineering blog, support, and 32 more developer resources.'
plans:
- name: Scrunch Ai Plans Pricing
  plan_count: 3
  slug: scrunch-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Scrunch Ai Rate Limits
  slug: scrunch-ai-rate-limits
scopes:
- name: Scrunch Ai Scopes
  scope_count: 3
  slug: scrunch-ai-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 26
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 68.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 76.9
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scrunch-ai/refs/heads/main/screenshots/scrunch-ai-2026-08-17T081741.png
security:
- kind: authentication
  name: Scrunch Ai Authentication
  slug: scrunch-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scrunch Ai Domain Security
  slug: scrunch-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scrunch Ai Trust Center
  slug: scrunch-ai-trust-center
  summary_line: SOC 2 Type II
slug: scrunch-ai
tags:
- Company
- Artificial Intelligence
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
