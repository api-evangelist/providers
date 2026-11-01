---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/promptgruup/hosts/promptgruup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptgruup-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptgruup/vendors/promptgruup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptgruup-vendors.yml
- group: auth
  href: https://artifacts.apis.io/promptgruup/security/promptgruup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptgruup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptgruup.com/
coverage:
  checked: '2026-10-18'
  detail: The homepage returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://promptgruup.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: PromptGruup provides AI‑driven prompt engineering services, helping developers and creators craft high‑quality inputs for large language models. The company offers a platform that curates, tests, and optimizes prompts across multiple AI providers, delivering analytics, version control, and collaborative tools. By integrating with popular LLM APIs, PromptGruup enables rapid iteration and deployment of prompt‑based applications, reducing time‑to‑market and improving model performance. Their mission is to democratize access to effective prompt design, supporting enterprises, startups, and individual developers in unlocking the full potential of generative AI technologies.
layout: provider
modified: '2026-10-18'
name: PromptGruup
nav: Providers
network: true
overview: PromptGruup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Prompt Engineering, Platform, and Collaboration.
random_paper: 13
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
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
  name: Promptgruup Domain Security
  slug: promptgruup-domain-security
  summary_line: TLSv1.3 · HSTS
slug: promptgruup
tags:
- Company
- Artificial Intelligence
- Prompt Engineering
- Platform
- Collaboration
website: https://promptgruup.com/
---
