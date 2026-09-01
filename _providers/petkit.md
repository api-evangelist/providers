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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://petkit.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/petkit-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petkit-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/petkit-packages.yml
created: '2026-07-17'
description: PetKit is a consumer smart pet-technology company that designs and sells connected pet-care hardware — automated feeders, smart water fountains, self-cleaning litter boxes, cameras, and health-monitoring accessories — paired with the PetKit mobile app that controls the devices over the cloud. It was surfaced as a portfolio company of the venture firm qiming and added to the API Evangelist network as a stub for enrichment. As of this enrichment pass, PetKit publishes no dedicated first-party developer portal or public API; petkit.com is operated as a Shopify storefront, so the only machine discoverable surface on the domain is Shopify's Customer Account OAuth/OIDC discovery documents. Third-party (community, reverse-engineered) integrations exist for the mobile-app backend but there is no officially documented API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petkit.png
layout: provider
modified: '2026-07-20'
name: petkit
nav: Providers
network: true
overview: petkit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pet Tech, Smart Home, Internet of Things, and Consumer Electronics.
random_paper: 6
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Petkit Domain Security
  slug: petkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: petkit
tags:
- Company
- Pet Tech
- Smart Home
- Internet of Things
- Consumer Electronics
- E-Commerce
website: https://petkit.com
---
