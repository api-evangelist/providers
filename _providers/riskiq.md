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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/security/business/siem-and-xdr/microsoft-defender-threat-intelligence
created: '2026-07-17'
description: RiskIQ was a San Francisco-based external threat intelligence and attack surface management company, known for its PassiveTotal platform (passive DNS, WHOIS, SSL certificate and host-pair intelligence), Digital Footprint external asset discovery, and External Threats brand/phishing detection. It exposed a developer REST API at api.riskiq.net and a research console at community.riskiq.com. Microsoft acquired RiskIQ in 2021 and folded its technology into Microsoft Defender Threat Intelligence (MDTI) and Microsoft Defender External Attack Surface Management (Defender EASM). As of this enrichment pass the riskiq.com domain runs on Microsoft/Azure infrastructure and www.riskiq.com issues a 301 redirect to the Microsoft Defender Threat Intelligence product page; the standalone RiskIQ/PassiveTotal API hosts (api.riskiq.net, community.riskiq.com) no longer accept connections. This profile is retained as a historical/acquired-company record with no live, independent API surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riskiq.png
layout: provider
modified: '2026-07-21'
name: RiskIQ
nav: Providers
network: true
overview: RiskIQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Threat Intelligence, Attack Surface Management, and Cybersecurity.
random_paper: 8
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: riskiq
tags:
- Company
- Security
- Threat Intelligence
- Attack Surface Management
- Cybersecurity
- Passive DNS
- Acquired
website: https://www.microsoft.com/security/business/siem-and-xdr/microsoft-defender-threat-intelligence
---
