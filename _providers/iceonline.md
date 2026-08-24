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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iceonline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iceonline.cn/
created: '2026-07-17'
description: 'iceonline (冰场联盟) operates an enterprise-grade backend management platform for ice rinks in China, published at www.iceonline.cn as a login-gated single-page administrative console branded "冰场联盟 企业级后台管理系统" (Ice Rink Alliance Enterprise Management System). The company was surfaced as a portfolio company of Qiming Venture Partners and added to the API Evangelist network as a lead for enrichment. As of this enrichment pass the public surface is a private SPA with no discoverable API: no OpenAPI/Swagger, SDK, developer portal, changelog, or security.txt was found — every probed path (including /.well-known/*, /swagger.json, /openapi.json) returns the SPA shell rather than a real document. Only live domain-security posture (TLS/DNS) could be captured this round.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iceonline.png
layout: provider
modified: '2026-07-19'
name: iceonline
nav: Providers
network: true
overview: iceonline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ice Rink, Facility Management, Enterprise Software, and Sports and Recreation.
random_paper: 5
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iceonline/refs/heads/main/screenshots/iceonline-2026-07-25T222106.png
security:
- kind: domain-security
  name: Iceonline Domain Security
  slug: iceonline-domain-security
  summary_line: TLSv1.2
slug: iceonline
tags:
- Company
- Ice Rink
- Facility Management
- Enterprise Software
- Sports and Recreation
- Software-as-a-Service
- China
website: https://www.iceonline.cn/
---
