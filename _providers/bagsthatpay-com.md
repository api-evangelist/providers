---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Bagsthatpay Com Agentic Access
  operation_count: 34
  slug: bagsthatpay-com-agentic-access
  summary_line: 34 operations · 31 acting
api_count: 1
apis:
- baseURL: https://bagsthatpay.com
  baseurl_source: declared
  description: dataset
  name: Bags That Pay Dataset API
  slug: bagsthatpay-com-dataset-api
- baseURL: https://bagsthatpay.com
  baseurl_source: declared
  description: enquiry
  name: Bags That Pay Enquiry API
  slug: bagsthatpay-com-enquiry-api
- baseURL: https://bagsthatpay.com
  baseurl_source: declared
  description: entities
  name: Bags That Pay Entities API
  slug: bagsthatpay-com-entities-api
- baseURL: https://bagsthatpay.com
  baseurl_source: declared
  description: listing
  name: Bags That Pay Listing API
  slug: bagsthatpay-com-listing-api
- baseURL: https://bagsthatpay.com
  baseurl_source: declared
  description: The mcp API from Bags That Pay — 1 operation(s) for mcp.
  name: Bags That Pay MCP API
  slug: bagsthatpay-com-mcp-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/bagsthatpay-com/agentic-access/bagsthatpay-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bagsthatpay-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bagsthatpay-com/rules/bagsthatpay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bagsthatpay-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bagsthatpay-com/vocabulary/bagsthatpay-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bagsthatpay-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bagsthatpay-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://bagsthatpay.com/terms
- group: design
  href: https://artifacts.apis.io/bagsthatpay-com/errors/bagsthatpay-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bagsthatpay-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bagsthatpay-com/conformance/bagsthatpay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bagsthatpay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bagsthatpay-com/llms/bagsthatpay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bagsthatpay-com-llms.txt
- group: build
  href: https://artifacts.apis.io/bagsthatpay-com/mcp/bagsthatpay-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bagsthatpay-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bagsthatpay-com/mcp/bagsthatpay-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bagsthatpay-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bagsthatpay-com/well-known/bagsthatpay-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bagsthatpay-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bagsthatpay-com/well-known/bagsthatpay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bagsthatpay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bagsthatpay-com/hosts/bagsthatpay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bagsthatpay-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bagsthatpay-com/vendors/bagsthatpay-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bagsthatpay-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bagsthatpay-com/authentication/bagsthatpay-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bagsthatpay-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bagsthatpay-com/security/bagsthatpay-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bagsthatpay-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bagsthatpay-com/security/bagsthatpay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bagsthatpay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bagsthatpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bagsthatpay.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://bagsthatpay.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: mailto:hello@bagsthatpay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bagsthatpay.com/terms/listing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bagsthatpay.com/privacy/
created: '2026-11-02'
description: Bags That Pay provides tokenized treasury bills and other financial tokens, publishing the terms of 96 tokens sourced from issuers, DeFiLlama and CoinGecko. Each token page details what it represents, the claim shape, and issuer statements on redemption, eligibility, and payouts.
image: https://bagsthatpay.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at bagsthatpay.com.
  name: Bags That Pay MCP Server
  slug: bagsthatpay-com-mcp-yml
modified: '2026-11-02'
name: Bags That Pay
nav: Providers
network: true
overview: 'Bags That Pay publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dataset API, Enquiry API, Entities API, and 2 more. Tagged areas include Finance, Tokenization, Treasury-Bills, DeFi, and Data Aggregation.


  The Bags That Pay catalog on APIs.io includes 1 Spectral governance ruleset.


  Bags That Pay''s developer surface includes authentication, documentation, API reference, support, and 19 more developer resources.'
plans:
- name: Bagsthatpay Com Plans Pricing
  plan_count: 0
  slug: bagsthatpay-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Bagsthatpay Com Rate Limits
  slug: bagsthatpay-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Bags That Pay API Rules
  rule_count: 53
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 11
  slug: bagsthatpay-com-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 49.8
    developer_ergonomics: 31.4
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bagsthatpay Com Authentication
  slug: bagsthatpay-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bagsthatpay Com Domain Security
  slug: bagsthatpay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bagsthatpay Com Vulnerability Disclosure
  slug: bagsthatpay-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset
  slug: bagsthatpay-com-dataset
slug: bagsthatpay-com
tags:
- Finance
- Tokenization
- Treasury-Bills
- DeFi
- Data Aggregation
website: https://bagsthatpay.com/
---
