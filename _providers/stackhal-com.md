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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/stackhal-com/llms/stackhal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stackhal-com-llms.txt
- group: other
  href: https://artifacts.apis.io/stackhal-com/hosts/stackhal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stackhal-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/stackhal-com/security/stackhal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackhal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stackhal.com/
- group: company
  title: ''
  type: Blog
  url: https://stackhal.com/blog
coverage:
  checked: '2026-10-31'
  detail: StackHal offers only client‑side developer utilities and does not provide a public API.
  evidence:
  - status: 200
    url: https://stackhal.com/
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: StackHal provides a suite of free, browser‑based developer utilities focused on technical SEO, GEO readiness, Apple Wallet PKPass inspection, Caddy configuration transpilation, email and DNS security checks, and CIDR subnet visualization. The tools run client‑side without registration, offering instant analysis of websites, domains, and server configs while respecting privacy. StackHal’s mission is to empower developers with quick, no‑signup diagnostics for modern web infrastructure.
image: https://stackhal.com/og-image.jpg
layout: provider
modified: '2026-10-31'
name: stackhal-com
nav: Providers
network: true
overview: 'stackhal-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, SEO, Infrastructure, and Open Source.


  stackhal-com''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 9
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
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stackhal Com Domain Security
  slug: stackhal-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: stackhal-com
tags:
- Company
- Developer Tools
- SEO
- Infrastructure
- Open Source
website: https://stackhal.com/
---
