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
api_count: 1
apis:
- description: SigmaKit is a complete imitation‑learning package offering AI software, robotic hands, and teaching tools for manufacturing automation.
  name: SigmaKit API
  slug: sigmakit-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carbonsix/refs/heads/main/llms/carbonsix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carbonsix-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonsix/refs/heads/main/hosts/carbonsix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonsix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonsix/refs/heads/main/vendors/carbonsix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbonsix-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.carbon6robotics.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbonsix/refs/heads/main/security/carbonsix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonsix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbon6robotics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.carbon6robotics.com/product/
- group: company
  title: ''
  type: Newsroom
  url: https://www.carbon6robotics.com/newsroom/
- group: operate
  title: ''
  type: Contact
  url: https://www.carbon6robotics.com/contact/
coverage:
  checked: '2026-10-07'
  detail: Product page loads via JavaScript and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.carbon6robotics.com/product/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: CarbonSix is a Physical AI company developing deployment‑ready robotic intelligence and automation solutions for manufacturing. It combines Six‑Sigma robot dexterity with AI‑powered imitation learning to create adaptable robot skills for high‑variance factory environments, aiming to transform industrial operations worldwide.
layout: provider
modified: '2026-10-07'
name: CarbonSix
nav: Providers
network: true
overview: 'CarbonSix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Physical-AI, Manufacturing, and Automation.


  CarbonSix''s developer surface includes documentation and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.9
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
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Carbonsix Domain Security
  slug: carbonsix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbonsix
tags:
- Company
- Robotics
- Physical-AI
- Manufacturing
- Automation
- Artificial Intelligence
website: https://www.carbon6robotics.com/
---
