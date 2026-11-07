---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Globaldatabase Com Agentic Access
  operation_count: 23
  slug: globaldatabase-com-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 3
apis:
- description: 'Token-authenticated REST API over the company-intelligence core: company search and lookup (overview, autocomplete, enrichment by website / LinkedIn / email), company details, financials (by id or tic'
  name: Global Database API (v2)
  slug: global-database-api-v2
- description: Natural-language question endpoint (POST /v2/ai/query) that runs a server-side agent over the same tool set as the MCP server and streams the result as Server-Sent Events — status, tool_call, tool_res
  name: Regis AI Query API
  slug: regis-ai-query-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Autocomplete API from Global Database — 1 operation(s) for autocomplete.
  name: Global Database Autocomplete API
  slug: globaldatabase-com-autocomplete-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Company By Linkedin API from Global Database — 1 operation(s) for company by linkedin.
  name: Global Database Company By Linkedin API
  slug: globaldatabase-com-company-by-linkedin-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Company By Url API from Global Database — 1 operation(s) for company by url.
  name: Global Database Company By Url API
  slug: globaldatabase-com-company-by-url-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Company Details API from Global Database — 1 operation(s) for company details.
  name: Global Database Company Details API
  slug: globaldatabase-com-company-details-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Company Financials API from Global Database — 1 operation(s) for company financials.
  name: Global Database Company Financials API
  slug: globaldatabase-com-company-financials-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Company Ownership API from Global Database — 1 operation(s) for company ownership.
  name: Global Database Company Ownership API
  slug: globaldatabase-com-company-ownership-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The FastAPI API from Global Database — 1 operation(s) for fastapi.
  name: Global Database Fast API
  slug: globaldatabase-com-fastapi-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Health API from Global Database — 1 operation(s) for health.
  name: Global Database Health API
  slug: globaldatabase-com-health-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Nomenclature API from Global Database — 1 operation(s) for nomenclature.
  name: Global Database Nomenclature API
  slug: globaldatabase-com-nomenclature-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Oauth API from Global Database — 7 operation(s) for oauth.
  name: Global Database OAuth API
  slug: globaldatabase-com-oauth-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Playground API from Global Database — 1 operation(s) for playground.
  name: Global Database Playground API
  slug: globaldatabase-com-playground-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Prospecting API from Global Database — 1 operation(s) for prospecting.
  name: Global Database Prospecting API
  slug: globaldatabase-com-prospecting-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The Verify Token API from Global Database — 1 operation(s) for verify token.
  name: Global Database Verify Token API
  slug: globaldatabase-com-verify-token-api
- baseURL: https://api.globaldatabase.com/v2/
  baseurl_source: declared
  description: The .well Known API from Global Database — 1 operation(s) for .well known.
  name: Global Database .well Known API
  slug: globaldatabase-com-well-known-api
artifact_total: 29
asyncapis:
- description: ''
  name: Globaldatabase Com Companies Webhooks
  slug: globaldatabase-com-companies-webhooks
common:
- group: other
  href: https://artifacts.apis.io/globaldatabase-com/capabilities/globaldatabase-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/globaldatabase-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/globaldatabase-com/overlays/globaldatabase-com-mcp-playground-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/globaldatabase-com-mcp-playground-overlay.yaml
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
  href: https://artifacts.apis.io/globaldatabase-com/mcp/globaldatabase-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/globaldatabase-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/globaldatabase-com/mcp/globaldatabase-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/globaldatabase-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/globaldatabase-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/globaldatabase-com/skills/globaldatabase-com-company-due-diligence.md
  title: ''
  type: AgentSkill
  url: skills/globaldatabase-com-company-due-diligence.md
- group: agent
  href: https://artifacts.apis.io/globaldatabase-com/skills/globaldatabase-com-company-snapshot.md
  title: ''
  type: AgentSkill
  url: skills/globaldatabase-com-company-snapshot.md
- group: agent
  href: https://artifacts.apis.io/globaldatabase-com/skills/globaldatabase-com-prospect-list.md
  title: ''
  type: AgentSkill
  url: skills/globaldatabase-com-prospect-list.md
