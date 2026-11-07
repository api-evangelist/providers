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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/hos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/hos/hosts/hos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hos-hosts.yml
- group: other
  href: https://artifacts.apis.io/hos/vendors/hos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hos-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.hosinc.co/
- group: auth
  href: https://artifacts.apis.io/hos/security/hos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hosinc.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.hosinc.co/mcp
  - status: 403
    url: https://dev.hosinc.co/mcp
  - status: 200
    url: https://www.hosinc.co/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: hOS is a technology startup founded in 2021 by DataRobot Founder & CEO Jeremy Achin and other DataRobot alumni. The company builds AI‑driven technologies aimed at engineering prosperity, minimizing suffering, and delivering innovative solutions across industries. Backed by leading venture firms including NEA, Sequoia, B5 Capital, Cortical Ventures, and IA Ventures, hOS focuses on creating intelligent platforms that empower humans and businesses.
layout: provider
modified: '2026-10-26'
name: hOS
nav: Providers
network: true
overview: 'hOS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Startups, and Technology.


  hOS''s developer surface includes documentation and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.2
  provenance:
    mcp: unknown
    skills: unknown
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
screenshot: https://apis.io/screenshots/hos/hos-2026-11-03T133450.png
security:
- kind: domain-security
  name: Hos Domain Security
  slug: hos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hos
tags:
- Company
- Artificial Intelligence
- Startups
- Technology
website: https://www.hosinc.co/
---
