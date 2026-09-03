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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osyva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osyva.com
created: '2026-07-17'
description: Osyva is a B2B commerce and procurement platform for the veterinary supply sector in Colombia and Latin America ("Gestiona tus compras veterinarias"), connecting veterinary clinics, distributors, and buyers to manage the ordering and purchasing of veterinary products and pharmaceuticals. Backed by 500 Global, Osyva runs a web and mobile application (osyva.com, osyva2go.com) and the related Hubu brand (hubu.com.co). Its platform is powered by internal API hosts (api.osyva.com, api.osyva2go.com), but as of this profile it publishes no public developer portal, documentation, or API specification, so its API surface is private.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/osyva.png
layout: provider
modified: '2026-07-20'
name: Osyva
nav: Providers
network: true
overview: Osyva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Veterinary, B2B Commerce, Procurement, and E-Commerce.
random_paper: 16
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/osyva/refs/heads/main/screenshots/osyva-2026-08-07T191021.png
security:
- kind: domain-security
  name: Osyva Domain Security
  slug: osyva-domain-security
  summary_line: no transport/DNS hardening detected
slug: osyva
tags:
- Company
- Veterinary
- B2B Commerce
- Procurement
- E-Commerce
- Distribution
- AgTech
- Latin America
- Colombia
website: https://osyva.com
---
