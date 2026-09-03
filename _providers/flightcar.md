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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flightcar-domain-security.yml
created: '2026-07-17'
description: FlightCar was a United States peer-to-peer car-rental marketplace built around airport travel, surfaced into the API Evangelist network as an a16z portfolio lead. Enrichment probing on 2026-07-20 found no operating company behind the name and no API surface of any kind. The domain flightcar.com is registered but publishes no A, AAAA or MX records, resolves to no host, and sits on Njalla privacy nameservers with a SOA serial dated 2026-07-18; the api, developer and docs subdomains do not resolve; there is no GitHub organisation at github.com/flightcar; and no first-party client library exists on npm or PyPI. The Internet Archive shows the consumer site returning 200 through May 2016 and an Internal Server Error by July 2017, with no successful captures in 2017 or 2018. FlightCar is therefore carried in the network as a defunct company retained for portfolio-graph and historical continuity rather than as an active API provider, and should not be re-queued for artifact enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flightcar.png
layout: provider
modified: '2026-07-20'
name: FlightCar
nav: Providers
network: true
overview: FlightCar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Transportation, Travel, and Automotive.
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Flightcar Domain Security
  slug: flightcar-domain-security
  summary_line: no transport/DNS hardening detected
slug: flightcar
tags:
- Company
- Defunct
- Transportation
- Travel
- Automotive
- Car Rental
- Marketplace
- Peer-to-Peer
- Mobility
---
