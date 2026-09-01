---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 97
  human_in_the_loop: 0
  name: Bolt Eu Agentic Access
  operation_count: 97
  slug: bolt-eu-agentic-access
  summary_line: 97 operations · 97 acting
api_count: 3
apis:
- description: The GenericClient API from Bolt — 17 operation(s) for genericclient.
  name: Bolt GenericClient API
  slug: bolt-eu-genericclient-api
- description: The Pim API from Bolt — 27 operation(s) for pim.
  name: Bolt Pim API
  slug: bolt-eu-pim-api
- description: The ValidateLoyaltyCard API from Bolt — 1 operation(s) for validateloyaltycard.
  name: Bolt ValidateLoyaltyCard API
  slug: bolt-eu-validateloyaltycard-api
- description: The Bolt Delivery API API from Bolt — 0 operation(s) for bolt delivery api.
  name: Bolt Bolt Delivery API
  slug: bolt-eu-bolt-delivery-api-api
- description: The Bolt Food API API from Bolt — 0 operation(s) for bolt food api.
  name: Bolt Bolt Food API
  slug: bolt-eu-bolt-food-api-api
- description: The Bolt Stores API API from Bolt — 0 operation(s) for bolt stores api.
  name: Bolt Bolt Stores API
  slug: bolt-eu-bolt-stores-api-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bolt Delivery GenericClient API
  slug: open-bolt-eu-genericclient-api
- collection_type: open
  name: Bolt Delivery GenericClient Pim API
  slug: open-bolt-eu-pim-api
- collection_type: open
  name: Bolt Delivery GenericClient ValidateLoyaltyCard API
  slug: open-bolt-eu-validateloyaltycard-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bolt-eu-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bolt-eu-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bolt-eu-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bolt-eu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolt-eu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bolt-eu-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bolteu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bolt-eu
- group: company
  title: ''
  type: Website
  url: https://bolt.eu
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bolt.eu/
- group: commercial
  title: ''
  type: Plans
  url: plans/bolt-eu-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://bolt.eu/en/blog/
- group: other
  title: ''
  type: ProductPage
  url: https://fleets.bolt.eu/
created: '2026-07-11'
description: Bolt (bolt.eu) is the Estonian mobility super-app operating ride-hailing, ride booking, scooter and e-bike rentals, car-sharing, and food and grocery delivery across 50+ countries in Europe and Africa. This is NOT Bolt the US checkout/payments company (bolt.com). Bolt does not offer a public ride-booking API - the company states it has no public or private APIs for ride-hailing, and business ride booking happens through the Ride Booker web tool and private travel-platform partnerships. Its documented developer surface at developer.bolt.eu is partner-gated and covers the delivery side of the platform - Food, Stores, and Delivery APIs for POS, menu, order, warehouse, and PIM integration - plus a fleet API whose credentials are issued in the Fleet Portal but whose endpoints are not publicly documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolt-eu.png
layout: provider
modified: '2026-07-25'
name: Bolt
nav: Providers
network: true
overview: 'Bolt publishes 6 APIs on the [APIs.io](https://apis.io/) network, including GenericClient API, Pim API, ValidateLoyaltyCard API, and 3 more. Tagged areas include Ride Booking, Ride Hailing, Mobility, Transportation, and Food Delivery.


  Bolt''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Bolt Eu Plans Pricing
  plan_count: 3
  slug: bolt-eu-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 46.6
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bolt-eu/refs/heads/main/screenshots/bolt-eu-2026-07-25T203541.png
security:
- kind: authentication
  name: Bolt Eu Authentication
  slug: bolt-eu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bolt Eu Domain Security
  slug: bolt-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bolt Eu Vulnerability Disclosure
  slug: bolt-eu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bolt Eu Trust Center
  slug: bolt-eu-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: bolt-eu
tags:
- Ride Booking
- Ride Hailing
- Mobility
- Transportation
- Food Delivery
- Micromobility
- Delivery
- Super App
website: https://bolt.eu
---
