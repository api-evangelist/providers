---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vetstoria-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vetstoria
- group: company
  title: ''
  type: Website
  url: https://www.vetstoria.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.vetstoria.com/integrations/
- group: company
  title: ''
  type: Partners
  url: https://www.vetstoria.com/partners/
- group: commercial
  title: ''
  type: Plans
  url: https://www.vetstoria.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.vetstoria.com/blog/
created: '2026-07-03'
description: Vetstoria provides real-time online appointment booking, veterinary websites, and online payments for veterinary practices, integrating in real time with 40+ practice management systems (PIMS) - including ezyVet, IDEXX Neo, IDEXX Cornerstone, IDEXX Animana, Covetrus Ascend, AVImark, RxWorks, visionVPM, Provet Cloud, OpenVPMS, and others - to sync availability, prevent double-bookings, and match clients and pets back into the PIMS. Founded in 2015 and used by more than 5,000 practices worldwide (operating as PetDesk Direct Booking in the United States), Vetstoria does NOT publish a public, self-service developer API. Its integration surface is partner-gated - software vendors connect through a contact-based Integrations Partner program, and each PIMS integration is typically driven from the PIMS side (for example, ezyVet exposes Vetstoria as an "API Partner" and IDEXX Neo auto-generates an API key when the Vetstoria connection is enabled). No public API reference, developer portal,
  OpenAPI definition, or documented WebSocket exists as of this cataloging.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vetstoria.png
layout: provider
modified: '2026-07-03'
name: Vetstoria
nav: Providers
network: true
overview: 'Vetstoria is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Veterinary, Online Booking, Appointment Scheduling, Practice Management, and PIMS Integration.


  Vetstoria''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 99
score:
  band: minimal
  composite: 5.7
  delta: -1.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Vetstoria Domain Security
  slug: vetstoria-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vetstoria
tags:
- Veterinary
- Online Booking
- Appointment Scheduling
- Practice Management
- PIMS Integration
- Healthcare
- Payments
- Partner API
website: https://www.vetstoria.com
---
