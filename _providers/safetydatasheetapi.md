---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Safetydatasheetapi Agentic Access
  operation_count: 6
  slug: safetydatasheetapi-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: REST API that extracts structured data from Safety Data Sheet PDFs, returning normalized 16-section records as JSON/XML/CSV. Includes synchronous single-document extraction, async bulk jobs with webho
  name: SDS/MSDS Extraction REST API
  slug: sdsmsds-extraction-rest-api
artifact_total: 15
asyncapis:
- description: ''
  name: Safetydatasheetapi Webhooks
  slug: safetydatasheetapi-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://safetydatasheetapi.com/blog/
- group: auth
  href: https://artifacts.apis.io/safetydatasheetapi/security/safetydatasheetapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safetydatasheetapi-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/safetydatasheetapi/plans/safetydatasheetapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/safetydatasheetapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/safetydatasheetapi/rate-limits/safetydatasheetapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/safetydatasheetapi-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/safetydatasheetapi/conventions/safetydatasheetapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/safetydatasheetapi-conventions.yml
- group: company
  title: ''
  type: Website
  url: https://safetydatasheetapi.com
created: '2026-09-16'
description: A REST API by SafetyDataSheetAPI (a product of DscvryAI) that converts Safety Data Sheet PDFs into normalized 16-section structured records (product identity, GHS/H&P statements, composition, exposure controls/PPE, tox/eco data, disposal, transport, regulatory, revision metadata) output as JSON, XML, and CSV with confidence scores and warnings. Supports OCR for scanned PDFs, multilingual input, custom schema mapping, and bulk/webhook async flows.
json_schemas:
- name: BulkJobAccepted
  property_count: 5
  slug: safetydatasheetapi-bulk-job-accepted
- name: BulkJobStatus
  property_count: 10
  slug: safetydatasheetapi-bulk-job-status
- name: ExtractionResponse
  property_count: 12
  slug: safetydatasheetapi-extraction-response
jsonld:
- class_count: 6
  name: Safetydatasheetapi Context
  property_count: 27
  slug: safetydatasheetapi-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 3 tools listed. A candidate, not confirmed as published by the provider.
  name: Safety Data Sheet (SDS/MSDS) Extraction API MCP Server
  slug: safetydatasheetapi-mcp-yml
modified: '2026-10-06'
name: Safety Data Sheet (SDS/MSDS) Extraction API
nav: Providers
network: true
overview: 'Safety Data Sheet (SDS/MSDS) Extraction API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: SDS/MSDS Extraction REST API. Tagged areas include Safety Data Sheets, msds, ghs-classification, chemical-compliance, and EHS.


  The Safety Data Sheet (SDS/MSDS) Extraction API catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Safety Data Sheet (SDS/MSDS) Extraction API''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Safetydatasheetapi Plans Pricing
  plan_count: 4
  slug: safetydatasheetapi-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Safetydatasheetapi Rate Limits
  slug: safetydatasheetapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Safety Data Sheet (SDS/MSDS) Extraction API API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: safetydatasheetapi-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.5
    catalog_earned_first_party: 12.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 55.8
    developer_ergonomics: 11.9
    discoverability: 69.6
    operational_transparency: 0.0
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/safetydatasheetapi/safetydatasheetapi-2026-10-11T125502.png
security:
- kind: authentication
  name: Safetydatasheetapi Authentication
  slug: safetydatasheetapi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Safetydatasheetapi Domain Security
  slug: safetydatasheetapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Safetydatasheetapi Vulnerability Disclosure
  slug: safetydatasheetapi-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: safetydatasheetapi-bulk-extraction
  slug: safetydatasheetapi-bulk-extraction
slug: safetydatasheetapi
tags:
- Safety Data Sheets
- msds
- ghs-classification
- chemical-compliance
- EHS
- Regulatory Compliance
- Document Extraction
- OCR
- pdf-to-json
- data-normalization
- ERP Integration
- PLM
- Supply Chain
- Chemicals
website: https://safetydatasheetapi.com
---
