---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fetch Price Com Agentic Access
  operation_count: 4
  slug: fetch-price-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- baseURL: https://api.fetch-price.com
  baseurl_source: declared
  description: REST API at https://api.fetch-price.com. POST /api/query searches live UK marketplace listings by plain-language query (max_results 1-20, max_price in GBP, networks ebay_uk / amazon_uk) and returns no
  name: fetch-price API
  slug: fetch-price-api
- description: 'Agent-to-Agent surface declared by the A2A 1.0.0 agent card at https://fetch-price.com/.well-known/agent-card.json (also served at the legacy agent.json path and on api.fetch-price.com): a JSONRPC bin'
  name: fetch-price A2A Agent
  slug: fetch-price-a2a-agent
artifact_total: 8
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/agentic-access/fetch-price-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fetch-price-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://fetch-price.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fetch-price.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://fetch-price.com/docs/#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://fetch-price.com/docs/#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://fetch-price.com/docs/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://fetch-price.com/docs/#get-key
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fetch-price.com/privacy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/fusionx212/fetch-price
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/llms/fetch-price-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fetch-price-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://fetch-price.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/a2a/fetch-price-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fetch-price-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/well-known/fetch-price-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fetch-price-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/mcp/fetch-price-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fetch-price-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/mcp/fetch-price-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fetch-price-com-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/packages/fetch-price-com-packages.yml
  title: ''
  type: Packages
  url: packages/fetch-price-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/packages/fetch-price-com-packages.yml
  title: ''
  type: SDKs
  url: packages/fetch-price-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/authentication/fetch-price-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fetch-price-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/conformance/fetch-price-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fetch-price-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/conventions/fetch-price-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fetch-price-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/errors/fetch-price-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fetch-price-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/lifecycle/fetch-price-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fetch-price-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/rate-limits/fetch-price-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fetch-price-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/plans/fetch-price-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fetch-price-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/data-model/fetch-price-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fetch-price-com-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/security/fetch-price-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fetch-price-com-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fetch-price-com/refs/heads/main/regulatory/fetch-price-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/fetch-price-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://fetch-price.com/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://fetch-price.com/privacy
created: '2026-09-19'
description: 'POLICYANDPLAY LTD (England & Wales, company no. 17253846) operates fetch-price, a UK product and price search API built for AI agents: one POST to api.fetch-price.com returns live eBay UK listings (via the official Browse API; Amazon UK rolling out) as normalised JSON with GBP prices, condition and an affiliate-tracked purchase URL. The free tier needs no API key (50 lookups/month, 30 requests/minute); Pro (GBP 29) and Scale/Trade (GBP 99) plans raise quotas and let customers route affiliate commission to their own eBay Partner Network account. The same API is exposed as a conformant A2A 1.0.0 agent card with a live JSON-RPC message/send binding, a stdio MCP server listed in the official MCP registry, a provider-authored SKILL.md, llms.txt, and npm/PyPI SDKs. No OpenAPI is published; the profile''s spec was generated by API Evangelist from the provider''s own reference and checked against the live host.'
layout: provider
mcp_servers:
- description: ''
  name: POLICYANDPLAY LTD MCP Server
  slug: policyandplay-ltd-mcp-server
modified: '2026-09-19'
name: POLICYANDPLAY LTD
nav: Providers
network: true
overview: 'POLICYANDPLAY LTD publishes 2 APIs on the [APIs.io](https://apis.io/) network, including fetch-price API, and 1 more. Tagged areas include Company, Price Comparison, Product Search, E-Commerce, and Affiliates.


  POLICYANDPLAY LTD''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Fetch Price Com Plans Pricing
  plan_count: 4
  slug: fetch-price-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Fetch Price Com Rate Limits
  slug: fetch-price-com-rate-limits
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 15.5
    developer_ergonomics: 54.8
    discoverability: 68.3
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 40.1
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Fetch Price Com Authentication
  slug: fetch-price-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Fetch Price Com Domain Security
  slug: fetch-price-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fetch-price-com
tags:
- Company
- Price Comparison
- Product Search
- E-Commerce
- Affiliates
- Marketplace
- Shopping
- eBay
- United Kingdom
- AI Agents
- A2A
- MCP
website: https://fetch-price.com/
---
