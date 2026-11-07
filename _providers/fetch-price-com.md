---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fetch Price Com Agentic Access
  operation_count: 4
  slug: fetch-price-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: 'Agent-to-Agent surface declared by the A2A 1.0.0 agent card at https://fetch-price.com/.well-known/agent-card.json (also served at the legacy agent.json path and on api.fetch-price.com): a JSONRPC bin'
  name: fetch-price A2A Agent
  slug: fetch-price-a2a-agent
- baseURL: https://api.fetch-price.com
  baseurl_source: declared
  description: Agent registration and API key issuance
  name: POLICYANDPLAY LTD Agents API
  slug: fetch-price-com-agents-api
- baseURL: https://api.fetch-price.com
  baseurl_source: declared
  description: Live UK marketplace product and price search
  name: POLICYANDPLAY LTD Products API
  slug: fetch-price-com-products-api
- baseURL: https://api.fetch-price.com
  baseurl_source: declared
  description: Health and public statistics
  name: POLICYANDPLAY LTD Service API
  slug: fetch-price-com-service-api
artifact_total: 22
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.fetch-price.com</code
- group: design
  href: https://artifacts.apis.io/fetch-price-com/rules/fetch-price-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fetch-price-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fetch-price-com/json-ld/fetch-price-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fetch-price-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/fetch-price-com/vocabulary/fetch-price-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fetch-price-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/fetch-price-com/lifecycle/fetch-price-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/fetch-price-com-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/fetch-price-com/hosts/fetch-price-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fetch-price-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/fetch-price-com/integrations/fetch-price-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/fetch-price-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/fetch-price-com/vendors/fetch-price-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fetch-price-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/fetch-price-com/agentic-access/fetch-price-com-agentic-access.yml
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
  href: https://artifacts.apis.io/fetch-price-com/llms/fetch-price-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fetch-price-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://fetch-price.com/llms.txt
- group: other
  href: https://artifacts.apis.io/fetch-price-com/a2a/fetch-price-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fetch-price-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/fetch-price-com/well-known/fetch-price-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fetch-price-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/fetch-price-com/mcp/fetch-price-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fetch-price-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/fetch-price-com/mcp/fetch-price-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fetch-price-com-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/fetch-price-com/packages/fetch-price-com-packages.yml
  title: ''
  type: Packages
  url: packages/fetch-price-com-packages.yml
- group: build
  href: https://artifacts.apis.io/fetch-price-com/packages/fetch-price-com-packages.yml
  title: ''
  type: SDKs
  url: packages/fetch-price-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/fetch-price-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/fetch-price-com/authentication/fetch-price-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fetch-price-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/fetch-price-com/conformance/fetch-price-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fetch-price-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/fetch-price-com/conventions/fetch-price-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fetch-price-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/fetch-price-com/errors/fetch-price-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fetch-price-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fetch-price-com/lifecycle/fetch-price-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fetch-price-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/fetch-price-com/rate-limits/fetch-price-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fetch-price-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fetch-price-com/plans/fetch-price-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fetch-price-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fetch-price-com/data-model/fetch-price-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fetch-price-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fetch-price-com/security/fetch-price-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fetch-price-com-domain-security.yml
- group: other
  href: https://artifacts.apis.io/fetch-price-com/regulatory/fetch-price-com-regulatory-posture.yml
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
finops:
- has_sources: true
  method: derived
  name: Fetch Price Com Finops
  primary_unit: subscription
  service_category: ''
  slug: fetch-price-com-finops
  template: false
json_schemas:
- name: Health
  property_count: 4
  slug: fetch-price-com-health
- name: QueryRequest
  property_count: 6
  slug: fetch-price-com-query-request
- name: QueryResponse
  property_count: 2
  slug: fetch-price-com-query-response
- name: RegisterAgentRequest
  property_count: 5
  slug: fetch-price-com-register-agent-request
- name: RegisterAgentResponse
  property_count: 4
  slug: fetch-price-com-register-agent-response
- name: Stats
  property_count: 3
  slug: fetch-price-com-stats
jsonld:
- class_count: 10
  name: Fetch Price Com Context
  property_count: 32
  slug: fetch-price-com-context
layout: provider
mcp_servers:
- description: 'fetch-price ships ONE official MCP server and it is stdio-only: a single Python file (mcp/fetch_price_mcp.py, FastMCP, MIT) in the public GitHub repo, documented on the API reference page and listed i'
  name: POLICYANDPLAY LTD MCP Server
  slug: fetch-price-com-mcp-yml
modified: '2026-09-19'
name: POLICYANDPLAY LTD
nav: Providers
network: true
overview: 'POLICYANDPLAY LTD publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Products API, Service API, and 1 more. Tagged areas include Company, Price Comparison, Product Search, E-Commerce, and Affiliates.


  The POLICYANDPLAY LTD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  POLICYANDPLAY LTD''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 32 more developer resources.'
plans:
- name: Fetch Price Com Plans Pricing
  plan_count: 4
  slug: fetch-price-com-plans-pricing
- name: Fetch Price Com Price Estimates
  plan_count: 0
  slug: fetch-price-com-price-estimates
random_paper: 22
rate_limits:
- limit_count: 5
  name: Fetch Price Com Rate Limits
  slug: fetch-price-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: POLICYANDPLAY LTD API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: fetch-price-com-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 87.8
    catalog_earned_first_party: 24.0
    catalog_gap: 27.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 56.6
    contract_governance: 35.6
    contract_quality: 28.5
    developer_ergonomics: 45.2
    discoverability: 68.3
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 52.9
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fetch-price-com/fetch-price-com-2026-10-11T104441.png
security:
- kind: authentication
  name: Fetch Price Com Authentication
  slug: fetch-price-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Fetch Price Com Domain Security
  slug: fetch-price-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: fetch-price
  slug: fetch-price-com-fetch-price-skill
- name: fetch-price-register-and-search
  slug: fetch-price-com-register-and-search
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
