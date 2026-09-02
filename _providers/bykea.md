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
artifact_total: 2
common:
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bykea-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bykea-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bykea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bykea.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bykea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bykea.com
created: '2026-07-17'
description: Bykea is a Karachi-based Pakistani mobility and logistics super-app that offers app-hailed motorbike rides, on-demand parcel and food delivery, cash pickup and drop-off, and digital payments across major Pakistani cities. It connects a large network of motorbike captains with riders and merchants, positioning itself as a low-cost transport, last-mile logistics, and financial services platform for the mass market. Backed by Prosus Ventures (Naspers), Bykea was added to the API Evangelist network as a mobility-sector portfolio lead; this profile has been enriched with the provider's public security surface (a live RFC 9116 security.txt and a HackerOne bug bounty program) and domain-security posture. No public developer portal, OpenAPI, or partner API documentation is exposed - the primary web surface sits behind Cloudflare bot protection.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bykea.png
layout: provider
modified: '2026-07-18'
name: Bykea
nav: Providers
network: true
overview: Bykea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Logistics, Delivery, and Ride Hailing.
random_paper: 20
score:
  band: minimal
  composite: 4.3
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
    operational_transparency: 10.5
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Bykea Domain Security
  slug: bykea-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bykea Vulnerability Disclosure
  slug: bykea-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bykea
tags:
- Company
- Mobility
- Logistics
- Delivery
- Ride Hailing
- Payments
- Pakistan
website: https://bykea.com
---
