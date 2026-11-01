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
  href: https://artifacts.apis.io/lmql/hosts/lmql-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lmql-hosts.yml
- group: other
  href: https://artifacts.apis.io/lmql/vendors/lmql-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lmql-vendors.yml
- group: build
  href: https://artifacts.apis.io/lmql/packages/lmql-packages.yml
  title: ''
  type: SDKs
  url: packages/lmql-packages.yml
- group: build
  href: https://artifacts.apis.io/lmql/packages/lmql-packages.yml
  title: ''
  type: Packages
  url: packages/lmql-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://lmql.ai/playground
- group: docs
  title: ''
  type: Documentation
  url: https://lmql.ai/docs/
- group: company
  title: ''
  type: Blog
  url: https://lmql.ai/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://lmql.ai/docs/index.html
- group: auth
  href: https://artifacts.apis.io/lmql/security/lmql-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lmql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lmql.ai/
coverage:
  checked: '2026-10-20'
  detail: Documentation is rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://lmql.ai/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: LMQL provides a powerful query language for large language models, enabling developers to write expressive, constraint‑driven prompts that combine probabilistic reasoning with deterministic logic. The platform offers an open‑source SDK, cloud‑hosted execution, and integrations with major LLM providers, allowing seamless incorporation of advanced prompting techniques into applications ranging from chatbots to data analysis pipelines. LMQL’s documentation includes tutorials, API references, and example notebooks, helping users adopt the technology quickly and efficiently.
layout: provider
modified: '2026-10-20'
name: LMQL
nav: Providers
network: true
overview: 'LMQL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Query Language, LLM, and Open Source.


  LMQL''s developer surface includes sandbox, documentation, engineering blog, getting-started guide, and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 44.6
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
  name: Lmql Domain Security
  slug: lmql-domain-security
  summary_line: TLSv1.3
slug: lmql
tags:
- Company
- Artificial Intelligence
- Query Language
- LLM
- Open Source
website: https://lmql.ai/
---
