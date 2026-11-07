---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Soldfetch Com Agentic Access
  operation_count: 13
  slug: soldfetch-com-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Bulk Search API from soldfetch-com — 1 operation(s) for bulk search.
  name: soldfetch-com Bulk Search API
  slug: soldfetch-com-bulk-search-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Capabilities API from soldfetch-com — 1 operation(s) for capabilities.
  name: soldfetch-com Capabilities API
  slug: soldfetch-com-capabilities-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Item API from soldfetch-com — 1 operation(s) for item.
  name: soldfetch-com Item API
  slug: soldfetch-com-item-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Public API from soldfetch-com — 1 operation(s) for public.
  name: soldfetch-com Public API
  slug: soldfetch-com-public-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Rapidapi API from soldfetch-com — 1 operation(s) for rapidapi.
  name: soldfetch-com Rapidapi API
  slug: soldfetch-com-rapidapi-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Requests API from soldfetch-com — 1 operation(s) for requests.
  name: soldfetch-com Requests API
  slug: soldfetch-com-requests-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Scrape API from soldfetch-com — 6 operation(s) for scrape.
  name: soldfetch-com Scrape API
  slug: soldfetch-com-scrape-api
- baseURL: https://soldfetch.com
  baseurl_source: declared
  description: The Usage API from soldfetch-com — 1 operation(s) for usage.
  name: soldfetch-com Usage API
  slug: soldfetch-com-usage-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/soldfetch-com/agentic-access/soldfetch-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/soldfetch-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/soldfetch-com/rate-limits/soldfetch-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/soldfetch-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/soldfetch-com/plans/soldfetch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/soldfetch-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/soldfetch-com/rules/soldfetch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/soldfetch-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/soldfetch-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/soldfetch-com/conventions/soldfetch-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/soldfetch-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/soldfetch-com/authentication/soldfetch-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/soldfetch-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/soldfetch-com/errors/soldfetch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/soldfetch-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/soldfetch-com/conformance/soldfetch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/soldfetch-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/soldfetch-com/llms/soldfetch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soldfetch-com-llms.txt
- group: other
  href: https://artifacts.apis.io/soldfetch-com/a2a/soldfetch-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/soldfetch-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/soldfetch-com/mcp/soldfetch-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/soldfetch-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/soldfetch-com/mcp/soldfetch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/soldfetch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/soldfetch-com/well-known/soldfetch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/soldfetch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/soldfetch-com/hosts/soldfetch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soldfetch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/soldfetch-com/vendors/soldfetch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soldfetch-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://soldfetch.com/status
- group: start
  title: ''
  type: GettingStarted
  url: https://soldfetch.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/soldfetch-com/security/soldfetch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soldfetch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soldfetch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://soldfetch.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://soldfetch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://soldfetch.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soldfetch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soldfetch.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://soldfetch.com/contact
created: '2026-10-31'
description: SoldFetch offers an eBay Sold Listings & Pricing API that returns up to 200 sold listings per request, including displayed prices, item details, and seller information. Designed for resellers, developers, and enterprises, the service provides free and paid plans, comprehensive documentation, pricing details, and contact support. It enables integration of eBay historical sales data into applications and AI agents.
image: https://soldfetch.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at soldfetch.com.
  name: soldfetch-com MCP Server
  slug: soldfetch-com-mcp-yml
modified: '2026-10-31'
name: soldfetch-com
nav: Providers
network: true
overview: 'soldfetch-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk Search API, Capabilities API, Item API, and 5 more. Tagged areas include Company, eBay, Listings, Pricing, and Reseller.


  The soldfetch-com catalog on APIs.io includes 1 Spectral governance ruleset.


  soldfetch-com''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, support, and 20 more developer resources.'
plans:
- name: Soldfetch Com Plans Pricing
  plan_count: 4
  slug: soldfetch-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Soldfetch Com Rate Limits
  slug: soldfetch-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: soldfetch-com API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 1
  slug: soldfetch-com-rules
scopes:
- name: Soldfetch Com Scopes
  scope_count: 0
  slug: soldfetch-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 46.4
    developer_ergonomics: 28.0
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 50.4
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/soldfetch-com/soldfetch-com-2026-11-03T143513.png
security:
- kind: authentication
  name: Soldfetch Com Authentication
  slug: soldfetch-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Soldfetch Com Domain Security
  slug: soldfetch-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: soldfetch
  slug: soldfetch-com-soldfetch
slug: soldfetch-com
tags:
- Company
- eBay
- Listings
- Pricing
- Reseller
website: https://soldfetch.com/
---
