---
access_model:
  confidence: low
  gated: partner
  gated_source:
  - tag:Partner Gated
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Start, stop, extend, and query active and historical parking sessions across pay-station, mobile-app, and permit channels, and expose real-time session state to enforcement and occupancy consumers. En
  name: Flowbird HUB Parking Sessions API
  provenance: modeled
  slug: flowbird-hub-parking-sessions-api
- description: 'Configure and read parking tariffs, pricing rules, and rights (digital permits, subscriptions, and eligibility) consistently across every sales channel. Flowbird documents that tariffs and rights can '
  name: Flowbird HUB Tariffs and Rights API
  provenance: modeled
  slug: flowbird-hub-tariffs-rights-api
- description: Retrieve the inventory, configuration, health/status, and collection (coin, card, and cash) data for Flowbird pay stations and terminals managed by the central platform. Endpoints are modeled from Flo
  name: Flowbird HUB Pay Stations API
  provenance: modeled
  slug: flowbird-hub-pay-stations-api
- description: Read parking and mobility payment transactions and revenue/reporting data across channels for reconciliation and analytics, with role-based access and ownership filters. Endpoints are modeled from Flo
  name: Flowbird HUB Transactions API
  provenance: modeled
  slug: flowbird-hub-transactions-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/flowbird/hosts/flowbird-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flowbird-hosts.yml
- group: build
  href: https://artifacts.apis.io/flowbird/integrations/flowbird-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/flowbird-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/flowbird/vendors/flowbird-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flowbird-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flowbird.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flowbird.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.flowbird.com/media/podcasts/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flowbirdhub.com/#getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flowbirdhub.com/
- group: auth
  href: https://artifacts.apis.io/flowbird/security/flowbird-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowbird-domain-security.yml
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
coverage:
  checked: '2026-10-20'
  detail: The Flowbird HUB API reference lives in a Stoplight workspace at docs.flowbirdhub.com that shows only the unedited Stoplight template to anonymous visitors, with no public projects, and access is routed through the Customer & Partner Access page.
  evidence:
  - status: 200
    url: https://docs.flowbirdhub.com/explore
  - status: 404
    url: https://docs.flowbirdhub.com/api/v1/projects
  - status: 200
    url: https://www.flowbird.com/customer-partner-access/
  reason: customer-only-docs
  state: gated
created: '2026-07-03'
description: Flowbird is a global urban mobility and parking technology company that builds pay stations, mobile parking apps, digital permits, EV charging, and transit ticketing systems for cities and transport authorities worldwide. Flowbird was acquired by EasyPark Group in an acquisition that closed in January 2025. Its integration surface is the Flowbird HUB, an open platform that exposes documented but partner/agency-gated APIs (OAuth2 and client-certificate secured, with role-based access control and ownership filters) for tariffs, rights/permits, parking sessions, pay stations, and transactions. There is no self-service public sign-up; access is granted to cities, transport agencies, and integration partners under contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flowbird.png
layout: provider
modified: '2026-07-03'
name: Flowbird
nav: Providers
network: true
overview: 'Flowbird is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, Urban Mobility, Transit Ticketing, Payments, and Smart City.


  Flowbird''s developer surface includes getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 63.4
    operational_transparency: 0.0
  previous_composite: 17.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flowbird/flowbird-2026-07-25T214835.png
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
website: https://www.flowbird.group
---
