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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API services offered by AvantGuard
  name: AvantGuard API
  slug: avantguard-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avantguard/refs/heads/main/llms/avantguard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avantguard-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avantguard/refs/heads/main/hosts/avantguard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avantguard-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avantguard/refs/heads/main/vendors/avantguard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avantguard-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.avantguardinc.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.avantguardinc.com/news/categories/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avantguard/refs/heads/main/security/avantguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avantguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avantguardinc.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.avantguardinc.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: AvantGuard is a Cornell University‑based spin‑out developing antimicrobial technologies to combat Candida auris and other pathogens. The company leverages N‑halamine chemistry to create surface‑protecting solutions for healthcare, consumer, and industrial markets, aiming to reduce reliance on traditional antibiotics. Founded in 2018 as Halomine, AvantGuard has secured multiple NIH grants and a $1.7 M seed round to advance its decolonization platform.
image: https://static.wixstatic.com/media/54e09a_1fa6b9cb133e4576a48ea7e52b0eb5b6~mv2.jpg/v1/fill/w_1800,h_1134,al_c/54e09a_1fa6b9cb133e4576a48ea7e52b0eb5b6~mv2.jpg
layout: provider
modified: '2026-09-26'
name: AvantGuard
nav: Providers
network: true
overview: 'AvantGuard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Antimicrobial, Biotechnology, Healthcare, and Startups.


  AvantGuard''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avantguard Domain Security
  slug: avantguard-domain-security
  summary_line: TLSv1.3 · HSTS
slug: avantguard
tags:
- Company
- Antimicrobial
- Biotechnology
- Healthcare
- Startups
website: https://www.avantguardinc.com/
---
