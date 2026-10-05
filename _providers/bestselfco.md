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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestselfco/refs/heads/main/llms/bestselfco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestselfco-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestselfco/refs/heads/main/well-known/bestselfco-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bestselfco-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestselfco/refs/heads/main/hosts/bestselfco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestselfco-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestselfco/refs/heads/main/vendors/bestselfco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestselfco-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestselfco/refs/heads/main/security/bestselfco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestselfco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestself.co
coverage:
  checked: '2026-09-28'
  detail: The site returns a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://bestself.co
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bestselfco creates personal development tools, planners, journals, and decks aimed at improving productivity, relationships, and personal growth. Their product line includes the BestSelf Planner, Self Journal, Intimacy Deck, and various digital downloads, marketed through their e‑commerce site bestself.co.
image: https://cdn.shopify.com/s/files/1/1015/4487/files/share-image.jpg?v=1748103047
layout: provider
modified: '2026-09-28'
name: Bestselfco
nav: Providers
network: true
overview: Bestselfco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Development, Productivity, Journals, E-Commerce, and Lifestyle.
random_paper: 10
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
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
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestselfco Domain Security
  slug: bestselfco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bestselfco
tags:
- Personal Development
- Productivity
- Journals
- E-Commerce
- Lifestyle
website: https://bestself.co
---
