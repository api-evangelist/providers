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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/counterpane-domain-security.yml
created: '2026-07-17'
description: 'Counterpane Internet Security, Inc. was a managed security services provider founded by cryptographer Bruce Schneier, growing out of his Counterpane Systems cryptography consultancy. Counterpane pioneered Managed Security Monitoring (MSM) — outsourced, 24x7 human-staffed security operations centers that monitored customer networks and devices for intrusions, rather than selling security products. It was venture-backed, with Accel among its investors, and was acquired by BT Group in 2006, after which its operations were folded into BT''s managed security business. The company is defunct as an independent entity: it operates no product, developer portal, documentation, SDKs, or API surface today. As of the 2026-07-20 enrichment probe, counterpane.com resolves (209.17.116.163, Network Solutions nameservers) but refuses HTTPS on port 443, and plain HTTP redirects to https://www.schneier.com/ — Bruce Schneier''s personal site. www.counterpane.com returns HTTP 404. There is no MX,
  SPF, DMARC, or CAA record on the domain. This profile is retained as a historical record; there is no API surface to enrich.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/counterpane.png
layout: provider
modified: '2026-07-20'
name: Counterpane
nav: Providers
network: true
overview: Counterpane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Managed Security Services, Security Monitoring, and Defunct.
random_paper: 48
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Counterpane Domain Security
  slug: counterpane-domain-security
  summary_line: no transport/DNS hardening detected
slug: counterpane
tags:
- Company
- Cybersecurity
- Managed Security Services
- Security Monitoring
- Defunct
- Acquired
- Historical
---
