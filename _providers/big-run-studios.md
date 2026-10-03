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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/big-run-studios/refs/heads/main/hosts/big-run-studios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/big-run-studios-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bigrunstudios.com/tos/
- group: company
  title: ''
  type: Newsroom
  url: https://bigrunstudios.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/big-run-studios/refs/heads/main/security/big-run-studios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/big-run-studios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigrunstudios.com
- group: company
  title: ''
  type: Blog
  url: https://bigrunstudios.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://bigrunstudios.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bigrunstudios.com/privacy
- group: company
  title: ''
  type: AboutUs
  url: https://bigrunstudios.com/about-us/
coverage:
  checked: '2026-09-28'
  detail: No documentation host or machine‑readable API specification was found on bigrunstudios.com.
  evidence:
  - status: 200
    url: https://bigrunstudios.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Big Run Studios is a mobile game developer focused on creating cutting edge, casual competitive games for traditionally underserved audiences. Their portfolio includes titles such as Blackout Bingo, Big Cooking, Big Run Solitaire, and more, offering real‑cash rewards and social competition across iOS and Android platforms.
image: https://www.bigrunstudios.com/wp-content/uploads/2020/11/banner@3x.png
layout: provider
modified: '2026-09-28'
name: Big Run Studios
nav: Providers
network: true
overview: 'Big Run Studios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Mobile, Casual, and Underserved.


  Big Run Studios'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Big Run Studios Domain Security
  slug: big-run-studios-domain-security
  summary_line: TLSv1.3
slug: big-run-studios
tags:
- Company
- Gaming
- Mobile
- Casual
- Underserved
website: https://bigrunstudios.com
---
