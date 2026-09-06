---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://schemasure.com
  baseurl_source: declared
  description: REST API (OpenAPI 3.1) exposing POST /v2/extract for text/HTML and POST /v2/extract-image for document images (both x402 V2 paid, charge-only-on-success), a deprecated legacy POST /extract with 3 free
  name: SchemaSure Structured Extraction API
  slug: schemasure-structured-extraction-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://schemasure.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/schemasure-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schemasure-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/schemasure-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/schemasure-security.txt
- group: auth
  title: ''
  type: Security
  url: security/schemasure-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/schemasure-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/schemasure-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/schemasure-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/schemasure-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/schemasure-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/schemasure-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/schemasure-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/schemasure-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/schemasure-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/schemasure-plans-pricing.yml
- group: operate
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
created: '2026-07-19'
description: Structured data extraction API that converts unstructured text or HTML into JSON guaranteed to validate against a caller-supplied JSON Schema, or returns a typed error at no charge. Access is gated by x402 pay-per-call micropayments (USDC on Base), with no accounts or API keys.
image: https://schemasure.com/icon.svg
layout: provider
mcp_servers:
- description: First-party MCP client, local-stdio only (npx -y @noamjose/schemasure); no hosted endpoint — /mcp probed 404 on 2026-09-03.
  name: SchemaSure MCP Server
  slug: schemasure-mcp-server
modified: '2026-09-03'
name: SchemaSure
nav: Providers
network: true
overview: 'SchemaSure publishes 1 API on the [APIs.io](https://apis.io/) network: Structured Extraction API. Tagged areas include Structured Data Extraction, text-to-JSON, JSON-Schema, Document Parsing, and Data Cleaning.


  SchemaSure''s developer surface includes authentication, sandbox, pricing, and 19 more developer resources.'
plans:
- name: Schemasure Plans Pricing
  plan_count: 2
  slug: schemasure-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Schemasure Rate Limits
  slug: schemasure-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 44.2
    developer_ergonomics: 37.5
    discoverability: 83.3
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 38.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/schemasure/refs/heads/main/screenshots/schemasure-2026-09-02T154524.png
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
slug: schemasure
tags:
- Structured Data Extraction
- text-to-JSON
- JSON-Schema
- Document Parsing
- Data Cleaning
- LLM Tooling
- AI Agents
- x402-micropayments
- agent-native
- A2A
- MCP
website: https://schemasure.com
---
