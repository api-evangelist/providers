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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/battleface/refs/heads/main/llms/battleface-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/battleface-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/battleface/refs/heads/main/hosts/battleface-hosts.yml
  title: ''
  type: Hosts
  url: hosts/battleface-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/battleface/refs/heads/main/vendors/battleface-vendors.yml
  title: ''
  type: Vendors
  url: vendors/battleface-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.battleface.com/en-us/media/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/battleface/refs/heads/main/security/battleface-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/battleface-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.battleface.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.battleface.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.battleface.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.battleface.com
- group: company
  title: ''
  type: Blog
  url: https://www.battleface.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.battleface.com/en-us/benefits/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.battleface.com/en-us/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.battleface.com/en-us/privacy-policy/
coverage:
  checked: '2026-09-27'
  detail: Developer portal at https://developers.battleface.com is a Postman-hosted site that renders documentation via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://developers.battleface.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Battleface provides travel insurance and assistance services for adventurers and everyday travelers worldwide. Founded in the UK, it has expanded to the US, Canada, Australia and beyond, offering single‑trip, multi‑trip and annual plans with 24/7 support, medical evacuation, baggage protection and more. The company emphasizes digital claims, a partner network, and a mission to make travel insurance simple and reliable for customers across the globe.
image: https://www.battleface.com/wp-content/uploads/2024/07/travel-insurance-built-just-for-you.jpg
layout: provider
modified: '2026-09-27'
name: Battleface
nav: Providers
network: true
overview: 'Battleface is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Insurance, Adventure, DigitalClaims, and Global.


  Battleface''s developer surface includes documentation, API reference, engineering blog, pricing, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Battleface Domain Security
  slug: battleface-domain-security
  summary_line: TLSv1.3 · DMARC
slug: battleface
tags:
- Travel
- Insurance
- Adventure
- DigitalClaims
- Global
website: https://www.battleface.com
---
