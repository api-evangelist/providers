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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Hapag-Lloyd''s API Portal exposes container shipping APIs covering container tracking and tracing, vessel schedules, point-to-point routings, booking submission, and shipment status events. APIs targe
  name: Hapag-Lloyd API Portal
  slug: hapag-lloyd-api-portal
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hapag-lloyd-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hapag-Lloyd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hapag-lloyd-ag
- group: company
  title: ''
  type: Website
  url: https://www.hapag-lloyd.com/
- group: start
  title: ''
  type: Portal
  url: https://api-portal.hlag.com/
created: '2026-05-05'
description: A German multinational container shipping company and one of the world's largest liner shipping companies. Operates a fleet of over 250 vessels serving approximately 600 ports across 130 countries with a focus on quality and reliability. Provides a public API portal (api-portal.hlag.com) exposing container tracking, schedule, and booking APIs to customers, partners, and logistics platforms.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hapag-lloyd.png
layout: provider
modified: '2026-05-16'
name: Hapag-Lloyd
nav: Providers
network: true
overview: 'Hapag-Lloyd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Maritime, Shipping, Container Logistics, and Supply Chain.


  Hapag-Lloyd''s developer surface includes developer portal and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.2
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
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hapag-lloyd/refs/heads/main/screenshots/hapag-lloyd-2026-06-20T182512.png
security:
- kind: domain-security
  name: Hapag Lloyd Domain Security
  slug: hapag-lloyd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hapag-lloyd
tags:
- Maritime
- Shipping
- Container Logistics
- Supply Chain
website: https://www.hapag-lloyd.com/
---
