---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: REST API that extracts structured data from Safety Data Sheet PDFs, returning normalized 16-section records as JSON/XML/CSV. Includes synchronous single-document extraction, async bulk jobs with webho
  name: SDS/MSDS Extraction REST API
  slug: sdsmsds-extraction-rest-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safetydatasheetapi/refs/heads/main/security/safetydatasheetapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safetydatasheetapi-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/safetydatasheetapi/refs/heads/main/plans/safetydatasheetapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/safetydatasheetapi-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/safetydatasheetapi/refs/heads/main/rate-limits/safetydatasheetapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/safetydatasheetapi-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/safetydatasheetapi/refs/heads/main/conventions/safetydatasheetapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/safetydatasheetapi-conventions.yml
- group: company
  title: ''
  type: Website
  url: https://safetydatasheetapi.com
created: '2026-09-16'
description: A REST API by SafetyDataSheetAPI (a product of DscvryAI) that converts Safety Data Sheet PDFs into normalized 16-section structured records (product identity, GHS/H&P statements, composition, exposure controls/PPE, tox/eco data, disposal, transport, regulatory, revision metadata) output as JSON, XML, and CSV with confidence scores and warnings. Supports OCR for scanned PDFs, multilingual input, custom schema mapping, and bulk/webhook async flows.
layout: provider
mcp_servers:
- description: ''
  name: Safety Data Sheet (SDS/MSDS) Extraction API MCP Server
  slug: safety-data-sheet-sdsmsds-extraction-api-mcp-server
modified: '2026-09-16'
name: Safety Data Sheet (SDS/MSDS) Extraction API
nav: Providers
network: true
overview: 'Safety Data Sheet (SDS/MSDS) Extraction API publishes 1 API on the [APIs.io](https://apis.io/) network: SDS/MSDS Extraction REST API. Tagged areas include SDS, msds, Safety Data Sheets, ghs-classification, and chemical-compliance.'
plans:
- name: Safetydatasheetapi Plans Pricing
  plan_count: 4
  slug: safetydatasheetapi-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Safetydatasheetapi Rate Limits
  slug: safetydatasheetapi-rate-limits
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 72.2
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Safetydatasheetapi Domain Security
  slug: safetydatasheetapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: safetydatasheetapi
tags:
- SDS
- msds
- Safety Data Sheets
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
