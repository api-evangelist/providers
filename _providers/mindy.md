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
  href: https://artifacts.apis.io/mindy/hosts/mindy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mindy-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mindy/security/mindy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mindy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mindy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://mindy.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Mindy is an AI‑first workflow automation platform that started in 2023 to make artificial intelligence accessible and useful for everyday users. Initially an email‑first AI agent, Mindy helped simplify complex workflows, manage context, and turn communications into actionable tasks. The product expanded to support content workflows for creators and brand teams. In 2024 Mindy joined WorkWhile, an AI‑native labor platform, extending its reach to frontline enterprise workers and broadening its impact across the workforce.
layout: provider
modified: '2026-10-23'
name: Mindy
nav: Providers
network: true
overview: Mindy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Workflow Automation, Email Agent, and Enterprise.
random_paper: 17
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
  name: Mindy Domain Security
  slug: mindy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mindy
tags:
- Company
- AI
- Workflow Automation
- Email Agent
- Enterprise
website: https://mindy.com/
---
