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
- group: agent
  href: https://artifacts.apis.io/guided-energy/llms/guided-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/guided-energy-llms.txt
- group: other
  href: https://artifacts.apis.io/guided-energy/hosts/guided-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/guided-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/guided-energy/vendors/guided-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/guided-energy-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.guided.energy/en/blog
- group: auth
  href: https://artifacts.apis.io/guided-energy/security/guided-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guided-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://guided.energy
coverage:
  checked: '2026-10-23'
  detail: The provider's documentation pages return HTML shells with JavaScript redirects and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://guidedenergy.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Guided Energy builds autonomous AI agents that automate track and trace, carrier booking, load sourcing, and dispatch operations for freight teams. Their AI-driven logistics platform streamlines transportation management, improves visibility, and reduces manual effort across the supply chain, delivering smarter, faster freight operations for shippers and carriers.
image: https://guided.energy/og-image.jpeg
layout: provider
modified: '2026-10-23'
name: Guided Energy
nav: Providers
network: true
overview: 'Guided Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Logistics, Freight, and Automation.


  Guided Energy''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.6
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
screenshot: https://apis.io/screenshots/guided-energy/guided-energy-2026-11-03T133118.png
security:
- kind: domain-security
  name: Guided Energy Domain Security
  slug: guided-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: guided-energy
tags:
- Company
- Artificial Intelligence
- Logistics
- Freight
- Automation
website: https://guided.energy
---
