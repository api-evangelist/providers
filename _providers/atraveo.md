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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atraveo/refs/heads/main/hosts/atraveo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atraveo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atraveo/refs/heads/main/vendors/atraveo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atraveo-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://signup.atraveo.com/register
- group: company
  title: ''
  type: Newsroom
  url: https://www.atraveo.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atraveo/refs/heads/main/security/atraveo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atraveo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atraveo.com
coverage:
  checked: 2026-09-26
  detail: API host https://api.atraveo.com returned 403 for OpenAPI attempts, and no documentation host is available.
  evidence:
  - status: 403
    url: https://api.atraveo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atraveo is a European holiday‑home rental platform that connects property owners with guests across dozens of booking portals such as Airbnb, Booking.com and Expedia. It offers a full‑service solution including marketing, payment processing, guest communication and 7‑day payout, charging a 19.5% commission only on successful bookings. Owners can list properties for free, set their own prices and retain control over distribution, while Atraveo handles the operational workload, providing tools, tutorials and support for hosts.
image: https://cdn.hometogo.net/assets/media/pics/1920_auto/6352721ce45d0.jpg
layout: provider
modified: '2026-09-26'
name: Atraveo
nav: Providers
network: true
overview: 'Atraveo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Holiday Rentals, Vacation Homes, Property Management, and Travel.


  Atraveo''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atraveo Domain Security
  slug: atraveo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atraveo
tags:
- Company
- Holiday Rentals
- Vacation Homes
- Property Management
- Travel
website: https://www.atraveo.com
---
