---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Machine-readable contract for APIR services via MCP JSON-RPC.
  name: APIR MCP
  slug: apir-mcp
- baseURL: https://podncdlwtknujadrtsxz.supabase.co/functions/v1/Audit
  baseurl_source: declared
  description: 'APIR API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: APIR API
  slug: apir-ai-api
artifact_total: 18
common:
- group: design
  href: https://artifacts.apis.io/apir-ai/rules/apir-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/apir-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/apir-ai/json-ld/apir-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apir-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/apir-ai/vocabulary/apir-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apir-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apir-ai/data-model/apir-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apir-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://apir.ai/trust
- group: auth
  title: ''
  type: Security
  url: https://apir.ai/trust#disclosure
- group: design
  href: https://artifacts.apis.io/apir-ai/conformance/apir-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apir-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apir-ai/llms/apir-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apir-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/apir-ai/mcp/apir-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apir-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/apir-ai/well-known/apir-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apir-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/apir-ai/well-known/apir-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apir-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/apir-ai/well-known/apir-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apir-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/apir-ai/hosts/apir-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apir-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/apir-ai/vendors/apir-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apir-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://apir.ai/login
- group: auth
  href: https://artifacts.apis.io/apir-ai/security/apir-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apir-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/apir-ai/security/apir-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apir-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/apir-ai/security/apir-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apir-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apir.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apir.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://apir.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apir.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://apir.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apir-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://apir.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apir.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apir.ai/legal/privacy
created: '2026-11-01'
description: APIR is the evidence record for AI agents. It provides a tamper‑evident work history for each AI, signed with Ed25519 keys and anchored by RFC 3161 timestamps. Buyers, auditors and insurers can verify an agent’s credentials without trusting the provider. The platform also offers file sealing, business‑seller financial checks, and integrates with existing AI workflows. Founded in 2025 by RIPA PTY LTD in Adelaide, Australia, APIR aims to bring transparency and trust to autonomous systems.
image: https://apir.ai/images/brand/1200x1200.png
json_schemas:
- name: GetApiV1ProfileResponse
  property_count: 5
  slug: apir-ai-get-api-v1-profile-response
- name: GetApiV1ResolveResponse
  property_count: 10
  slug: apir-ai-get-api-v1-resolve-response
- name: PostApiV1EventsRequest
  property_count: 2
  slug: apir-ai-post-api-v1-events-request
- name: PostApiV1EventsResponse
  property_count: 2
  slug: apir-ai-post-api-v1-events-response
- name: PostApiV1ResolveRequest
  property_count: 2
  slug: apir-ai-post-api-v1-resolve-request
- name: PostApiV1SealRequest
  property_count: 7
  slug: apir-ai-post-api-v1-seal-request
jsonld:
- class_count: 10
  name: Apir Ai Context
  property_count: 34
  slug: apir-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at apir.ai.
  name: APIR MCP Server
  slug: apir-ai-mcp-yml
modified: '2026-11-01'
name: APIR
nav: Providers
network: true
overview: 'APIR is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Evidence, Audit, Security, and Blockchain.


  The APIR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIR''s developer surface includes documentation, API reference, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Apir Ai Plans Pricing
  plan_count: 0
  slug: apir-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Apir Ai Rate Limits
  slug: apir-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: APIR API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: apir-ai-rules
scopes:
- name: Apir Ai Scopes
  scope_count: 0
  slug: apir-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 14.3
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 38.7
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
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apir Ai Authentication
  slug: apir-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apir Ai Domain Security
  slug: apir-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apir Ai Vulnerability Disclosure
  slug: apir-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Apir Ai Trust Center
  slug: apir-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apir-ai
tags:
- Artificial Intelligence
- Evidence
- Audit
- Security
- Blockchain
website: https://apir.ai/
---
