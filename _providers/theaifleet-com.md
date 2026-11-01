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
  href: https://artifacts.apis.io/theaifleet-com/hosts/theaifleet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theaifleet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/theaifleet-com/vendors/theaifleet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/theaifleet-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aifleet.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theaifleet
- group: auth
  href: https://artifacts.apis.io/theaifleet-com/security/theaifleet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theaifleet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aifleet.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aifleet.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://aifleet.com/contact
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://theaifleet.com/mcp
  - status: 200
    url: https://theaifleet.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: AI Fleet is a technology-driven trucking company that leverages AI and advanced planning software to improve driver pay, reduce dwell times, and increase revenue for carriers. The platform offers a driver‑focused experience with reliable schedules, transparent earnings, and fleet‑backed support, aiming to modernize the trucking industry and address driver shortages.
image: http://static1.squarespace.com/static/63979be84dc550258986aafb/t/63e3f26a6872726aacd94866/1675883114541/Aifleet+Social+Sharing+Logo.png?format=1500w
layout: provider
modified: '2026-10-22'
name: AI Fleet
nav: Providers
network: true
overview: AI Fleet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trucking, AI, Logistics, and Transportation.
random_paper: 23
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Theaifleet Com Domain Security
  slug: theaifleet-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: theaifleet-com
tags:
- Company
- Trucking
- AI
- Logistics
- Transportation
website: https://aifleet.com
---
