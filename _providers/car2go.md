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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Car2go (now Free2move) provides car sharing services; the API is documented on the Free2move developer site.
  name: Free2move API
  slug: free2move-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/car2go/refs/heads/main/hosts/car2go-hosts.yml
  title: ''
  type: Hosts
  url: hosts/car2go-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/car2go/refs/heads/main/vendors/car2go-vendors.yml
  title: ''
  type: Vendors
  url: vendors/car2go-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dev.free2move.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/car2go/refs/heads/main/security/car2go-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/car2go-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.free2move.com
coverage:
  checked: '2026-10-07'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.dev.free2move.rent/fr-FR/reserver-une-voiture
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Car2go was a car‑sharing service founded by Daimler in 2008, operating in numerous cities across Europe and North America. It allowed users to locate, reserve, and unlock vehicles via a mobile app, charging by the minute. Over its lifespan, Car2go amassed millions of members and a fleet of thousands of Smart, Mercedes‑Benz, BMW, Mini, and other vehicles. In 2019, Car2go merged with DriveNow to form Share Now, and the service was gradually discontinued in North America by 2020, with remaining European operations winding down later.
image: https://www.free2move.com/assets/strapi/free2move_og_image_7589f4601b.jpg
layout: provider
modified: '2026-10-06'
name: Car2go
nav: Providers
network: true
overview: 'Car2go is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Car Sharing, Mobility, Daimler, ShareNow, and Europe.


  Car2go''s developer surface includes documentation and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Car2Go Domain Security
  slug: car2go-domain-security
  summary_line: TLSv1.3 · DMARC
slug: car2go
tags:
- Car Sharing
- Mobility
- Daimler
- ShareNow
- Europe
website: https://www.free2move.com
---
