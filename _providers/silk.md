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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silk.security/
created: '2026-07-17'
description: Silk (Silk Security) was a cybersecurity company backed by Insight Partners that built an exposure, vulnerability and security-finding correlation / risk-prioritization platform. As of this enrichment pass its primary domain silk.security issues a verified 301 redirect to armis.com, indicating the company and product have been absorbed into Armis; no standalone Silk developer or API surface (developer portal, OpenAPI, SDKs, docs, or status page) is currently published, so there is no independent API to enrich beyond a domain-security probe of the still-live silk.security host.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silk.png
layout: provider
modified: '2026-07-21'
name: Silk
nav: Providers
network: true
overview: Silk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Vulnerability Management, and Exposure Management.
random_paper: 15
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Silk Domain Security
  slug: silk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: silk
tags:
- Company
- Cybersecurity
- Security
- Vulnerability Management
- Exposure Management
- Risk
website: https://www.silk.security/
---
