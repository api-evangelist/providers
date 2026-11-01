---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Loopholetape Com Agentic Access
  operation_count: 40
  slug: loopholetape-com-agentic-access
  summary_line: 40 operations
api_count: 1
apis:
- baseURL: https://api.loopholetape.com
  baseurl_source: declared
  description: machine-readable descriptions of this service
  name: loopholetape-com Discovery API
  slug: loopholetape-com-discovery-api
- baseURL: https://api.loopholetape.com
  baseurl_source: declared
  description: no payment
  name: loopholetape-com Free API
  slug: loopholetape-com-free-api
- baseURL: https://api.loopholetape.com
  baseurl_source: declared
  description: x402-paid resources (USDC on Solana mainnet or Base)
  name: loopholetape-com Paid API
  slug: loopholetape-com-paid-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/loopholetape-com/overlays/loopholetape-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/loopholetape-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/loopholetape-com/agentic-access/loopholetape-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loopholetape-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/loopholetape-com/rate-limits/loopholetape-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loopholetape-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/loopholetape-com/rules/loopholetape-com-rules.yml
  title: ''
  type: Spectral
  url: rules/loopholetape-com-rules.yml
- group: design
  href: https://artifacts.apis.io/loopholetape-com/json-ld/loopholetape-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/loopholetape-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/loopholetape-com/vocabulary/loopholetape-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/loopholetape-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/loopholetape-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/loopholetape-com/data-model/loopholetape-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loopholetape-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://api.loopholetape.com/terms
- group: auth
  href: https://artifacts.apis.io/loopholetape-com/authentication/loopholetape-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loopholetape-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/loopholetape-com/errors/loopholetape-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loopholetape-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/loopholetape-com/conformance/loopholetape-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loopholetape-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/loopholetape-com/llms/loopholetape-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loopholetape-com-llms.txt
- group: other
  href: https://artifacts.apis.io/loopholetape-com/a2a/loopholetape-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/loopholetape-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/loopholetape-com/mcp/loopholetape-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/loopholetape-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/loopholetape-com/mcp/loopholetape-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/loopholetape-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/loopholetape-com/well-known/loopholetape-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/loopholetape-com-security.txt
- group: auth
  href: https://artifacts.apis.io/loopholetape-com/well-known/loopholetape-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/loopholetape-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/loopholetape-com/well-known/loopholetape-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loopholetape-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/loopholetape-com/hosts/loopholetape-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loopholetape-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/loopholetape-com/vendors/loopholetape-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loopholetape-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://api.loopholetape.com/pricing
- group: auth
  href: https://artifacts.apis.io/loopholetape-com/security/loopholetape-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/loopholetape-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/loopholetape-com/security/loopholetape-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loopholetape-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://loopholetape.com/
- group: docs
  title: ''
  type: Documentation
  url: https://loopholetape.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://loopholetape.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.loopholetape.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://loopholetape.com/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loopholetape.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loopholetape.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loopholetape
created: '2026-10-30'
description: Loopholetape provides live rug checks for new pump.fun memecoins on the Solana blockchain. It delivers calibrated rug probability, graduation odds, holder information, creator records, and token risk cards, computed in real time from independent capture of every on‑chain event. The service requires no account; payments are per request in USDC on Solana or Base via x402, with pricing from $0.001 per request. Operated by the loopholetape project, it offers transparent risk assessment for crypto traders.
image: https://loopholetape.com/favicon.ico
json_schemas:
- name: Envelope
  property_count: 7
  slug: loopholetape-com-envelope
- name: RiskEnvelope
  property_count: 7
  slug: loopholetape-com-risk-check
- name: VerdictEnvelope
  property_count: 7
  slug: loopholetape-com-verdict
jsonld:
- class_count: 6
  name: Loopholetape Com Context
  property_count: 18
  slug: loopholetape-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.loopholetape.com requiring an API key.
  name: loopholetape-com MCP Server
  slug: loopholetape-com-mcp-yml
modified: '2026-10-30'
name: loopholetape-com
nav: Providers
network: true
overview: 'loopholetape-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Free API, and Paid API. Tagged areas include Company, Crypto, Solana, Risk, and API.


  The loopholetape-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  loopholetape-com''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, and 27 more developer resources.'
plans:
- name: Loopholetape Com Plans Pricing
  plan_count: 0
  slug: loopholetape-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Loopholetape Com Rate Limits
  slug: loopholetape-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: loopholetape-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: loopholetape-com-rules
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 60.5
    developer_ergonomics: 56.4
    discoverability: 65.0
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Loopholetape Com Authentication
  slug: loopholetape-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Loopholetape Com Domain Security
  slug: loopholetape-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Loopholetape Com Vulnerability Disclosure
  slug: loopholetape-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: token-check
  slug: loopholetape-com-token_check
slug: loopholetape-com
tags:
- Company
- Crypto
- Solana
- Risk
- API
website: https://loopholetape.com/
---
