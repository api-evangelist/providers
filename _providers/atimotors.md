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
  href: https://raw.githubusercontent.com/api-evangelist/atimotors/refs/heads/main/llms/atimotors-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atimotors-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atimotors/refs/heads/main/hosts/atimotors-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atimotors-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atimotors/refs/heads/main/vendors/atimotors-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atimotors-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.atirobotics.ai/resources/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.atirobotics.ai/company/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atimotors/refs/heads/main/security/atimotors-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atimotors-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atirobotics.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/atimotors
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Ati Robotics (formerly Atimotors) provides autonomous mobile robots (AMRs) and AI-driven material orchestration software for factories. Their solutions include tugging, pallet movement, lifting, handling, and physical AI across industries such as automotive, medical, food & beverage, consumer goods, heavy equipment, and energy. With over 70 plants deployed and a 99% mission success rate, they claim rapid ROI and advanced automation capabilities.
image: https://www.atirobotics.ai/assets/images/social/og-default.jpg
layout: provider
modified: '2026-09-26'
name: Atimotors
nav: Providers
network: true
overview: Atimotors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Material Handling, Industrial Automation, Artificial Intelligence, and Factory Software.
random_paper: 4
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atimotors Domain Security
  slug: atimotors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atimotors
tags:
- Robotics
- Material Handling
- Industrial Automation
- Artificial Intelligence
- Factory Software
- Robots-as-a-Service
website: https://www.atirobotics.ai
---
