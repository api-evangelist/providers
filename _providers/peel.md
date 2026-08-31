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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.peel.com/
created: '2026-07-17'
description: Peel Technologies Inc (peel.com) is a Redpoint Ventures-backed consumer technology company known for the Peel Smart Remote mobile app, which turned smartphones into universal remote controls for TVs, set-top boxes, and home-entertainment devices with a TV guide and content discovery layer. As of this enrichment pass the peel.com website resolves over HTTPS but serves only a single-logo placeholder page (frameset redirecting to an S3-hosted logo), indicating the company is dormant. No public developer portal, API documentation, OpenAPI, SDKs, or /.well-known discovery surface was found; developer/api/docs subdomains do not resolve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peel.png
layout: provider
modified: '2026-07-20'
name: Peel
nav: Providers
network: true
overview: Peel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Smart Remote, Mobile App, and Media and Entertainment.
random_paper: 2
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Peel Domain Security
  slug: peel-domain-security
  summary_line: TLSv1.3
slug: peel
tags:
- Company
- Consumer Electronics
- Smart Remote
- Mobile App
- Media and Entertainment
- Smart Home
website: http://www.peel.com/
---
