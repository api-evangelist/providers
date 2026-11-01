---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for NIU platform accessible via portal.niu.com (requires authentication)
  name: NIU Portal API
  slug: niu-portal-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/niu/llms/niu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/niu-llms.txt
- group: agent
  href: https://artifacts.apis.io/niu/well-known/niu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/niu-well-known.yml
- group: other
  href: https://artifacts.apis.io/niu/hosts/niu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/niu-hosts.yml
- group: other
  href: https://artifacts.apis.io/niu/vendors/niu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/niu-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://global.niu.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.niu.com/
- group: auth
  href: https://artifacts.apis.io/niu/security/niu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/niu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://niu.com/
- group: company
  title: ''
  type: Blog
  url: https://global.niu.com/en-us/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.niu.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://global.niu.com/contact
coverage:
  checked: '2026-10-28'
  detail: API endpoints require authentication and redirect to a login page (302 response)
  evidence:
  - status: 302
    url: https://portal.niu.com/api/v1/customers
  reason: partner-login
  state: gated
created: '2026-10-28'
description: NIU is a global brand focused on urban electric mobility, designing, manufacturing and selling smart electric scooters, e‑bikes and related accessories. The company emphasizes technology, style and sustainability, offering a portfolio that includes the NQi, MQi, UQi, RQi, XQi, BQi and KQi series. NIU operates a worldwide dealer network, provides warranty and service support, and maintains a consumer‑focused app for vehicle monitoring and anti‑theft features. Its products target commuters, campus users and recreational riders, aiming to make electric transportation accessible and enjoyable.
image: https://global.niu.com/assets/icons/icon_512x512.png
layout: provider
modified: '2026-10-28'
name: NIU
nav: Providers
network: true
overview: 'NIU is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include electric-vehicles, scooters, e-bikes, mobility, and technology.


  NIU''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Niu Domain Security
  slug: niu-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: niu
tags:
- electric-vehicles
- scooters
- e-bikes
- mobility
- technology
- company
website: https://niu.com/
---
