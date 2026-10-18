---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Akta Pro Agentic Access
  operation_count: 14
  slug: akta-pro-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 2
apis:
- description: 'Remote Streamable-HTTP MCP server (https://mcp.akta.pro/mcp) that exposes the akta.pro company-intelligence stack to Claude, ChatGPT, Cursor, VS Code, Claude Code and other MCP clients: company and in'
  name: akta.pro MCP Server
  slug: akta-pro-mcp-server
- baseURL: https://api.akta.pro/api
  baseurl_source: declared
  description: Company data enrichment, search, and addition
  name: akta.pro Company API
  slug: akta-pro-company-api
- baseURL: https://api.akta.pro/api
  baseurl_source: declared
  description: Build targeted company lists using structured filters or natural language queries
  name: akta.pro List Generation API
  slug: akta-pro-list-generation-api
- baseURL: https://api.akta.pro/api
  baseurl_source: declared
  description: Enriched news articles with AI summaries, sentiment, and company mentions
  name: akta.pro News API
  slug: akta-pro-news-api
- baseURL: https://api.akta.pro/api
  baseurl_source: declared
  description: Product and employee reviews from external sources
  name: akta.pro Reviews API
  slug: akta-pro-reviews-api
- baseURL: https://api.akta.pro/api
  baseurl_source: declared
  description: Utility endpoints for request tracking
  name: akta.pro Supporting APIs API
  slug: akta-pro-supporting-apis-api
artifact_total: 21
asyncapis:
- description: ''
  name: Akta Pro Webhooks
  slug: akta-pro-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/agentic-access/akta-pro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/akta-pro-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/rate-limits/akta-pro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/akta-pro-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/plans/akta-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/akta-pro-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/rules/akta-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/akta-pro-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/json-ld/akta-pro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/akta-pro-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/vocabulary/akta-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/akta-pro-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/asyncapi/akta-pro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/akta-pro-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/data-model/akta-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/akta-pro-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/cli/akta-pro-cli.yml
  title: ''
  type: CLI
  url: cli/akta-pro-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/changelog/akta-pro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/akta-pro-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/conventions/akta-pro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/akta-pro-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/lifecycle/akta-pro-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/akta-pro-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/lifecycle/akta-pro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/akta-pro-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/errors/akta-pro-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/akta-pro-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/errors/akta-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/akta-pro-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/conformance/akta-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/akta-pro-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/overlays/akta-pro-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/akta-pro-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/llms/akta-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akta-pro-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/a2a/akta-pro-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/akta-pro-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/mcp/akta-pro-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/akta-pro-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/mcp/akta-pro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/akta-pro-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/well-known/akta-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/akta-pro-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/hosts/akta-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akta-pro-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/vendors/akta-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akta-pro-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/packages/akta-pro-packages.yml
  title: ''
  type: SDKs
  url: packages/akta-pro-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/packages/akta-pro-packages.yml
  title: ''
  type: Packages
  url: packages/akta-pro-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/authentication/akta-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/akta-pro-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://akta.pro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://playground.akta.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akta.pro/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.akta.pro/api-reference/news-signals
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akta.pro/getting-started/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.akta.pro/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://akta.pro/pricing
- group: company
  title: ''
  type: Blog
  url: https://akta.pro/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.akta.pro/contact
- group: start
  title: ''
  type: SignUp
  url: https://playground.akta.pro/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akta-pro
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akta.pro/legal?tab=terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akta.pro/legal?tab=privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akta-pro
- group: company
  title: ''
  type: Twitter
  url: https://x.com/akta_pro
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/security/akta-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akta-pro-domain-security.yml
created: '2026-10-07'
description: akta.pro (marketed as "akta.pro by Wokelo AI", a product of Wokelo Inc.) is a private-company data, news and signals API built for AI agents, developers and enterprise teams. It covers 20M+ companies with 75+ data points each (firmographics, business model, financial estimates, management, technology, funding and M&A), entity-resolved and de-duplicated news classified against an 80+ event taxonomy plus NAICS, SIC, IPTC and IAB codes, list generation from structured filters or natural language, and alternative signals (headcount trends, website traffic, job posts, social posts, employee and product reviews). Access is credit-based and pay-as-you-go through a REST API (api.akta.pro), a remote MCP server (mcp.akta.pro) and the akta-pro-cli on PyPI.
image: https://akta.pro/opengraph-image?af85e82039d972ad
json_schemas:
- name: CompanyAdditionResponse
  property_count: 6
  slug: akta-pro-company-addition-response
- name: EmployeeReview
  property_count: 2
  slug: akta-pro-employee-review
- name: ListGenerationRequest
  property_count: 7
  slug: akta-pro-list-generation-request
- name: NewsArticle
  property_count: 14
  slug: akta-pro-news-article
- name: ProductReview
  property_count: 11
  slug: akta-pro-product-review
- name: StatusResponse
  property_count: 6
  slug: akta-pro-status-response
jsonld:
- class_count: 20
  name: Akta Pro Context
  property_count: 91
  slug: akta-pro-context
layout: provider
mcp_servers:
- description: 'Official remote MCP server for the akta.pro company-intelligence stack. The docs say: "akta.pro MCP server can be installed in any MCP client with the server URL https://mcp.akta.pro/mcp". Listed in t'
  name: akta.pro MCP
  slug: akta-pro-mcp
modified: '2026-10-07'
name: akta.pro
nav: Providers
network: true
overview: 'akta.pro publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Company API, List Generation API, News API, and 3 more. Tagged areas include Company, Company Data, Company Intelligence, News, and Alternative Data.


  The akta.pro catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  akta.pro''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 37 more developer resources.'
plans:
- name: Akta Pro Plans Pricing
  plan_count: 3
  slug: akta-pro-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 120
  name: Akta Pro Rate Limits
  slug: akta-pro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: akta.pro API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 4
    warn: 1
  slug: akta-pro-rules
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 72.9
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 68.4
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/akta-pro/refs/heads/main/screenshots/akta-pro-2026-10-11T093532.png
security:
- kind: authentication
  name: Akta Pro Authentication
  slug: akta-pro-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Akta Pro Domain Security
  slug: akta-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akta-pro
tags:
- Company
- Company Data
- Company Intelligence
- News
- Alternative Data
- Private Companies
- Firmographics
- Data Enrichment
- Signals
- MCP
- Market Intelligence
website: https://akta.pro
---
