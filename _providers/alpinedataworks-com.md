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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Alpinedataworks Com Agentic Access
  operation_count: 46
  slug: alpinedataworks-com-agentic-access
  summary_line: 46 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.alpinedataworks.com
  baseurl_source: declared
  description: Account snapshot, usage, and credit balance (session or bearer key)
  name: AlpineDataWorks.AI Account API
  slug: alpinedataworks-com-account-api
- baseURL: https://api.alpinedataworks.com
  baseurl_source: declared
  description: Stripe checkout, credit packs, billing portal, and status (session required)
  name: AlpineDataWorks.AI Billing API
  slug: alpinedataworks-com-billing-api
- baseURL: https://api.alpinedataworks.com
  baseurl_source: declared
  description: The Catalog API from AlpineDataWorks.AI — 2 operation(s) for catalog.
  name: AlpineDataWorks.AI Catalog API
  slug: alpinedataworks-com-catalog-api
- baseURL: https://api.alpinedataworks.com
  baseurl_source: declared
  description: Model Context Protocol server for agent access
  name: AlpineDataWorks.AI MCP API
  slug: alpinedataworks-com-mcp-api
- baseURL: https://api.alpinedataworks.com
  baseurl_source: declared
  description: Intelligence object endpoints (Bearer auth required)
  name: AlpineDataWorks.AI Products API
  slug: alpinedataworks-com-products-api
- baseURL: https://api.alpinedataworks.com
  baseurl_source: declared
  description: No authentication required
  name: AlpineDataWorks.AI Public API
  slug: alpinedataworks-com-public-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/alpinedataworks-com/agentic-access/alpinedataworks-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alpinedataworks-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/alpinedataworks-com/plans/alpinedataworks-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alpinedataworks-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alpinedataworks-com/rules/alpinedataworks-com-rules.yml
  title: ''
  type: Spectral
  url: rules/alpinedataworks-com-rules.yml
- group: design
  href: https://artifacts.apis.io/alpinedataworks-com/json-ld/alpinedataworks-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alpinedataworks-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/alpinedataworks-com/vocabulary/alpinedataworks-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alpinedataworks-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/alpinedataworks-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/alpinedataworks-com/data-model/alpinedataworks-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alpinedataworks-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/alpinedataworks-com/errors/alpinedataworks-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alpinedataworks-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alpinedataworks-com/conformance/alpinedataworks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alpinedataworks-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alpinedataworks-com/llms/alpinedataworks-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpinedataworks-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alpinedataworks-com/mcp/alpinedataworks-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alpinedataworks-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/alpinedataworks-com/well-known/alpinedataworks-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alpinedataworks-com-security.txt
- group: agent
  href: https://artifacts.apis.io/alpinedataworks-com/well-known/alpinedataworks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpinedataworks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alpinedataworks-com/hosts/alpinedataworks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpinedataworks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpinedataworks-com/vendors/alpinedataworks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpinedataworks-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://alpinedataworks.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://alpinedataworks.com/playground
- group: start
  title: ''
  type: Login
  url: https://alpinedataworks.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://alpinedataworks.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/alpinedataworks-com/authentication/alpinedataworks-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alpinedataworks-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alpinedataworks-com/security/alpinedataworks-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alpinedataworks-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alpinedataworks-com/security/alpinedataworks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpinedataworks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alpinedataworks.com/
created: '2026-11-01'
description: AlpineDataWorks.AI provides over 300 intelligence objects built from more than 2,000 public data sources, offered via REST and MCP APIs for AI agents. Users can sign up for a free API key, explore the data catalog, view the intelligence dashboard, and access methodology and trust information. The platform covers economy, health, energy, housing and more, with a focus on explainable scores and open data.
image: https://alpinedataworks.com/og.png
json_schemas:
- name: Driver
  property_count: 2
  slug: alpinedataworks-com-driver
- name: HistoryPoint
  property_count: 2
  slug: alpinedataworks-com-history-point
- name: IntelligenceObject
  property_count: 13
  slug: alpinedataworks-com-intelligence-object
- name: ProductSummary
  property_count: 8
  slug: alpinedataworks-com-product-summary
jsonld:
- class_count: 5
  name: Alpinedataworks Com Context
  property_count: 24
  slug: alpinedataworks-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.alpinedataworks.com.
  name: AlpineDataWorks.AI MCP Server
  slug: alpinedataworks-com-mcp-yml
modified: '2026-11-01'
name: AlpineDataWorks.AI
nav: Providers
network: true
overview: 'AlpineDataWorks.AI publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Catalog API, and 3 more. Tagged areas include Data, Artificial Intelligence, Intelligence, Analytics, and Open Data.


  The AlpineDataWorks.AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AlpineDataWorks.AI''s developer surface includes sandbox, API reference, authentication, and 20 more developer resources.'
plans:
- name: Alpinedataworks Com Plans Pricing
  plan_count: 2
  slug: alpinedataworks-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AlpineDataWorks.AI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: alpinedataworks-com-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 27.6
    contract_governance: 35.6
    contract_quality: 59.3
    developer_ergonomics: 20.8
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alpinedataworks Com Authentication
  slug: alpinedataworks-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alpinedataworks Com Domain Security
  slug: alpinedataworks-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alpinedataworks Com Vulnerability Disclosure
  slug: alpinedataworks-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: alpinedataworks-com-billing-upgrade
  slug: alpinedataworks-com-billing-upgrade
- name: alpinedataworks-com-get-product-details
  slug: alpinedataworks-com-get-product-details
- name: alpinedataworks-com-validate-iom
  slug: alpinedataworks-com-validate-iom
slug: alpinedataworks-com
tags:
- Data
- Artificial Intelligence
- Intelligence
- Analytics
- Open Data
website: https://alpinedataworks.com/
---
