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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/extreme-ip-lookup/hosts/extreme-ip-lookup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/extreme-ip-lookup-hosts.yml
- group: auth
  href: https://artifacts.apis.io/extreme-ip-lookup/security/extreme-ip-lookup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/extreme-ip-lookup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://extreme-ip-lookup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://extreme-ip-lookup.com/
- group: docs
  title: ''
  type: APIReference
  url: https://extreme-ip-lookup.com/json/?key=demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://extreme-ip-lookup.com/terms-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://extreme-ip-lookup.com/terms-privacy
- group: operate
  title: ''
  type: Support
  url: mailto:info@extreme-ip-lookup.com
coverage:
  checked: '2026-10-26'
  detail: The provider offers an API but does not publish any machine‑readable contract such as OpenAPI, AsyncAPI, GraphQL SDL, gRPC proto or WSDL.
  evidence:
  - status: 200
    url: https://extreme-ip-lookup.com/json/?key=demo
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Extreme IP Lookup provides a geolocation API that returns detailed information about IP addresses, including type (Business, Education, Residential), name, and associated website when available. Users can retrieve data in JSON, JSONP, or CSV formats via simple HTTP GET requests. An API key is required for access, obtainable through a subscription package. The service is operated from Amsterdam, Netherlands and emphasizes privacy and data security.
image: https://extreme-ip-lookup.com/img/extreme-ip-lookup.com.eipl-wide-share-ogimage.png
layout: provider
modified: '2026-10-26'
name: Extreme IP Lookup
nav: Providers
network: true
overview: 'Extreme IP Lookup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geolocation, IP, API, and Data.


  Extreme IP Lookup''s developer surface includes documentation, API reference, support, and 5 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Extreme Ip Lookup Domain Security
  slug: extreme-ip-lookup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: extreme-ip-lookup
tags:
- Company
- Geolocation
- IP
- API
- Data
- Netherlands
website: https://extreme-ip-lookup.com/
---
