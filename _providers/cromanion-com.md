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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Cromanion provides an AI‑powered conversion agent API accessible via its MCP endpoint.
  name: Cromanion API
  slug: cromanion-api
- baseURL: https://in.cromanion.com
  baseurl_source: declared
  description: 'Cromanion API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cromanion API
  slug: cromanion-com-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/cromanion-com/plans/cromanion-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cromanion-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cromanion-com/rules/cromanion-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cromanion-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cromanion-com/json-ld/cromanion-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cromanion-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cromanion-com/vocabulary/cromanion-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cromanion-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cromanion-com/data-model/cromanion-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cromanion-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cromanion-com/authentication/cromanion-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cromanion-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cromanion-com/conformance/cromanion-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cromanion-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cromanion-com/llms/cromanion-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cromanion-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cromanion-com/mcp/cromanion-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cromanion-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/cromanion-com/hosts/cromanion-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cromanion-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cromanion-com/vendors/cromanion-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cromanion-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://cromanion.com/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cromanion.com/developers
- group: auth
  href: https://artifacts.apis.io/cromanion-com/security/cromanion-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cromanion-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cromanion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cromanion.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cromanion.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cromanion.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cromanion.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://cromanion.com/install
coverage:
  detail: MCP endpoint requires POST requests, which are disallowed, preventing contract retrieval.
  evidence:
  - status: 405
    url: https://cromanion.com/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-04'
description: Cromanion provides an AI-powered conversion agent that analyzes website traffic tags to identify high-value visitors and runs controlled experiments to improve conversion rates. The platform operates as a black-box service, requiring only a single tag integration to deliver insights and automated optimization, positioning itself as a self‑running tool for marketers seeking data‑driven growth without extensive manual setup.
image: https://cromanion.com/og.png
json_schemas:
- name: GetApiAgentErrorsResponse
  property_count: 1
  slug: cromanion-com-get-api-agent-errors-response
- name: GetApiAgentInstallCheckResponse
  property_count: 1
  slug: cromanion-com-get-api-agent-install-check-response
- name: GetApiAgentSiteResponse
  property_count: 2
  slug: cromanion-com-get-api-agent-site-response
- name: PostApiAgentCheckoutRequest
  property_count: 1
  slug: cromanion-com-post-api-agent-checkout-request
- name: PostApiAgentCheckoutResponse
  property_count: 1
  slug: cromanion-com-post-api-agent-checkout-response
- name: PostApiAgentClaimsVerifyResponse
  property_count: 3
  slug: cromanion-com-post-api-agent-claims-verify-response
jsonld:
- class_count: 8
  name: Cromanion Com Context
  property_count: 12
  slug: cromanion-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at cromanion.com.
  name: Cromanion MCP Server
  slug: cromanion-com-mcp-yml
modified: '2026-11-04'
name: Cromanion
nav: Providers
network: true
overview: 'Cromanion is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, CRO, Conversion, and Marketing.


  The Cromanion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cromanion''s developer surface includes authentication, support, documentation, pricing, getting-started guide, and 15 more developer resources.'
plans:
- name: Cromanion Com Plans Pricing
  plan_count: 4
  slug: cromanion-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Cromanion API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 1
  slug: cromanion-com-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 47.6
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cromanion Com Authentication
  slug: cromanion-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cromanion Com Domain Security
  slug: cromanion-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cromanion-com
tags:
- Company
- Artificial Intelligence
- CRO
- Conversion
- Marketing
- Software-as-a-Service
website: https://cromanion.com/
---
