---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.1
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Globaldatabase Com Agentic Access
  operation_count: 23
  slug: globaldatabase-com-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 1
apis:
- description: 'Token-authenticated REST API over the company-intelligence core: company search and lookup (overview, autocomplete, enrichment by website / LinkedIn / email), company details, financials (by id or tic'
  name: Global Database API (v2)
  slug: global-database-api-v2
- baseURL: https://mcp.globaldatabase.com/mcp
  baseurl_source: declared
  description: Hosted remote Model Context Protocol server (streamable HTTP) exposing 23 read-only tools over company profiles, financials, ownership, digital insights, people search and contact enrichment, prospect
  name: Global Database MCP Server
  slug: global-database-mcp-server
- description: Natural-language question endpoint (POST /v2/ai/query) that runs a server-side agent over the same tool set as the MCP server and streams the result as Server-Sent Events — status, tool_call, tool_res
  name: Regis AI Query API
  slug: regis-ai-query-api
artifact_total: 11
asyncapis:
- description: ''
  name: Globaldatabase Com Companies Webhooks
  slug: globaldatabase-com-companies-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.globaldatabase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.globaldatabase.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://api.globaldatabase.com/docs/v2/
- group: docs
  title: ''
  type: APIReference
  url: https://api.globaldatabase.com/docs/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.globaldatabase.com/docs/v2/#authentication
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/mcp/globaldatabase-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/globaldatabase-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/mcp/globaldatabase-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/globaldatabase-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/skills/globaldatabase-com-company-due-diligence.md
  title: ''
  type: AgentSkill
  url: skills/globaldatabase-com-company-due-diligence.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/skills/globaldatabase-com-company-snapshot.md
  title: ''
  type: AgentSkill
  url: skills/globaldatabase-com-company-snapshot.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/skills/globaldatabase-com-prospect-list.md
  title: ''
  type: AgentSkill
  url: skills/globaldatabase-com-prospect-list.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/llms/globaldatabase-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/globaldatabase-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.globaldatabase.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/well-known/globaldatabase-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globaldatabase-com-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/asyncapi/globaldatabase-com-companies-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/globaldatabase-com-companies-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/authentication/globaldatabase-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/globaldatabase-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/scopes/globaldatabase-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/globaldatabase-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/conventions/globaldatabase-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/globaldatabase-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/errors/globaldatabase-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/globaldatabase-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/lifecycle/globaldatabase-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/globaldatabase-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/rate-limits/globaldatabase-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/globaldatabase-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/plans/globaldatabase-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globaldatabase-com-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.globaldatabase.com/pricing-products
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/packages/globaldatabase-com-packages.yml
  title: ''
  type: Packages
  url: packages/globaldatabase-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/conformance/globaldatabase-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/globaldatabase-com-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/conformance/globaldatabase-com-conformance.yml
  title: ''
  type: Compliance
  url: conformance/globaldatabase-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/data-model/globaldatabase-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/globaldatabase-com-data-model.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.globaldatabase.com/data-dictionary
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/regulatory/globaldatabase-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/globaldatabase-com-regulatory-posture.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://www.globaldatabase.com/processors
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.globaldatabase.com/gdpr
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/agentic-access/globaldatabase-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/globaldatabase-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldatabase-com/refs/heads/main/security/globaldatabase-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globaldatabase-com-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/global-database
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/global-database/n8n-nodes-globaldatabase
- group: company
  title: ''
  type: Blog
  url: https://www.globaldatabase.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.globaldatabase.com/blog/news
- group: other
  title: ''
  type: CaseStudies
  url: https://www.globaldatabase.com/customers
- group: start
  title: ''
  type: SignUp
  url: https://platform.globaldatabase.com/public/signup/free_tier_ai
- group: start
  title: ''
  type: Login
  url: https://platform.globaldatabase.com/
- group: operate
  title: ''
  type: Support
  url: https://www.globaldatabase.com/contact-us
- group: operate
  title: ''
  type: Contact
  url: mailto:support@globaldatabase.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.globaldatabase.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.globaldatabase.com/privacy-notice
- group: company
  title: ''
  type: Careers
  url: https://www.globaldatabase.com/careers
- group: company
  title: ''
  type: Partners
  url: https://www.globaldatabase.com/become-partner
- group: company
  title: ''
  type: About
  url: https://www.globaldatabase.com/about
created: '2026-09-19'
description: Global Database (GLOBAL DATA INTELLIGENCE Ltd, UK) is a B2B company-intelligence provider that sources company records directly from 400+ official government registries across 200+ countries — 600M+ company profiles with registry data, officers and shareholders, UBO and group structure, up to 20 years of filed financials, credit reports, bank-account (Verification of Payee) checks, firmographics, contacts and web-technology insights. It is delivered through a token-authenticated v2 REST API with signed change webhooks, an SSE-streamed natural-language query endpoint (Regis), a hosted OAuth 2.1 MCP server with 23 read-only tools and three provider-published Agent Skills, an n8n node, bulk data feeds and CRM connectors.
image: https://mcp.globaldatabase.com/static/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Global Database MCP Server
  slug: global-database-mcp-server
modified: '2026-09-19'
name: Global Database
nav: Providers
network: true
overview: 'Global Database publishes 1 API on the [APIs.io](https://apis.io/) network: MCP Server. Tagged areas include Company, Company Data, KYB, Compliance, and Business Verification.


  The Global Database catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Global Database''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, engineering blog, signup flow, and 40 more developer resources.'
plans:
- name: Globaldatabase Com Plans Pricing
  plan_count: 1
  slug: globaldatabase-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Globaldatabase Com Rate Limits
  slug: globaldatabase-com-rate-limits
scopes:
- name: Globaldatabase Com Scopes
  scope_count: 0
  slug: globaldatabase-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Globaldatabase Com Authentication
  slug: globaldatabase-com-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Globaldatabase Com Domain Security
  slug: globaldatabase-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: globaldatabase-com
tags:
- Company
- Company Data
- KYB
- Compliance
- Business Verification
- Beneficial Ownership
- Financial
- Credit Risk
- Data Enrichment
- Prospecting
- Webhook
- MCP
- AI Agents
- United Kingdom
website: https://www.globaldatabase.com/
---
