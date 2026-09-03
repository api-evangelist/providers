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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: A direct system-to-system API that Emirates SkyCargo advertises on its own Digital Booking Channels page, described as connecting a freight forwarder's in-house system for real-time instant booking co
  name: Emirates SkyCargo Host-to-Host API
  slug: emirates-skycargo-host-to-host-api
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.skycargo.com/
- group: start
  title: ''
  type: Portal
  url: https://eskycargo.emirates.com/app/offerandorder/
- group: docs
  title: ''
  type: Documentation
  url: https://www.skycargo.com/my-shipments/digital-booking-channels/
- group: docs
  title: ''
  type: Documentation
  url: https://www.skycargo.com/my-shipments/e-awb/
- group: operate
  title: ''
  type: Support
  url: https://www.skycargo.com/contact-support/
- group: operate
  title: ''
  type: FAQ
  url: https://www.skycargo.com/contact-support/frequently-asked-question-faqs/
- group: learn
  title: ''
  type: Training
  url: https://www.skycargo.com/contact-support/e-skycargo-training/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skycargo.com/website-user-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skycargo.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.skycargo.com/media-centre
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emirates-skycargo
created: '2026-07-30'
description: 'Emirates SkyCargo is the air cargo division of Emirates Airline, headquartered at Dubai International Airport in the United Arab Emirates, moving general freight, pharmaceuticals, perishables, live animals, valuables, mail and courier traffic across a network of more than 140 destinations on six continents using both freighters and passenger-aircraft bellyhold capacity. In the shipment chain it is the airborne carrier leg sitting between the freight forwarder and the ground handler, and it books almost exclusively through intermediaries rather than shippers directly. Its API posture is advertised but not published: Emirates SkyCargo states on its own Digital Booking Channels page that it offers "a direct API connection to your in-house system" covering booking creation, amendments, cancellations and track and trace, yet there is no developer portal, no API reference, no OpenAPI or AsyncAPI document, no base URL and no self-serve signup anywhere on skycargo.com. Access is obtained
  only by emailing SkyCargoAPISupport@emirates.com to negotiate a host-to-host connection, by integrating through the CargoWise transport management system, by submitting Freight Forwarding Requests over EDI, or by booking through the WebCargo, CargoAi, Pelicargo and cargo.one marketplaces, which themselves require IATA/CASS accreditation. The one standard the organization documents on its own surface is IATA e-AWB: agents must sign the IATA Multilateral e-AWB Agreement before submitting FWB and FHL cargo messages over EDI messaging. This is an EDI-and-bilateral-integration carrier with a customer-contract portal veneer, not a public API provider.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emirates-skycargo.png
layout: provider
modified: '2026-07-30'
name: Emirates SkyCargo
nav: Providers
network: true
overview: 'Emirates SkyCargo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, United Arab Emirates, Air Cargo, and Airline.


  Emirates SkyCargo''s developer surface includes developer portal, documentation, support, FAQ, training material, engineering blog, and 5 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 15.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emirates-skycargo/refs/heads/main/screenshots/emirates-skycargo-2026-08-07T164847.png
slug: emirates-skycargo
tags:
- Logistics
- Supply Chain
- United Arab Emirates
- Air Cargo
- Airline
- Freight
- Track and Trace
- EDI
- e-AWB
- Standards
website: https://www.skycargo.com/
---
