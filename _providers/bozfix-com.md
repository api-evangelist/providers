---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only public API providing Antalya service data such as categories, verified professionals and price ranges.
  name: BOZFIX Developer API v1
  slug: bozfix-developer-api-v1
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bozfix-com/llms/bozfix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bozfix-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bozfix-com/hosts/bozfix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bozfix-com-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://bozfix.com/blog
- group: auth
  href: https://artifacts.apis.io/bozfix-com/security/bozfix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bozfix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bozfix.com/
coverage:
  checked: '2026-11-03'
  detail: Developer API page provides only HTML documentation and requires an API key, no OpenAPI or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://bozfix.com/api-dokuman.php
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BOZFIX is a free service platform based in Antalya, Turkey, connecting customers with verified local craftsmen, service providers, and motorcycle couriers. The platform offers transparent pricing, 24/7 emergency assistance, and a 30‑day guarantee on work. It supports multiple languages and provides a searchable marketplace for services like electricians, plumbers, and more, without taking a commission from providers.
image: https://bozfix.com/img/icon-512.png
layout: provider
modified: '2026-11-02'
name: BOZFIX
nav: Providers
network: true
overview: 'BOZFIX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Services, Marketplace, Turkey, and Free.


  BOZFIX''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bozfix Com Domain Security
  slug: bozfix-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bozfix-com
tags:
- Company
- Services
- Marketplace
- Turkey
- Free
website: https://bozfix.com/
---
