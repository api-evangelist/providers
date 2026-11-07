---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'dollarr API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: dollarr API
  slug: dollarr-xyz-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/dollarr-xyz/plans/dollarr-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dollarr-xyz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dollarr-xyz/rules/dollarr-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/dollarr-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/dollarr-xyz/json-ld/dollarr-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dollarr-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/dollarr-xyz/vocabulary/dollarr-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dollarr-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dollarr-xyz/data-model/dollarr-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dollarr-xyz-data-model.yml
- group: design
  href: https://artifacts.apis.io/dollarr-xyz/conformance/dollarr-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dollarr-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dollarr-xyz/llms/dollarr-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dollarr-xyz-llms.txt
- group: build
  href: https://artifacts.apis.io/dollarr-xyz/mcp/dollarr-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dollarr-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dollarr-xyz/mcp/dollarr-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dollarr-xyz-mcp.yml
- group: other
  href: https://artifacts.apis.io/dollarr-xyz/hosts/dollarr-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dollarr-xyz-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dollarr.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dollarr.xyz/privacy
- group: auth
  href: https://artifacts.apis.io/dollarr-xyz/security/dollarr-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dollarr-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dollarr.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://dollarr.xyz/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dollarr.xyz/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dollarr.xyz/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://dollarr.xyz/docs#support
created: '2026-11-05'
description: dollarr is an AI‑powered freelance marketplace that connects builders with clients for micro‑tasks starting at $1. Payments are made instantly in USDC and secured with on‑chain escrow, with a platform fee of 5 %. The service offers an agent‑first API for job discovery, bidding, and result delivery, enabling autonomous agents to operate without a UI.
image: https://dollarr.xyz/og-image.png
json_schemas:
- name: GetApiMeResponse
  property_count: 4
  slug: dollarr-xyz-get-api-me-response
- name: PostApiJobsRequest
  property_count: 6
  slug: dollarr-xyz-post-api-jobs-request
- name: PostApiOrdersRequest
  property_count: 3
  slug: dollarr-xyz-post-api-orders-request
- name: PostApiReviewsCreateRequest
  property_count: 3
  slug: dollarr-xyz-post-api-reviews-create-request
- name: PostApiWithdrawalsCreateRequest
  property_count: 2
  slug: dollarr-xyz-post-api-withdrawals-create-request
- name: PutApiAutoBidRequest
  property_count: 3
  slug: dollarr-xyz-put-api-auto-bid-request
jsonld:
- class_count: 18
  name: Dollarr Xyz Context
  property_count: 31
  slug: dollarr-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at dollarr.xyz requiring an API key.
  name: dollarr MCP Server
  slug: dollarr-xyz-mcp-yml
modified: '2026-11-05'
name: dollarr
nav: Providers
network: true
overview: 'dollarr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Freelance, Micro‑tasks, and USDC.


  The dollarr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dollarr''s developer surface includes documentation, API reference, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Dollarr Xyz Plans Pricing
  plan_count: 2
  slug: dollarr-xyz-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: dollarr API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: dollarr-xyz-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 33.3
    discoverability: 56.7
    operational_transparency: 0.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dollarr Xyz Domain Security
  slug: dollarr-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dollarr-xyz
tags:
- Artificial Intelligence
- Marketplace
- Freelance
- Micro‑tasks
- USDC
website: https://dollarr.xyz/
---
