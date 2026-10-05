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
api_count: 1
apis:
- description: Travel booking API documented on the sandbox portal
  name: AsiaYo API
  slug: asiayo-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asiayo/refs/heads/main/llms/asiayo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asiayo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asiayo/refs/heads/main/hosts/asiayo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asiayo-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asiayo.com/en-us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asiayo.com/en-us/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.asiayo.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asiayo/refs/heads/main/security/asiayo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asiayo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asiayo.com
coverage:
  checked: 2026-09-26
  detail: Sandbox portal renders with JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://sandbox.asiayo.com/en-us/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: AsiaYo is a global travel platform offering bookings for hotels, tours, sports activities, and transportation. It provides a marketplace for travelers to discover and reserve accommodations, group tours, cruises, and day trips worldwide, with multilingual support and member discounts.
image: https://img.asiayo.com/static/images/fb_og.jpg
layout: provider
modified: '2026-09-26'
name: Asiayo
nav: Providers
network: true
overview: 'Asiayo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Marketplace, Booking, Tours, and Hospitality.


  Asiayo''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asiayo Domain Security
  slug: asiayo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asiayo
tags:
- Travel
- Marketplace
- Booking
- Tours
- Hospitality
website: https://asiayo.com
---
