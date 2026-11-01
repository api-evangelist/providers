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
  href: https://artifacts.apis.io/thehalara-com/llms/thehalara-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thehalara-com-llms.txt
- group: other
  href: https://artifacts.apis.io/thehalara-com/hosts/thehalara-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thehalara-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/thehalara-com/vendors/thehalara-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thehalara-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/thehalara-com/security/thehalara-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thehalara-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thehalara.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://thehalara.com/mcp
  - status: 200
    url: https://thehalara.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: 'Halara is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by hongshan) and added to the network as a stub for full-pipeline profiling.'
image: https://mpir.halarastatic.com/upload/online/59/13/22/06/22/_7756834691-750x.jpg
layout: provider
modified: '2026-10-25'
name: Halara
nav: Providers
network: true
overview: Halara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 6
score:
  band: minimal
  composite: 1.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Thehalara Com Domain Security
  slug: thehalara-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thehalara-com
tags:
- Company
website: https://thehalara.com
---
