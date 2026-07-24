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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 97
  human_in_the_loop: 0
  name: Bolt Eu Agentic Access
  operation_count: 97
  slug: bolt-eu-agentic-access
  summary_line: 97 operations · 97 acting
api_count: 4
apis:
- description: Partner-gated fleet integration for companies operating driver fleets on the Bolt ride-hailing platform. Fleet owners can generate API credentials (Client ID and Secret) under Settings > API in the Bo
  name: Bolt Fleet API
  slug: bolt-eu-fleet-api
- description: The GenericClient API from Bolt — 17 operation(s) for genericclient.
  name: Bolt GenericClient API
  slug: bolt-eu-genericclient-api
- description: The Pim API from Bolt — 27 operation(s) for pim.
  name: Bolt Pim API
  slug: bolt-eu-pim-api
- description: The ValidateLoyaltyCard API from Bolt — 1 operation(s) for validateloyaltycard.
  name: Bolt ValidateLoyaltyCard API
  slug: bolt-eu-validateloyaltycard-api
artifact_total: 10
common:
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
created: '2026-07-11'
description: Bolt (bolt.eu) is the Estonian mobility super-app operating ride-hailing, ride booking, scooter and e-bike rentals, car-sharing, and food and grocery delivery across 50+ countries in Europe and Africa. This is NOT Bolt the US checkout/payments company (bolt.com). Bolt does not offer a public ride-booking API - the company states it has no public or private APIs for ride-hailing, and business ride booking happens through the Ride Booker web tool and private travel-platform partnerships. Its documented developer surface at developer.bolt.eu is partner-gated and covers the delivery side of the platform - Food, Stores, and Delivery APIs for POS, menu, order, warehouse, and PIM integration - plus a fleet API whose credentials are issued in the Fleet Portal but whose endpoints are not publicly documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolt-eu.png
layout: provider
modified: '2026-07-11'
name: Bolt
nav: Providers
network: true
overview: 'Bolt publishes 3 APIs on the [APIs.io](https://apis.io/) network: GenericClient API, Pim API, and ValidateLoyaltyCard API. Tagged areas include Ride Booking, Ride Hailing, Mobility, Transportation, and Food Delivery.


  Bolt''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Bolt Eu Plans Pricing
  plan_count: 3
  slug: bolt-eu-plans-pricing
random_paper: 33
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.6
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
