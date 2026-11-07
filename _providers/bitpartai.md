---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bitpartai/plans/bitpartai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bitpartai-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/bitpartai/hosts/bitpartai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitpartai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitpartai/vendors/bitpartai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitpartai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bitpartai/security/bitpartai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitpartai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitpart.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bitpart-ai.gitbook.io/bitpart.ai-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bitpart.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://bitpart-ai.gitbook.io/bitpart.ai-docs/getting-started-with-bitpart/editor
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bitpart.ai/pricing
coverage:
  checked: '2026-10-24'
  detail: Bitpart.ai documentation is served via GitBook with JavaScript rendering, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://bitpart-ai.gitbook.io/bitpart.ai-docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Bitpart.ai provides a platform for creating immersive, AI‑driven virtual worlds. It offers tools such as the Bitpart Unreal Plugin, Archetypes, Coppola authoring tool, and the Aesop multi‑agent planner, enabling developers to build interactive characters and environments. The service includes documentation, tutorials, pricing plans, and a community hub, targeting game developers, simulation creators, and AI researchers.
image: http://static1.squarespace.com/static/66352b116635501ff3ab78a5/t/66352b146635501ff3ab78fe/1713556130551/_logo.png?format=1500w
layout: provider
modified: '2026-10-24'
name: Bitpart.ai
nav: Providers
network: true
overview: 'Bitpart.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Virtual Worlds, Game Development, and Simulation.


  Bitpart.ai''s developer surface includes documentation, getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Bitpartai Plans Pricing
  plan_count: 2
  slug: bitpartai-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.9
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
screenshot: https://apis.io/screenshots/bitpartai/bitpartai-2026-11-03T121821.png
security:
- kind: domain-security
  name: Bitpartai Domain Security
  slug: bitpartai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitpartai
tags:
- Company
- Artificial Intelligence
- Virtual Worlds
- Game Development
- Simulation
website: https://www.bitpart.ai/
---
