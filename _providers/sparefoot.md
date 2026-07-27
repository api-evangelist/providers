---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparefoot-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sparefoot
- group: company
  title: ''
  type: Website
  url: https://www.sparefoot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.sparefoot.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sparefoot-plans-pricing.yml
created: '2026-07-03'
description: SpareFoot is the largest online marketplace for finding and reserving self-storage units, owned by Storable (the same parent that owns the storEDGE and SiteLink property-management systems, cataloged separately at api-evangelist/storable). SpareFoot itself does not publish a developer portal, API reference, or self-serve API keys for third parties to call. Instead, storage facilities' pricing, unit availability, and promotions reach SpareFoot through one-way, partner-gated data-feed integrations built by property-management software vendors - Storable Edge (storEDGE), SiteLink Web Edition, Storable Easy, Self Storage Manager (E-SoftSys), eDOMICO, and DoorSwap - each of which pushes its own facilities' inventory into the marketplace and receives reservation/lead data back. No endpoint list, request/response schema, or authentication scheme for this feed mechanism is publicly documented; a facility operator or software vendor must go through SpareFoot/Storable's integrations team
  to be onboarded. This entry documents that access model honestly rather than fabricating an API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sparefoot.png
layout: provider
modified: '2026-07-03'
name: SpareFoot
nav: Providers
network: true
overview: 'SpareFoot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Self Storage, Marketplace, Storage Unit Listings, Lead Generation, and Reservations.


  SpareFoot''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Sparefoot Plans Pricing
  plan_count: 2
  slug: sparefoot-plans-pricing
random_paper: 27
score:
  band: minimal
  composite: 12.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Sparefoot Domain Security
  slug: sparefoot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sparefoot
tags:
- Self Storage
- Marketplace
- Storage Unit Listings
- Lead Generation
- Reservations
- Partner Integration
- Data Feed
- Storable
- SiteLink
- storEDGE
website: https://www.sparefoot.com/
---
