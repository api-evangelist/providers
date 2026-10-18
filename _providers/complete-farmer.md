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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/complete-farmer/refs/heads/main/hosts/complete-farmer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/complete-farmer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/complete-farmer/refs/heads/main/vendors/complete-farmer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/complete-farmer-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.completefarmer.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/complete-farmer/refs/heads/main/security/complete-farmer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/complete-farmer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.completefarmer.com/
- group: company
  title: ''
  type: Blog
  url: https://www.completefarmer.com/blogs
- group: company
  title: ''
  type: About
  url: https://www.completefarmer.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.completefarmer.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.completefarmer.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.completefarmer.com/terms-and-conditions
coverage:
  checked: '2026-10-10'
  detail: The provider's website does not expose any developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://www.completefarmer.com
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Complete Farmer is an agritech platform connecting African farmers, buyers, and vendors through a data‑driven marketplace. It offers tools for growers to access inputs, expert support, and market access, while enabling buyers to source high‑quality produce. The solution aims to reduce fragmentation in African agriculture, improve supply‑chain transparency, and foster sustainable growth across the continent.
image: https://www.completefarmer.com/images/about/CultureAndValues/Hero-1.png
layout: provider
modified: '2026-10-09'
name: Complete Farmer
nav: Providers
network: true
overview: 'Complete Farmer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AgTech, Marketplace, Africa, and Agriculture.


  Complete Farmer''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Complete Farmer Domain Security
  slug: complete-farmer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: complete-farmer
tags:
- Company
- AgTech
- Marketplace
- Africa
- Agriculture
website: https://www.completefarmer.com/
---
