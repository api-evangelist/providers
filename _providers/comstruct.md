---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comstruct-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/comstruct-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/comstruct-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.comstruct.com
- group: start
  title: ''
  type: Login
  url: https://app.comstruct.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comstruct.com/bedingungen-und-konditionen
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comstruct.com/datenschutzerklaerung
created: '2026-07-17'
description: Comstruct is a Munich-based construction technology company that provides AI-powered agents to automate the procurement of construction materials. Its platform runs the full procurement workflow from the bill of materials (Leistungsverzeichnis) through supplier inquiry, offer comparison, contract negotiation, digital delivery notes, AI-based invoice verification, and sustainability reporting. Customers include HOCHTIEF, Implenia, Marti, and Leonhard Weiss. Comstruct is backed by GV (Google Ventures). As of enrichment the company publishes no public developer portal, API reference, or OpenAPI definition; this profile is maintained in the API Evangelist network from its public web presence.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comstruct.png
layout: provider
modified: '2026-07-18'
name: Comstruct
nav: Providers
network: true
overview: Comstruct is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Construction, Construction Technology, and Procurement.
random_paper: 102
score:
  band: emerging
  composite: 12.8
  delta: -1.4
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comstruct/refs/heads/main/screenshots/comstruct-2026-07-25T210213.png
security:
- kind: domain-security
  name: Comstruct Domain Security
  slug: comstruct-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Comstruct Trust Center
  slug: comstruct-trust-center
  summary_line: trust center published
slug: comstruct
tags:
- Company
- Enterprise
- Construction
- Construction Technology
- Procurement
- Supply Chain
- Invoice Automation
- Fintech
- Artificial Intelligence
- Germany
website: https://www.comstruct.com
---
