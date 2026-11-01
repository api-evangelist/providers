---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: 'SOAP web service. Creates shipments and skybills (labels), single and multi-parcel, with reservation and ESD (pickup) variants, routing and pickup booking/cancellation. 38 operations in the published '
  name: Chronopost Shipping Web Service
  slug: shipping
- description: SOAP web service. Tracks skybills by number or sender reference, searches proof of delivery, and cancels skybills. 9 operations in the published WSDL.
  name: Chronopost Tracking Web Service
  slug: tracking
- description: SOAP web service. Quotes shipping prices, lists products available for a route and calculates delivery times. 6 operations in the published WSDL.
  name: Chronopost QuickCost Web Service
  slug: quickcost
- description: SOAP web service. Searches Chronopost relay (Pickup) points and agencies by postcode, coordinates, ID and service, and delivery rounds. 19 operations in the published WSDL.
  name: Chronopost Point Relais Web Service
  slug: pointrelais
- description: SOAP web service. Searches and confirms delivery time slots (appointment delivery) and geocodes addresses. 4 operations in the published WSDL.
  name: Chronopost Creneau Web Service
  slug: creneau
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/chronopost/hosts/chronopost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chronopost-hosts.yml
- group: other
  href: https://artifacts.apis.io/chronopost/vendors/chronopost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chronopost-vendors.yml
- group: build
  href: https://artifacts.apis.io/chronopost/packages/chronopost-packages.yml
  title: ''
  type: SDKs
  url: packages/chronopost-packages.yml
- group: build
  href: https://artifacts.apis.io/chronopost/packages/chronopost-packages.yml
  title: ''
  type: Packages
  url: packages/chronopost-packages.yml
- group: auth
  href: https://artifacts.apis.io/chronopost/security/chronopost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chronopost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chronopost.fr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chronopost.fr/fr/conditions-generales-utilisation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chronopost.fr/fr/politique-informatique-et-libertes
- group: operate
  title: ''
  type: Support
  url: https://www.chronopost.fr/fr/aide
- group: start
  title: ''
  type: SignUp
  url: https://www.chronopost.fr/fr/se-creer-un-compte
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chronopost.fr/fr/tarif-envoi-colis
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.chronopost.fr/fr/divulgation-de-vulnerabilites
- group: company
  title: ''
  type: Blog
  url: https://www.chronopost-presse.fr/
- group: company
  title: ''
  type: LinkedIn
  url: https://fr.linkedin.com/company/chronopost
- group: other
  title: ''
  type: X
  url: https://twitter.com/Chronopost
created: '2026-10-13'
description: 'Chronopost is the French express parcel and courier carrier of the La Poste group (DPDgroup), delivering business and consumer parcels across France, its overseas departments and internationally, with Pickup relay points and Shop2Shop. For business customers it publishes public SOAP web services at ws.chronopost.fr, each with a live WSDL: Shipping (label/skybill creation and pickup booking, 38 operations), Tracking (tracking, proof of delivery and cancellation, 9), QuickCost (pricing and delivery-time quotes, 6), PointRelais (relay point and agency search, 19) and Creneau (delivery-slot appointment booking, 4). Calls require a Chronopost customer account number and password.'
layout: provider
modified: '2026-10-13'
name: Chronopost
nav: Providers
network: true
overview: 'Chronopost is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Parcel Delivery, and Express Courier.


  Chronopost''s developer surface includes support, signup flow, pricing, engineering blog, and 11 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 67.9
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chronopost Domain Security
  slug: chronopost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chronopost
tags:
- Company
- Shipping
- Logistics
- Parcel Delivery
- Express Courier
- SOAP
- Tracking
- France
website: https://www.chronopost.fr
---
