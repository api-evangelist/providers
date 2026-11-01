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
- group: other
  href: https://artifacts.apis.io/selectstar/hosts/selectstar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/selectstar-hosts.yml
- group: other
  href: https://artifacts.apis.io/selectstar/vendors/selectstar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/selectstar-vendors.yml
- group: auth
  href: https://artifacts.apis.io/selectstar/security/selectstar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/selectstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://selectstar.ai/
- group: company
  title: ''
  type: Blog
  url: https://selectstar.ai/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://selectstar.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://selectstar.ai/usecases/
- group: operate
  title: ''
  type: Support
  url: https://selectstar.ai/contact_page/
coverage:
  checked: '2026-10-19'
  detail: Developer portal at https://dev.selectstar.ai/ serves only JavaScript-rendered pages, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://dev.selectstar.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Selectstar AI provides data‑centric AI consulting, development, and deployment services, including data design, LLM validation, and end‑to‑end AI solution building. Leveraging over 200 million data tasks, they help enterprises accelerate AI adoption with robust data pipelines and model integration.
image: https://selectstar.ai/wp-content/uploads/2023/07/thum.png
layout: provider
modified: '2026-10-18'
name: Selectstar
nav: Providers
network: true
overview: 'Selectstar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Consulting, Data, and LLM.


  Selectstar''s developer surface includes engineering blog, documentation, getting-started guide, support, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Selectstar Domain Security
  slug: selectstar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: selectstar
tags:
- Company
- Artificial Intelligence
- Consulting
- Data
- LLM
- Platform
website: https://selectstar.ai/
---
