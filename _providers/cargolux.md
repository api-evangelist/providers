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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.cargolux.com/
- group: start
  title: ''
  type: CustomerPortal
  url: https://my.cargolux.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargolux.com/customer-service/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargolux.com/your-shipment-s-journey/
- group: other
  title: ''
  type: TrackAndTrace
  url: https://www.cargolux.com/track-and-trace/
- group: other
  title: ''
  type: Schedules
  url: https://www.cargolux.com/flight-scheduler/
- group: other
  title: ''
  type: EAWB
  url: https://www.cargolux.com/your-shipment-s-journey/go-paperless/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cargolux.com/terms-of-use/
- group: other
  title: ''
  type: ConditionsOfCarriage
  url: https://www.cargolux.com/conditions-of-carriage/
- group: other
  title: ''
  type: ConditionsOfContract
  url: https://www.cargolux.com/conditions-of-contract/
- group: commercial
  title: ''
  type: GeneralTermsAndConditions
  url: https://www.cargolux.com/general-terms-and-conditions-of-cargo-sales/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cargolux.com/data-protection/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.cargolux.com/cookie-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.cargolux.com/media/media-releases/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cargolux-airlines/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/CargoluxAirlines
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Cargolux_Intl
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargolux
- group: operate
  title: ''
  type: Contact
  url: https://www.cargolux.com/contact/
created: '2026-07-30'
description: 'Cargolux Airlines International S.A. is Europe''s largest all-cargo airline, headquartered at Luxembourg Findel Airport in Luxembourg and operating a global Boeing 747 freighter network under IATA designator CV and air waybill prefix 172 (with Cargolux Italia on prefix 356). In the logistics chain Cargolux is the main-leg air carrier: it sells capacity to freight forwarders and general sales agents rather than to shippers, hands cargo to terminal and ground handling operators such as its Luxcargo Handling subsidiary, and files customs and security data on behalf of the contracted forwarder. Its API posture is honestly a customer-contract one. Cargolux publishes no developer portal and no machine-readable contract of any kind — developer.cargolux.com, developers.cargolux.com and docs.cargolux.com do not resolve, and /developers, /api, /openapi.json, /swagger.json, /api-docs and /.well-known/ all return 404 on www.cargolux.com. The only public self-service surfaces are HTML:
  a track-and-trace widget and a flight scheduler on the marketing site, plus a login-walled Customer Portal at my.cargolux.com. A real quote-and- booking API exists, but it is a bilateral, commercially negotiated forwarder interface — piloted with Kuehne+Nagel in 2021 and extended to DB Schenker — with no published reference, and it is complemented by indirect distribution through the cargo.one, CargoAi and WebCargo by Freightos marketplaces. Underneath, Cargolux runs IBS Software''s iCargo SaaS cargo management system and holds a large minority stake in Luxembourg''s CHAMP Cargosystems, whose developer.champ.aero portal is the developer surface Cargolux''s ecosystem actually reads — CHAMP''s, not Cargolux''s. IATA e-AWB "Single Process" is documented; no IATA ONE Record or Cargo-XML publication was found.'
layout: provider
modified: '2026-07-30'
name: Cargolux
nav: Providers
network: true
overview: 'Cargolux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, Luxembourg, Air Cargo, and Airlines.


  Cargolux''s developer surface includes documentation, engineering blog, and 17 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 11.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargolux/refs/heads/main/screenshots/cargolux-2026-08-07T163019.png
slug: cargolux
tags:
- Logistics
- Supply Chain
- Luxembourg
- Air Cargo
- Airlines
- Freight
- Track and Trace
- Standards
website: https://www.cargolux.com/
---
