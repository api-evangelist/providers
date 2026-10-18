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
  href: https://raw.githubusercontent.com/api-evangelist/flapico/refs/heads/main/llms/flapico-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flapico-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flapico/refs/heads/main/hosts/flapico-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flapico-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flapico/refs/heads/main/vendors/flapico-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flapico-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://flapico.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flapico
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flapico/refs/heads/main/security/flapico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flapico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flapico.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://flapico.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Flapico is a technology company specializing in AI and infrastructure, operating like a lab that builds products and services for the next generation of web users. The company focuses on rebuilding the web for agents and humans, offering AI-driven solutions, fast iteration, and a philosophy of loud, clear error handling. Flapico ships its own products, runs them first, and emphasizes rapid development and innovation across its portfolio.
layout: provider
modified: '2026-10-16'
name: Flapico
nav: Providers
network: true
overview: Flapico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Infrastructure, Web, and Lab.
random_paper: 8
score:
  band: minimal
  composite: 4.6
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
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flapico Domain Security
  slug: flapico-domain-security
  summary_line: TLSv1.3
slug: flapico
tags:
- Company
- Artificial Intelligence
- Infrastructure
- Web
- Lab
website: https://flapico.com/
---
