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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/automation-hero/refs/heads/main/llms/automation-hero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automation-hero-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/automation-hero/refs/heads/main/hosts/automation-hero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automation-hero-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/automation-hero/refs/heads/main/security/automation-hero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automation-hero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://automationhero.com
coverage:
  checked: 2026-09-26
  detail: The provider's website returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://automationhero.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: 'Automation Hero is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-26'
name: Automation Hero
nav: Providers
network: true
overview: Automation Hero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 2
score:
  band: minimal
  composite: 1.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 33.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automation Hero Domain Security
  slug: automation-hero-domain-security
  summary_line: TLSv1.3
slug: automation-hero
tags:
- Company
website: https://automationhero.com
---
