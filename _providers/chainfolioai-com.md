---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read‑only crypto portfolio API providing endpoints for balances, transactions and tax calculations.
  name: ChainFolioAI API
  slug: chainfolioai-api
- description: 'ChainFolioAI API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: ChainFolioAI API
  slug: chainfolioai-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/chainfolioai-com/plans/chainfolioai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chainfolioai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chainfolioai-com/rules/chainfolioai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/chainfolioai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/chainfolioai-com/json-ld/chainfolioai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chainfolioai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/chainfolioai-com/vocabulary/chainfolioai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chainfolioai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chainfolioai-com/data-model/chainfolioai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chainfolioai-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/chainfolioai-com/conformance/chainfolioai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chainfolioai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chainfolioai-com/llms/chainfolioai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainfolioai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/chainfolioai-com/mcp/chainfolioai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chainfolioai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/chainfolioai-com/well-known/chainfolioai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chainfolioai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chainfolioai-com/hosts/chainfolioai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chainfolioai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chainfolioai-com/vendors/chainfolioai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chainfolioai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chainfolioai.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainfolioai.com/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://chainfolioai.com/pricing
- group: start
  title: ''
  type: Login
  url: https://chainfolioai.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://chainfolioai.com/guides/crypto-tax
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chainfolioai.com/developers
- group: auth
  href: https://artifacts.apis.io/chainfolioai-com/security/chainfolioai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainfolioai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chainfolioai.com/
coverage:
  checked: '2026-11-03'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI, AsyncAPI, GraphQL or gRPC specifications.
  evidence:
  - status: 200
    url: https://chainfolioai.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ChainFolioAI is a read‑only crypto and traditional portfolio tracker offering real‑time PNL, multi‑country tax tools, an AI assistant, and free tier access. It provides API/MCP endpoints for AI agents to retrieve portfolio data without custodial risk. The platform supports major assets like Bitcoin, Ethereum, Solana, Cardano and integrates with exchanges and wallets.
image: https://chainfolioai.com/opengraph-image
json_schemas:
- name: GetApiV1DefiResponse
  property_count: 7
  slug: chainfolioai-com-get-api-v1-defi-response
- name: GetApiV1FireResponse
  property_count: 6
  slug: chainfolioai-com-get-api-v1-fire-response
- name: GetApiV1GlobalResponse
  property_count: 5
  slug: chainfolioai-com-get-api-v1-global-response
- name: GetApiV1PriceResponse
  property_count: 8
  slug: chainfolioai-com-get-api-v1-price-response
- name: GetApiV1RealizedGainsResponse
  property_count: 8
  slug: chainfolioai-com-get-api-v1-realized-gains-response
- name: GetApiV1TaxEstimateResponse
  property_count: 10
  slug: chainfolioai-com-get-api-v1-tax-estimate-response
jsonld:
- class_count: 24
  name: Chainfolioai Com Context
  property_count: 79
  slug: chainfolioai-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at chainfolioai.com.
  name: ChainFolioAI MCP Server
  slug: chainfolioai-com-mcp-yml
modified: '2026-11-03'
name: ChainFolioAI
nav: Providers
network: true
overview: 'ChainFolioAI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Portfolio, Finance, and Artificial Intelligence.


  The ChainFolioAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ChainFolioAI''s developer surface includes pricing, documentation, and 17 more developer resources.'
plans:
- name: Chainfolioai Com Plans Pricing
  plan_count: 3
  slug: chainfolioai-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: ChainFolioAI API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: chainfolioai-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 9.5
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chainfolioai Com Domain Security
  slug: chainfolioai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chainfolioai-com
tags:
- Company
- Cryptocurrency
- Portfolio
- Finance
- Artificial Intelligence
- Non-Custodial
website: https://chainfolioai.com/
---
