---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Allratestoday Com Agentic Access
  operation_count: 23
  slug: allratestoday-com-agentic-access
  summary_line: 23 operations · 1 acting
api_count: 1
apis:
- baseURL: https://allratestoday.com
  baseurl_source: declared
  description: The Authentication API from allratestoday-com — 1 operation(s) for authentication.
  name: allratestoday-com Authentication API
  slug: allratestoday-com-authentication-api
- baseURL: https://allratestoday.com
  baseurl_source: declared
  description: Official reference rates as published by central banks and tax authorities (API key required)
  name: allratestoday-com Central Bank Rates API
  slug: allratestoday-com-central-bank-rates-api
- baseURL: https://allratestoday.com
  baseurl_source: declared
  description: Drop-in JSON shapes for exchangeratesapi.io, Fixer, exchangerate.host and Frankfurter, served from the ECB reference table.
  name: allratestoday-com Compatibility API
  slug: allratestoday-com-compatibility-api
- baseURL: https://allratestoday.com
  baseurl_source: declared
  description: Live and historical mid-market rates (updated ~every 60 seconds)
  name: allratestoday-com Market Rates API
  slug: allratestoday-com-market-rates-api
- baseURL: https://allratestoday.com
  baseurl_source: declared
  description: Keyless endpoints — no API key needed
  name: allratestoday-com Open Endpoints API
  slug: allratestoday-com-open-endpoints-api
- baseURL: https://allratestoday.com
  baseurl_source: declared
  description: The Reference Rate API from allratestoday-com — 4 operation(s) for reference rate.
  name: allratestoday-com Reference Rate API
  slug: allratestoday-com-reference-rate-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/allratestoday-com/a2a/allratestoday-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/allratestoday-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/allratestoday-com/agentic-access/allratestoday-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/allratestoday-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/allratestoday-com/plans/allratestoday-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allratestoday-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/allratestoday-com/rules/allratestoday-com-rules.yml
  title: ''
  type: Spectral
  url: rules/allratestoday-com-rules.yml
- group: design
  href: https://artifacts.apis.io/allratestoday-com/json-ld/allratestoday-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allratestoday-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/allratestoday-com/vocabulary/allratestoday-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allratestoday-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/allratestoday-com/data-model/allratestoday-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allratestoday-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/allratestoday-com/authentication/allratestoday-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allratestoday-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://allratestoday.com/status
- group: design
  href: https://artifacts.apis.io/allratestoday-com/lifecycle/allratestoday-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/allratestoday-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/allratestoday-com/errors/allratestoday-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allratestoday-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/allratestoday-com/conformance/allratestoday-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allratestoday-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allratestoday-com/llms/allratestoday-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allratestoday-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/allratestoday-com/mcp/allratestoday-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/allratestoday-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/allratestoday-com/well-known/allratestoday-com-publicapis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allratestoday-com-publicapis-security.txt
- group: auth
  href: https://artifacts.apis.io/allratestoday-com/well-known/allratestoday-com-clawhub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allratestoday-com-clawhub-security.txt
- group: agent
  href: https://artifacts.apis.io/allratestoday-com/well-known/allratestoday-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allratestoday-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/allratestoday-com/hosts/allratestoday-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allratestoday-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allratestoday-com/vendors/allratestoday-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allratestoday-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/allratestoday-com/packages/allratestoday-com-packages.yml
  title: ''
  type: SDKs
  url: packages/allratestoday-com-packages.yml
- group: build
  href: https://artifacts.apis.io/allratestoday-com/packages/allratestoday-com-packages.yml
  title: ''
  type: Packages
  url: packages/allratestoday-com-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://allratestoday.com/docs/mcp-server/
- group: auth
  href: https://artifacts.apis.io/allratestoday-com/security/allratestoday-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allratestoday-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allratestoday.com/
- group: docs
  title: ''
  type: Documentation
  url: https://allratestoday.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://allratestoday.com/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://allratestoday.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://allratestoday.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://allratestoday.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allratestoday.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allratestoday.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://allratestoday.com/register
- group: start
  title: ''
  type: Login
  url: https://allratestoday.com/login
- group: start
  title: ''
  type: Sandbox
  url: https://allratestoday.com/playground
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AllRates-Today
created: '2026-10-29'
description: AllRates Today provides comprehensive exchange rate data and financial APIs, offering real-time, historical, and central bank rates across multiple currencies. The platform supplies developers with reliable endpoints for currency conversion, rate lookup, and financial analytics, supporting various SDKs and integration guides. It emphasizes accuracy, extensive coverage, and easy-to-use documentation for fintech applications and services.
image: https://allratestoday.com/og-image.png
json_schemas:
- name: CbPairDated
  property_count: 12
  slug: allratestoday-com-cb-pair-dated
- name: CbPair
  property_count: 10
  slug: allratestoday-com-cb-pair
- name: CbRate
  property_count: 4
  slug: allratestoday-com-cb-rate
- name: CbTableDated
  property_count: 7
  slug: allratestoday-com-cb-table-dated
- name: CbTable
  property_count: 5
  slug: allratestoday-com-cb-table
jsonld:
- class_count: 4
  name: Allratestoday Com Context
  property_count: 17
  slug: allratestoday-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at allratestoday.com.
  name: allratestoday-com MCP Server
  slug: allratestoday-com-mcp-yml
modified: '2026-10-29'
name: allratestoday-com
nav: Providers
network: true
overview: 'allratestoday-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Central Bank Rates API, Compatibility API, and 3 more. Tagged areas include Company, Fintech, Exchange Rates, and Data.


  The allratestoday-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  allratestoday-com''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Allratestoday Com Plans Pricing
  plan_count: 5
  slug: allratestoday-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: allratestoday-com API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 3
    warn: 4
  slug: allratestoday-com-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 42.9
    discoverability: 58.3
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/allratestoday-com/allratestoday-com-2026-11-03T120650.png
security:
- kind: authentication
  name: Allratestoday Com Authentication
  slug: allratestoday-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Allratestoday Com Domain Security
  slug: allratestoday-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allratestoday-com
tags:
- Company
- Fintech
- Exchange Rates
- Data
website: https://allratestoday.com/
---
