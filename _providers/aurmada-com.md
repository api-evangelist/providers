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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aurmada-com/llms/aurmada-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurmada-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aurmada-com/hosts/aurmada-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurmada-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurmada-com/vendors/aurmada-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurmada-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aurmada.com/news
- group: auth
  href: https://artifacts.apis.io/aurmada-com/security/aurmada-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurmada-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aurmada.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on the provider's hosts.
  evidence:
  - status: 200
    url: https://aurmada.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'Aurmada builds the OS for humans, robots, and AI: a hardware‑agnostic layer where people, AI agents, and robots share context and act together in the physical world. The platform enables seamless integration across devices, providing developers with APIs to manage identity, data exchange, and orchestration of autonomous agents. Aurmada aims to simplify the creation of intelligent ecosystems that bridge physical and digital realms.'
image: https://aurmada.com/images/og-image.jpg
layout: provider
modified: '2026-11-02'
name: Aurmada
nav: Providers
network: true
overview: Aurmada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Robotics, Platform, Os, and Human-Computer Interaction.
random_paper: 15
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 3.6
  provenance:
    mcp: unknown
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
  name: Aurmada Com Domain Security
  slug: aurmada-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aurmada-com
tags:
- Artificial Intelligence
- Robotics
- Platform
- Os
- Human-Computer Interaction
website: https://aurmada.com/
---
