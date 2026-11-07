---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Marketplace of micro‑services for AI agents offering pay‑per‑call APIs without API keys.
  name: x402 micro pay API
  slug: x402-micro-pay-api
- description: 'x402-micro-pay-com API as documented publicly: 42 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: x402-micro-pay-com API
  slug: x402-micro-pay-com-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/x402-micro-pay-com/plans/x402-micro-pay-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/x402-micro-pay-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/x402-micro-pay-com/rules/x402-micro-pay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/x402-micro-pay-com-rules.yml
- group: design
  href: https://artifacts.apis.io/x402-micro-pay-com/json-ld/x402-micro-pay-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/x402-micro-pay-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/x402-micro-pay-com/vocabulary/x402-micro-pay-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/x402-micro-pay-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/x402-micro-pay-com/data-model/x402-micro-pay-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/x402-micro-pay-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/x402-micro-pay-com/authentication/x402-micro-pay-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/x402-micro-pay-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/x402-micro-pay-com/conformance/x402-micro-pay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/x402-micro-pay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/x402-micro-pay-com/llms/x402-micro-pay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/x402-micro-pay-com-llms.txt
- group: other
  href: https://artifacts.apis.io/x402-micro-pay-com/a2a/x402-micro-pay-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/x402-micro-pay-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/x402-micro-pay-com/mcp/x402-micro-pay-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/x402-micro-pay-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/x402-micro-pay-com/well-known/x402-micro-pay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/x402-micro-pay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/x402-micro-pay-com/hosts/x402-micro-pay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/x402-micro-pay-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/x402-micro-pay-com/vendors/x402-micro-pay-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/x402-micro-pay-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://grokzilla.shop/quickstart
- group: auth
  href: https://artifacts.apis.io/x402-micro-pay-com/security/x402-micro-pay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/x402-micro-pay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://x402-micro-pay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://x402-micro-pay.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://x402-micro-pay.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://x402-micro-pay.com/terms
created: '2026-10-31'
description: x402 micro pay provides a marketplace of micro‑services for AI agents, offering pay‑per‑call APIs without requiring API keys. Hosted on Base, the platform enables agents to pay with USDC while humans can pay via Stripe. It features tools such as OSINT graph generation, SEO optimization, AI content detection, and blockchain token risk analysis, all priced per call from $0.001 upwards. The service includes tutorials, quickstarts, and a developer portal for easy integration.
json_schemas:
- name: GetApiCatalogResponse
  property_count: 1
  slug: x402-micro-pay-com-get-api-catalog-response
- name: GetWellKnownX402Response
  property_count: 1
  slug: x402-micro-pay-com-get-well-known-x402-response
- name: PostApiSkillsUuidMintRequest
  property_count: 2
  slug: x402-micro-pay-com-post-api-skills-uuid-mint-request
jsonld:
- class_count: 3
  name: X402 Micro Pay Com Context
  property_count: 2
  slug: x402-micro-pay-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at x402-micro-pay.com.
  name: x402-micro-pay-com MCP Server
  slug: x402-micro-pay-com-mcp-yml
modified: '2026-10-31'
name: x402-micro-pay-com
nav: Providers
network: true
overview: 'x402-micro-pay-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Payments, Microservices, and Marketplace.


  The x402-micro-pay-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  x402-micro-pay-com''s developer surface includes authentication, getting-started guide, documentation, pricing, and 15 more developer resources.'
plans:
- name: X402 Micro Pay Com Plans Pricing
  plan_count: 41
  slug: x402-micro-pay-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: x402-micro-pay-com API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: x402-micro-pay-com-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 22.6
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 29.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: X402 Micro Pay Com Authentication
  slug: x402-micro-pay-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: X402 Micro Pay Com Domain Security
  slug: x402-micro-pay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: x402-micro-pay-com
tags:
- Company
- Artificial Intelligence
- Payments
- Microservices
- Marketplace
website: https://x402-micro-pay.com/
---
