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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kura-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kura.tech
created: '2026-07-17'
description: Kura is a company surfaced as a portfolio company of 500-global and added to the API Evangelist network as a stub for enrichment. An enrichment pass on 2026-07-19 found no live company or developer surface behind this profile. The domain kura.tech resolves to GoDaddy nameservers and serves a parked-domain lander on every path, returning HTTP 200 for arbitrary URLs (a soft-404 catch-all), so no documentation, API reference, OpenAPI, SDK, or /.well-known artifact could be verified. The domain publishes no MX, SPF, DMARC, CAA, or DNSSEC records, indicating it is not in active operational use. No first-party GitHub organization was identified. The only artifact captured is a probed domain-security posture. This profile remains a dormant lead pending a confirmed live website for the company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kura.png
layout: provider
modified: '2026-07-19'
name: Kura
nav: Providers
network: true
overview: Kura is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Portfolio Lead, 500 Global, Dormant, and Parked Domain.
random_paper: 15
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kura/refs/heads/main/screenshots/kura-2026-07-25T224329.png
security:
- kind: domain-security
  name: Kura Domain Security
  slug: kura-domain-security
  summary_line: TLSv1.3
slug: kura
tags:
- Company
- Portfolio Lead
- 500 Global
- Dormant
- Parked Domain
website: https://kura.tech
---
