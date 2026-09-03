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
api_count: 4
apis:
- description: Start, stop, extend, and query active and historical parking sessions across pay-station, mobile-app, and permit channels, and expose real-time session state to enforcement and occupancy consumers. En
  name: Flowbird HUB Parking Sessions API
  slug: flowbird-hub-parking-sessions-api
- description: 'Configure and read parking tariffs, pricing rules, and rights (digital permits, subscriptions, and eligibility) consistently across every sales channel. Flowbird documents that tariffs and rights can '
  name: Flowbird HUB Tariffs and Rights API
  slug: flowbird-hub-tariffs-rights-api
- description: Retrieve the inventory, configuration, health/status, and collection (coin, card, and cash) data for Flowbird pay stations and terminals managed by the central platform. Endpoints are modeled from Flo
  name: Flowbird HUB Pay Stations API
  slug: flowbird-hub-pay-stations-api
- description: Read parking and mobility payment transactions and revenue/reporting data across channels for reconciliation and analytics, with role-based access and ownership filters. Endpoints are modeled from Flo
  name: Flowbird HUB Transactions API
  slug: flowbird-hub-transactions-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flowbird-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flowbird
- group: company
  title: ''
  type: Website
  url: https://www.flowbird.group
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flowbirdhub.com/
- group: company
  title: ''
  type: PartnerAccess
  url: https://www.flowbird.com/customer-partner-access/
- group: company
  title: ''
  type: Blog
  url: https://www.flowbird.com/news/
created: '2026-07-03'
description: Flowbird is a global urban mobility and parking technology company that builds pay stations, mobile parking apps, digital permits, EV charging, and transit ticketing systems for cities and transport authorities worldwide. Flowbird was acquired by EasyPark Group in an acquisition that closed in January 2025. Its integration surface is the Flowbird HUB, an open platform that exposes documented but partner/agency-gated APIs (OAuth2 and client-certificate secured, with role-based access control and ownership filters) for tariffs, rights/permits, parking sessions, pay stations, and transactions. There is no self-service public sign-up; access is granted to cities, transport agencies, and integration partners under contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flowbird.png
layout: provider
modified: '2026-07-03'
name: Flowbird
nav: Providers
network: true
overview: 'Flowbird publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, Urban Mobility, Transit Ticketing, Payments, and Smart City.


  Flowbird''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flowbird/refs/heads/main/screenshots/flowbird-2026-07-25T214835.png
security:
- kind: domain-security
  name: Flowbird Domain Security
  slug: flowbird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flowbird
tags:
- Parking
- Urban Mobility
- Transit Ticketing
- Payments
- Smart City
- Pay Stations
- EV Charging
- Digital Permits
- Partner Gated
website: https://www.flowbird.group
---
