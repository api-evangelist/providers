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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/closure-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/closure-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/closure-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.closure-intel.com/
- group: company
  title: ''
  type: Website
  url: https://www.closure-intel.com/
created: '2026-07-17'
description: Closure (Closure Intelligence, Inc.) builds an AI-powered digital analyst platform for law enforcement agencies that securely transcribes, translates, searches, organizes, and analyzes case evidence — jail communications, warrant returns, and large multi-lingual case files — to help investigators overcome evidence overload and resolve homicides and cold cases. The platform runs under a zero-access security model with SOC 2 Type II, CJIS, and HIPAA compliance. Backed by CRV. No public API or developer program is currently published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/closure.png
layout: provider
modified: '2026-07-18'
name: Closure
nav: Providers
network: true
overview: Closure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Law Enforcement, Public Safety, and Evidence Analysis.
random_paper: 72
score:
  band: minimal
  composite: 10.0
  delta: -2.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Closure Domain Security
  slug: closure-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Closure Trust Center
  slug: closure-trust-center
  summary_line: SOC 2 Type II, CJIS, HIPAA
slug: closure
tags:
- Company
- Artificial Intelligence
- Law Enforcement
- Public Safety
- Evidence Analysis
- GovTech
- Security
- Compliance
website: https://www.closure-intel.com/
---
