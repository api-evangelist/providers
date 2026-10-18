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
- description: API for Bustle Digital Group services (not publicly documented).
  name: Bustle Digital Group API
  slug: bustle-digital-group-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bustle-digital-group/refs/heads/main/hosts/bustle-digital-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bustle-digital-group-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bustle-digital-group/refs/heads/main/vendors/bustle-digital-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bustle-digital-group-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bdg.com/info/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bdg.com/info/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.bdg.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bustle-digital-group/refs/heads/main/security/bustle-digital-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bustle-digital-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bdg.com
coverage:
  checked: '2026-10-06'
  detail: Probing known API host api.bdg.com returned 404 for common OpenAPI paths, and no documentation host is identified.
  evidence:
  - status: 404
    url: https://api.bdg.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Bustle Digital Group is a digital media company that operates a portfolio of online brands, including Bustle, Elite Daily, Mic, and others. It creates content across lifestyle, news, entertainment, and culture, reaching millions of readers worldwide. The company leverages data-driven storytelling and social media distribution to engage audiences and offers advertising solutions for brands.
image: https://imgix.bustle.com/uploads/image/2026/3/12/1b21221c/bdg_2026_share.png?w=1200&h=630&fit=crop&crop=faces&fm=jpg
layout: provider
modified: '2026-10-06'
name: Bustle Digital Group
nav: Providers
network: true
overview: Bustle Digital Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Digital, Publishing, Advertising, and Lifestyle.
random_paper: 12
score:
  band: minimal
  composite: 9.0
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
    developer_ergonomics: 0.0
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bustle Digital Group Domain Security
  slug: bustle-digital-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bustle-digital-group
tags:
- Media
- Digital
- Publishing
- Advertising
- Lifestyle
website: https://www.bdg.com
---
