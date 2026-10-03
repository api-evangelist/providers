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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aurate/refs/heads/main/llms/aurate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurate-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aurate/refs/heads/main/well-known/aurate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aurate-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aurate/refs/heads/main/hosts/aurate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aurate/refs/heads/main/vendors/aurate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurate-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://auratenewyork.com/blogs/news
- group: company
  title: ''
  type: Blog
  url: https://auratenewyork.com/blogs/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aurate/refs/heads/main/security/aurate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auratenewyork.com/
created: '2026-09-26'
description: Aurate New York is a sustainable fine jewelry brand offering ethically sourced, lab‑grown diamond and gemstone pieces. Their collections emphasize eco‑friendly materials, recycled gold, and customizable designs that reflect personal stories and values.
image: http://auratenewyork.com/cdn/shop/t/35/assets/og-image.png?v=57472515067479349441773774059
layout: provider
modified: '2026-09-26'
name: Aurate
nav: Providers
network: true
overview: 'Aurate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Jewelry, Sustainable, Ethical, and E-Commerce.


  Aurate''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aurate Domain Security
  slug: aurate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aurate
tags:
- Company
- Jewelry
- Sustainable
- Ethical
- E-Commerce
website: https://auratenewyork.com/
---
