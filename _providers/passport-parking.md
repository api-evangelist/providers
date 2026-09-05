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
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Quote, create, and stop parking sessions on behalf of a driver in a Passport-managed zone - the core surface behind facilitating a paid parking session from a parking app, navigation app, or in-car ex
  name: Passport Parking Sessions and Quotes API
  slug: passport-parking-sessions-quotes-api
- description: Determine the parking rate for a location and duration. Rates are defined uniquely by each Passport customer (city, university, or operator) and vary by location, time, and rules, giving partners a si
  name: Passport Parking Rates API
  slug: passport-parking-rates-api
- description: Bulk export of the parking environment. Returns a single-use URL to download a JSON file describing zones, zone numbers, geolocation (latitude and longitude), and associated rules and restrictions for
  name: Passport Parking Environment Export API
  slug: passport-parking-environment-export-api
- description: Versioned JSON schemas for the parking events Passport emits to partners (for example a parking_session_started event, v3.0.0). These are server-to-endpoint webhook-style event payloads that let partn
  name: Passport Parking Event Schemas
  slug: passport-parking-event-schemas
- description: Manage enforcement immobilizations (vehicle boots) - for example updating an existing immobilization record - as part of Passport's digital parking enforcement and compliance workflow. Part of the bro
  name: Passport Immobilizations API
  slug: passport-immobilizations-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/passport-parking-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passport-parking-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/passport-labs
- group: company
  title: ''
  type: Website
  url: https://www.passportinc.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.passportinc.com/
- group: commercial
  title: ''
  type: Plans
  url: https://www.passportinc.com/resources/partnerships/
- group: company
  title: ''
  type: Blog
  url: https://www.passportinc.com/feed/
created: '2026-07-03'
description: Passport (Passport Labs) is a mobility management platform for cities, universities, and agencies, covering digital parking payments, enforcement, permits, and curbside management, and is used by 800+ agencies. Passport exposes a partner developer program at developer.passportinc.com whose REST APIs let parking apps, navigation apps, in-car infotainment, and mobility/POS systems create and stop parking sessions, quote and determine rates, bulk-export the parking environment (zones, spaces, rules), receive parking event schemas, and manage enforcement immobilizations. Rates and rules are configured once by Passport's customers and pushed to payment providers via API. Access is gated - partners register an application, are issued OAuth client credentials by Passport's identity provider, and only authenticated partner applications may call the public APIs. No SDK is required. Commercial terms are partnership / agency-contract based rather than publicly listed self-serve pricing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/passport-parking.png
layout: provider
modified: '2026-07-03'
name: Passport
nav: Providers
network: true
overview: 'Passport publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, Mobility, Smart Cities, Payments, and Enforcement.


  Passport''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passport-parking/refs/heads/main/screenshots/passport-parking-2026-08-07T191541.png
security:
- kind: domain-security
  name: Passport Parking Domain Security
  slug: passport-parking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Passport Parking Trust Center
  slug: passport-parking-trust-center
  summary_line: SOC 2, PCI DSS
slug: passport-parking
tags:
- Parking
- Mobility
- Smart Cities
- Payments
- Enforcement
- Curbside Management
- Transportation
website: https://www.passportinc.com
---
