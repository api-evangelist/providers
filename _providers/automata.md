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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: The LINQ API provides programmatic access to Automata's lab automation platform, enabling workflow creation, execution, and monitoring.
  name: LINQ API
  slug: linq-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automata/refs/heads/main/llms/automata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automata-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automata/refs/heads/main/well-known/automata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automata-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automata/refs/heads/main/hosts/automata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automata-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automata/refs/heads/main/vendors/automata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automata-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.automata.tech/about-us/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.automata.tech/blog/drug-discovery
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.automata.tech/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automata.tech/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automata/refs/heads/main/security/automata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.automata.tech
coverage:
  checked: 2026-09-26
  detail: Documentation is public HTML but provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.automata.tech/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Automata provides an AI‑ready, software‑defined lab automation platform that orchestrates parallel workflows, delivers real‑time analytics, and integrates genomics, cell biology, and assay screening. Their LINQ suite enables developers to build, run, and monitor complex laboratory processes, accelerating discovery and reducing manual intervention across biotech and life‑science research.
layout: provider
modified: '2026-09-26'
name: Automata
nav: Providers
network: true
overview: 'Automata publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lab Automation, Artificial Intelligence, Biotechnology, and Software.


  Automata''s developer surface includes engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automata Domain Security
  slug: automata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: automata
tags:
- Company
- Lab Automation
- Artificial Intelligence
- Biotechnology
- Software
website: https://www.automata.tech
---
