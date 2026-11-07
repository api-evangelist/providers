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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bol Ai Agentic Access
  operation_count: 15
  slug: bol-ai-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- baseURL: https://bol.ai
  baseurl_source: declared
  description: The Billing API from Bol.ai — 1 operation(s) for billing.
  name: Bol.ai Billing API
  slug: bol-ai-billing-api
- baseURL: https://bol.ai
  baseurl_source: declared
  description: The Bol API from Bol.ai — 7 operation(s) for bol.
  name: Bol.ai Bol API
  slug: bol-ai-bol-api
- baseURL: https://bol.ai
  baseurl_source: declared
  description: The Mcp API from Bol.ai — 1 operation(s) for mcp.
  name: Bol.ai MCP API
  slug: bol-ai-mcp-api
- baseURL: https://bol.ai
  baseurl_source: declared
  description: The Me API from Bol.ai — 2 operation(s) for me.
  name: Bol.ai Me API
  slug: bol-ai-me-api
- baseURL: https://bol.ai
  baseurl_source: declared
  description: The Usage API from Bol.ai — 1 operation(s) for usage.
  name: Bol.ai Usage API
  slug: bol-ai-usage-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/bol-ai/agentic-access/bol-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bol-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bol-ai/plans/bol-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bol-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bol-ai/rules/bol-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bol-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bol-ai/json-ld/bol-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bol-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bol-ai/vocabulary/bol-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bol-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bol-ai/data-model/bol-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bol-ai-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://bol.ai/privacy/
- group: design
  href: https://artifacts.apis.io/bol-ai/errors/bol-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bol-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bol-ai/conformance/bol-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bol-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bol-ai/llms/bol-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bol-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/bol-ai/well-known/bol-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bol-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/bol-ai/well-known/bol-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bol-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bol-ai/hosts/bol-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bol-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bol-ai/vendors/bol-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bol-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bol.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bol.ai/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://bol.ai/pricing.md
- group: docs
  title: ''
  type: APIReference
  url: https://bol.ai/docs/
- group: auth
  href: https://artifacts.apis.io/bol-ai/authentication/bol-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bol-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bol-ai/security/bol-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bol-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bol-ai/security/bol-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bol-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bol.ai/
created: '2026-11-02'
description: Bol.ai provides an AI‑powered Bill of Lading extraction service that transforms PDFs, scans or photos of freight documents into structured JSON or CSV data. It helps freight forwarders, customs brokers and logistics companies automate data entry, reducing manual re‑typing and errors. The platform offers API keys, free trial credits, and supports EU data residency. Documentation, pricing, and a machine‑readable llms.txt are publicly available.
image: https://bol.ai/img/og.png
json_schemas:
- name: ExtractedDocument
  property_count: 0
  slug: bol-ai-extracted-document
jsonld:
- class_count: 10
  name: Bol Ai Context
  property_count: 70
  slug: bol-ai-context
layout: provider
modified: '2026-11-02'
name: Bol.ai
nav: Providers
network: true
overview: 'Bol.ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Bol API, MCP API, and 2 more. Tagged areas include Freight Documents, Data Extraction, Bill of Lading, and 3PL.


  The Bol.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bol.ai''s developer surface includes pricing, API reference, authentication, and 19 more developer resources.'
plans:
- name: Bol Ai Plans Pricing
  plan_count: 4
  slug: bol-ai-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Bol.ai API Rules
  rule_count: 43
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 4
  slug: bol-ai-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.2
    catalog_earned_first_party: 12.0
    catalog_gap: 48.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 60.3
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bol Ai Authentication
  slug: bol-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bol Ai Domain Security
  slug: bol-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bol Ai Vulnerability Disclosure
  slug: bol-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bol-ai
tags:
- Freight Documents
- Data Extraction
- Bill of Lading
- 3PL
website: https://bol.ai/
---
