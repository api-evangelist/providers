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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuby-technologies/refs/heads/main/llms/cuby-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuby-technologies-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuby-technologies/refs/heads/main/hosts/cuby-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuby-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuby-technologies/refs/heads/main/vendors/cuby-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuby-technologies-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuby-technologies/refs/heads/main/security/cuby-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuby-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cubytechnologies.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cubytechnologies.com
  - status: 403
    url: https://forgeglobal.com/cuby-technologies_stock/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cuby Technologies, Inc. develops scalable hardware and software systems to improve process efficiency and automation in new home construction through its Mobile Micro‑Factories (MMF) platform. By deploying transportable, precision‑manufactured factories near construction sites, Cuby aims to deliver high‑quality, factory‑built homes faster, more affordably, and with reduced waste, addressing global housing deficits. The company offers an end‑to‑end platform that integrates design, manufacturing, logistics, and on‑site assembly, targeting developers, builders, and municipalities seeking rapid, sustainable housing solutions.
image: https://qtrypzzcjebvfcihiynt.supabase.co/storage/v1/render/image/public/base44-prod/public/691d125cc2afd268599683b0/5d7d33c51_Cuby_LogoMark_Black.png?width=1200&height=630&resize=contain
layout: provider
modified: '2026-10-11'
name: Cuby Technologies
nav: Providers
network: true
overview: Cuby Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Real Estate, Manufacturing, and Housing.
random_paper: 4
score:
  band: minimal
  composite: 4.2
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cuby Technologies Domain Security
  slug: cuby-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuby-technologies
tags:
- Company
- Construction
- Real Estate
- Manufacturing
- Housing
website: https://cubytechnologies.com
---