- group: agent
  href: https://artifacts.apis.io/globaldatabase-com/llms/globaldatabase-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/globaldatabase-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.globaldatabase.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/globaldatabase-com/well-known/globaldatabase-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globaldatabase-com-well-known.yml
- group: design
  href: https://artifacts.apis.io/globaldatabase-com/asyncapi/globaldatabase-com-companies-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/globaldatabase-com-companies-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/globaldatabase-com/authentication/globaldatabase-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/globaldatabase-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/globaldatabase-com/scopes/globaldatabase-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/globaldatabase-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/globaldatabase-com/conventions/globaldatabase-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/globaldatabase-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/globaldatabase-com/errors/globaldatabase-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/globaldatabase-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/globaldatabase-com/lifecycle/globaldatabase-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/globaldatabase-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/globaldatabase-com/rate-limits/globaldatabase-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/globaldatabase-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/globaldatabase-com/plans/globaldatabase-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globaldatabase-com-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.globaldatabase.com/pricing-products
- group: build
  href: https://artifacts.apis.io/globaldatabase-com/packages/globaldatabase-com-packages.yml
  title: ''
  type: Packages
  url: packages/globaldatabase-com-packages.yml
- group: design
  href: https://artifacts.apis.io/globaldatabase-com/conformance/globaldatabase-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/globaldatabase-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/globaldatabase-com/conformance/globaldatabase-com-conformance.yml
  title: ''
  type: Compliance
  url: conformance/globaldatabase-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/globaldatabase-com/data-model/globaldatabase-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/globaldatabase-com-data-model.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.globaldatabase.com/data-dictionary
- group: other
  href: https://artifacts.apis.io/globaldatabase-com/regulatory/globaldatabase-com-regulatory-posture.yml
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
  href: https://artifacts.apis.io/globaldatabase-com/agentic-access/globaldatabase-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/globaldatabase-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/globaldatabase-com/security/globaldatabase-com-domain-security.yml
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
finops:
- has_sources: true
  method: derived
  name: Globaldatabase Com Finops
  primary_unit: ''
  service_category: ''
  slug: globaldatabase-com-finops
  template: true
image: https://mcp.globaldatabase.com/static/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.globaldatabase.com over streamable HTTP requiring OAuth; 23 tools listed.
  name: Global Database MCP Server
  slug: global-database
modified: '2026-09-19'
name: Global Database
nav: Providers
network: true
overview: 'Global Database publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Autocomplete API, Company By Linkedin API, Company By Url API, and 13 more. Tagged areas include Company, Company Data, KYB, Compliance, and Business Verification.


  The Global Database catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Global Database''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, engineering blog, signup flow, and 42 more developer resources.'
plans:
- name: Globaldatabase Com Plans Pricing
  plan_count: 0
  slug: globaldatabase-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Globaldatabase Com Rate Limits
  slug: globaldatabase-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Global Database API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 1
  slug: globaldatabase-com-rules
scopes:
- name: Globaldatabase Com Scopes
  scope_count: 0
  slug: globaldatabase-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 30.3
    contract_governance: 31.8
    contract_quality: 45.2
    developer_ergonomics: 41.7
    discoverability: 80.8
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 3.3
      derived: 0
      marker_coverage: 50.0
      total: 30
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/globaldatabase-com/globaldatabase-com-2026-10-11T104933.png
security:
- kind: authentication
  name: Globaldatabase Com Authentication
  slug: globaldatabase-com-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Globaldatabase Com Domain Security
  slug: globaldatabase-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: company-due-diligence
  slug: globaldatabase-com-company-due-diligence
- name: company-snapshot
  slug: globaldatabase-com-company-snapshot
- name: prospect-list
  slug: globaldatabase-com-prospect-list
slug: globaldatabase-com
tags:
- Company
- Company Data
- KYB
- Compliance
- Business Verification
- Beneficial Ownership
- Finance
- Credit Risk
- Data Enrichment
- Prospecting
- Webhook
- MCP
- AI Agents
- United Kingdom
website: https://www.globaldatabase.com/
---
