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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/qxli/hosts/qxli-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qxli-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.qxli.com/
- group: auth
  href: https://artifacts.apis.io/qxli/security/qxli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qxli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qxli.com/
coverage:
  checked: '2026-10-18'
  detail: The provider's website https://qxli.com/ returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://qxli.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Space Armour, operating under the brand QXLI, provides an open sovereign AI engine for organizations that cannot rely on SaaS AI solutions. Their platform enables enterprises to deploy, control, and fine‑tune multiple large language models on‑premises, ensuring data never leaves the organization. The solution promises rapid deployment within weeks, multi‑model capabilities, cost‑effective pre‑configured setups, and full control over infrastructure, addressing compliance and IP protection needs for complex AI adoption.
layout: provider
modified: '2026-10-18'
name: Space Armour
nav: Providers
network: true
overview: 'Space Armour is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sovereign AI, Enterprise AI, Private AI, AI Agents, and Knowledge Assistant.


  Space Armour''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Qxli Domain Security
  slug: qxli-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qxli
tags:
- Sovereign AI
- Enterprise AI
- Private AI
- AI Agents
- Knowledge Assistant
- Workflow Automation
- Secure RAG
- AI Platform
website: https://qxli.com/
---
