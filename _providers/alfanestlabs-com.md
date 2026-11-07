---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Reference for Veridex, the AlfaNest Labs control plane for data in motion, and public APIs of Agent Security, Machine Identity, and API Risk.
  name: Veridex API
  slug: veridex-api
- description: 'AlfaNest Labs API as documented publicly: 47 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AlfaNest Labs API
  slug: alfanestlabs-com-api
artifact_total: 17
common:
- group: operate
  href: https://artifacts.apis.io/alfanestlabs-com/rate-limits/alfanestlabs-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alfanestlabs-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/alfanestlabs-com/plans/alfanestlabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alfanestlabs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alfanestlabs-com/rules/alfanestlabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/alfanestlabs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/alfanestlabs-com/json-ld/alfanestlabs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alfanestlabs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/alfanestlabs-com/vocabulary/alfanestlabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alfanestlabs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/alfanestlabs-com/data-model/alfanestlabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alfanestlabs-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://alfanestlabs.com/trust
- group: auth
  href: https://artifacts.apis.io/alfanestlabs-com/authentication/alfanestlabs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alfanestlabs-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/alfanestlabs-com/conformance/alfanestlabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alfanestlabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alfanestlabs-com/llms/alfanestlabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alfanestlabs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alfanestlabs-com/mcp/alfanestlabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alfanestlabs-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/alfanestlabs-com/well-known/alfanestlabs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alfanestlabs-com-security.txt
- group: agent
  href: https://artifacts.apis.io/alfanestlabs-com/well-known/alfanestlabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alfanestlabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alfanestlabs-com/hosts/alfanestlabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alfanestlabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alfanestlabs-com/vendors/alfanestlabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alfanestlabs-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://alfanestlabs.com/ei-bnc/security
- group: company
  title: ''
  type: Blog
  url: https://alfanestlabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alfanestlabs
- group: auth
  href: https://artifacts.apis.io/alfanestlabs-com/security/alfanestlabs-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/alfanestlabs-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/alfanestlabs-com/security/alfanestlabs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alfanestlabs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alfanestlabs-com/security/alfanestlabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alfanestlabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alfanestlabs.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://alfanestlabs.com/prices
- group: start
  title: ''
  type: SignUp
  url: https://alfanestlabs.com/login?redirect=%2Fveridex%2Fdashboard
- group: operate
  title: ''
  type: Support
  url: https://alfanestlabs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alfanestlabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alfanestlabs.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://alfanestlabs.com/veridex
- group: docs
  title: ''
  type: APIReference
  url: https://alfanestlabs.com/api-risk
coverage:
  checked: '2026-11-01'
  detail: Documentation is served as a JavaScript‑rendered single‑page app, so no machine‑readable OpenAPI spec could be retrieved.
  evidence:
  - status: 200
    url: https://alfanestlabs.com/veridex/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AlfaNest Labs builds data security for humans, applications, and AI. Their flagship control plane Veridex secures data in motion, complemented by products like API Risk Monitor, Agent Security, Machine Identity, Clearance, SafeKey Vault, WASTE.LAND marketplace, and AlfaNest Academy for ISO/IEC 27001 auditor training. The company, founded in 2024 in Saint‑Fulgent, France, focuses on zero‑knowledge encryption, AI guardrails, and compliance frameworks.
image: https://alfanestlabs.com/alfanestlabs-logo.png
json_schemas:
- name: GetApiPublicVerifyIdResponse
  property_count: 7
  slug: alfanestlabs-com-get-api-public-verify-id-response
- name: PostApiAgentSecurityV1DecideRequest
  property_count: 8
  slug: alfanestlabs-com-post-api-agent-security-v1-decide-request
- name: PostApiProjectsIdRunResponse
  property_count: 9
  slug: alfanestlabs-com-post-api-projects-id-run-response
- name: PostApiScanCompareRequest
  property_count: 6
  slug: alfanestlabs-com-post-api-scan-compare-request
- name: PostApiVeridexRunRequest
  property_count: 5
  slug: alfanestlabs-com-post-api-veridex-run-request
- name: PostApiVeridexRunResponse
  property_count: 18
  slug: alfanestlabs-com-post-api-veridex-run-response
jsonld:
- class_count: 26
  name: Alfanestlabs Com Context
  property_count: 68
  slug: alfanestlabs-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at relay.alfanestlabs.com.
  name: AlfaNest Labs MCP Server
  slug: alfanestlabs-com-mcp-yml
modified: '2026-11-01'
name: AlfaNest Labs
nav: Providers
network: true
overview: 'AlfaNest Labs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Security, API Risk, Machine Identity, Artificial Intelligence, and Privacy.


  The AlfaNest Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AlfaNest Labs'' developer surface includes authentication, engineering blog, pricing, signup flow, support, documentation, API reference, and 22 more developer resources.'
plans:
- name: Alfanestlabs Com Plans Pricing
  plan_count: 8
  slug: alfanestlabs-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Alfanestlabs Com Rate Limits
  slug: alfanestlabs-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AlfaNest Labs API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: alfanestlabs-com-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 28.9
  previous_composite: 49.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alfanestlabs Com Authentication
  slug: alfanestlabs-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Alfanestlabs Com Domain Security
  slug: alfanestlabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alfanestlabs Com Vulnerability Disclosure
  slug: alfanestlabs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Alfanestlabs Com Trust Center
  slug: alfanestlabs-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: alfanestlabs-com
tags:
- Data Security
- API Risk
- Machine Identity
- Artificial Intelligence
- Privacy
website: https://alfanestlabs.com/
---
