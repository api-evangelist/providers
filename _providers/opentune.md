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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/opentune/hosts/opentune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opentune-hosts.yml
- group: other
  href: https://artifacts.apis.io/opentune/vendors/opentune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opentune-vendors.yml
- group: auth
  href: https://artifacts.apis.io/opentune/security/opentune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opentune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weboasis.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://weboasis.io/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Weboasis is a technology studio specializing in Web3, AI, and custom web applications. Their Opentune product is an in‑house AI tool that provides real‑time interaction, model customization, data analysis, and fine‑tuning for large language models such as LLaMA, GPT, and Claude. Opentune aims to help businesses integrate and optimize AI capabilities across workflows, offering a versatile, model‑agnostic platform for developers and enterprises.
image: https://weboasis.io/wo_metaimage_comp.jpg
layout: provider
modified: '2026-10-21'
name: Weboasis
nav: Providers
network: true
overview: Weboasis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web3, Artificial Intelligence, Software-as-a-Service, and Platform.
random_paper: 14
score:
  band: minimal
  composite: 3.4
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
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Opentune Domain Security
  slug: opentune-domain-security
  summary_line: TLSv1.3 · HSTS
slug: opentune
tags:
- Company
- Web3
- Artificial Intelligence
- Software-as-a-Service
- Platform
website: https://weboasis.io/
---
