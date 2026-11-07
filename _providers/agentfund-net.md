---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/agentfund-net/hosts/agentfund-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentfund-net-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentfund-net/security/agentfund-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentfund-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentfund.net/
coverage:
  checked: '2026-11-01'
  detail: No public API specifications or documentation were found on the company's website or API host.
  evidence:
  - status: 200
    url: https://agentfund.net/
  - status: 404
    url: https://agentfund.net/openapi.json
  - status: 0
    url: https://api.agentfund.net/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: Agent Fund Ventures backs the autonomous economy by building and funding companies that make AI agents useful. We run on the technology we build for, with operations—support, analytics, deployment—executed by AI agents, delivering more product with less overhead. We bootstrap without VC, creating profitable businesses that generate revenue and reinvest. Our thesis is that every job is a bundle of tasks that AI agents can unbundle into automatable units, scaling with compute rather than headcount.
image: https://agentfund.net/favicon.png
layout: provider
modified: '2026-10-31'
name: Agent Fund Ventures
nav: Providers
network: true
overview: Agent Fund Ventures is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Venture Capital, Funding, Autonomous-Economy, and Startups.
random_paper: 8
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentfund Net Domain Security
  slug: agentfund-net-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentfund-net
tags:
- Artificial Intelligence
- Venture Capital
- Funding
- Autonomous-Economy
- Startups
website: https://agentfund.net/
---
