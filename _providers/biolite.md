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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Biolite exposes a GraphQL API via Shopify storefront, but ownership could not be verified.
  name: Biolite API
  slug: biolite-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biolite/refs/heads/main/llms/biolite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biolite-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biolite/refs/heads/main/well-known/biolite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biolite-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biolite/refs/heads/main/hosts/biolite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biolite-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biolite/refs/heads/main/vendors/biolite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biolite-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bioliteenergy.com/pages/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.bioliteenergy.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bioliteenergy.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bioliteenergy.com/blogs/press
- group: company
  title: ''
  type: Blog
  url: https://blog.bioliteenergy.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.bioliteenergy.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biolite/refs/heads/main/security/biolite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biolite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bioliteenergy.com
created: '2026-09-28'
description: BioLite is a New York City‑based startup that creates off‑grid energy products for outdoor recreation and emerging markets. Founded in 2006, it designs wood‑burning stoves that generate electricity via thermoelectric technology, along with solar lighting, portable power stations, and rechargeable lanterns. The company’s mission is to bring clean, reliable energy to people everywhere, supporting sustainable living and empowering communities.
image: http://www.bioliteenergy.com/cdn/shop/files/BIoLite_Logo_Black_c027a27d-d0b2-4079-a551-5f23685e5da9_1200x628_pad_f5f5f5.png?v=1688072811
layout: provider
modified: '2026-09-28'
name: Biolite
nav: Providers
network: true
overview: 'Biolite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Lighting, Portable Power, Cooking, Outdoor Gear, and Home Backup.


  Biolite''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biolite Domain Security
  slug: biolite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biolite
tags:
- Lighting
- Portable Power
- Cooking
- Outdoor Gear
- Home Backup
website: https://www.bioliteenergy.com
---
