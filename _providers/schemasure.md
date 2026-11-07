---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://schemasure.com
  baseurl_source: spec
  description: The Health API from SchemaSure — 1 operation(s) for health.
  name: SchemaSure Health API
  slug: schemasure-health-api
- baseURL: https://schemasure.com
  baseurl_source: spec
  description: The Image extraction · x402 V2 API from SchemaSure — 1 operation(s) for image extraction · x402 v2.
  name: SchemaSure Image extraction · x402 V2 API
  slug: schemasure-image-extraction-x402-v2-api
- baseURL: https://schemasure.com
  baseurl_source: spec
  description: The Legacy V1 evaluation API API from SchemaSure — 1 operation(s) for legacy v1 evaluation api.
  name: SchemaSure Legacy V1 evaluation API
  slug: schemasure-legacy-v1-evaluation-api-api
- baseURL: https://schemasure.com
  baseurl_source: spec
  description: The Primary x402 V2 API API from SchemaSure — 1 operation(s) for primary x402 v2 api.
  name: SchemaSure Primary x402 V2 API
  slug: schemasure-primary-x402-v2-api-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/schemasure/overlays/schemasure-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/schemasure-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://schemasure.com
- group: auth
  href: https://artifacts.apis.io/schemasure/security/schemasure-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/schemasure-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/schemasure/security/schemasure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/schemasure-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/schemasure/well-known/schemasure-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/schemasure-well-known.yml
- group: auth
  href: https://artifacts.apis.io/schemasure/well-known/schemasure-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/schemasure-security.txt
- group: auth
  href: https://artifacts.apis.io/schemasure/security/schemasure-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/schemasure-vulnerability-disclosure.yml
- group: build
  href: https://artifacts.apis.io/schemasure/packages/schemasure-packages.yml
  title: ''
  type: Packages
  url: packages/schemasure-packages.yml
- group: build
  href: https://artifacts.apis.io/schemasure/packages/schemasure-packages.yml
  title: ''
  type: SDKs
  url: packages/schemasure-packages.yml
- group: agent
  href: https://artifacts.apis.io/schemasure/mcp/schemasure-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/schemasure-mcp.yml
- group: design
  href: https://artifacts.apis.io/schemasure/conformance/schemasure-conformance.yml
  title: ''
  type: Conformance
  url: conformance/schemasure-conformance.yml
- group: design
  href: https://artifacts.apis.io/schemasure/lifecycle/schemasure-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/schemasure-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/schemasure/authentication/schemasure-authentication.yml
  title: ''
  type: Authentication
  url: authentication/schemasure-authentication.yml
- group: start
  href: https://artifacts.apis.io/schemasure/sandbox/schemasure-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/schemasure-sandbox.yml
- group: design
  href: https://artifacts.apis.io/schemasure/conventions/schemasure-conventions.yml
  title: ''
  type: Conventions
  url: conventions/schemasure-conventions.yml
- group: design
  href: https://artifacts.apis.io/schemasure/data-model/schemasure-data-model.yml
  title: ''
  type: DataModel
  url: data-model/schemasure-data-model.yml
- group: agent
  href: https://artifacts.apis.io/schemasure/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/schemasure/plans/schemasure-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/schemasure-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/schemasure/rate-limits/schemasure-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/schemasure-rate-limits.yml
- group: other
  title: ''
  type: APIsJson
  url: https://schemasure.com/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://schemasure.com/.well-known/pricing.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://schemasure.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://schemasure.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@schemasure.com
created: '2026-07-19'
description: Structured data extraction API that converts unstructured text or HTML into JSON guaranteed to validate against a caller-supplied JSON Schema, or returns a typed error at no charge. Access is gated by x402 pay-per-call micropayments (USDC on Base), with no accounts or API keys.
finops:
- has_sources: true
  method: derived
  name: Schemasure Finops
  primary_unit: successful extraction
  service_category: ''
  slug: schemasure-finops
  template: false
image: https://schemasure.com/icon.svg
layout: provider
mcp_servers:
- description: First-party MCP client, local-stdio only (npx -y @noamjose/schemasure); no hosted endpoint — /mcp probed 404 on 2026-09-03.
  name: SchemaSure MCP Server
  slug: schemasure-mcp-yml
modified: '2026-09-03'
name: SchemaSure
nav: Providers
network: true
overview: 'SchemaSure publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Image extraction · x402 V2 API, Legacy V1 evaluation API, and 1 more. Tagged areas include Structured Data Extraction, text-to-JSON, JSON Schema, Document Parsing, and Data Cleaning.


  The SchemaSure catalog on APIs.io includes 1 Spectral governance ruleset.


  SchemaSure''s developer surface includes authentication, sandbox, pricing, support, and 20 more developer resources.'
plans:
- name: Schemasure Plans Pricing
  plan_count: 2
  slug: schemasure-plans-pricing
- name: Schemasure Price Estimates
  plan_count: 0
  slug: schemasure-price-estimates
random_paper: 16
rate_limits:
- limit_count: 0
  name: Schemasure Rate Limits
  slug: schemasure-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: SchemaSure API Rules
  rule_count: 44
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 2
  slug: schemasure-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 42.3
    discoverability: 70.0
    operational_transparency: 10.5
  previous_composite: 44.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/schemasure/schemasure-2026-09-02T154524.png
security:
- kind: authentication
  name: Schemasure Authentication
  slug: schemasure-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Schemasure Domain Security
  slug: schemasure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Schemasure Vulnerability Disclosure
  slug: schemasure-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: schemasure-extract-image-to-schema
  slug: schemasure-extract-image-to-schema
- name: schemasure-extract-text-to-schema
  slug: schemasure-extract-text-to-schema
slug: schemasure
tags:
- Structured Data Extraction
- text-to-JSON
- JSON Schema
- Document Parsing
- Data Cleaning
- LLM Tooling
- AI Agents
- x402-micropayments
- Agent-Native
- A2A
- MCP
website: https://schemasure.com
---
