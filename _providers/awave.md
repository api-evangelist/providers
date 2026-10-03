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
  href: https://raw.githubusercontent.com/api-evangelist/awave/refs/heads/main/hosts/awave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awave-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/awave/refs/heads/main/security/awave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.awave.se
- group: company
  title: ''
  type: Blog
  url: https://www.awave.se/blogg/
- group: operate
  title: ''
  type: Support
  url: https://www.awave.se/kontakt/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/awave
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Awave is a Stockholm‑based digital agency offering strategy, creative design, technology development, growth marketing and managed services. They help brands increase visibility, build modern web and app solutions, and provide accessibility consulting. Since 2021 Awave has been part of iO, expanding its expertise across Europe. Their services span digital transformation, SEO, e‑commerce, and custom software, targeting startups to large enterprises.
image: https://www.awave.se/wp-content/uploads/2023/10/awave-logo-share.png
layout: provider
modified: '2026-09-27'
name: Awave
nav: Providers
network: true
overview: 'Awave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Agency, Web Development, Marketing, Accessibility, and Stockholm.


  Awave''s developer surface includes engineering blog, support, and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.8
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
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Awave Domain Security
  slug: awave-domain-security
  summary_line: TLSv1.3 · HSTS
slug: awave
tags:
- Digital Agency
- Web Development
- Marketing
- Accessibility
- Stockholm
website: https://www.awave.se
---
