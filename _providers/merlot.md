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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/merlot/hosts/merlot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/merlot-hosts.yml
- group: auth
  href: https://artifacts.apis.io/merlot/security/merlot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merlot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.merlot.org/merlot/index.htm
- group: company
  title: ''
  type: Blog
  url: http://blog.merlot.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.merlot.org/merlot/index.htm
coverage:
  checked: '2026-10-27'
  detail: MERLOT provides educational resources but offers no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.merlot.org/merlot/index.htm
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: MERLOT (the Multimedia Educational Resource for Learning and Online Teaching) is a non‑profit organization that provides a curated collection of free and open online learning materials, tools, and resources for educators, students, and lifelong learners. It hosts a searchable repository of peer‑reviewed teaching materials, offers community‑driven support, and facilitates collaboration through its SkillsCommons platform, aiming to improve teaching and learning worldwide.
layout: provider
modified: '2026-10-26'
name: MERLOT
nav: Providers
network: true
overview: 'MERLOT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Open Source, Community, and Learning.


  MERLOT''s developer surface includes engineering blog, documentation, and 3 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 5.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/merlot/merlot-2026-11-03T135501.png
security:
- kind: domain-security
  name: Merlot Domain Security
  slug: merlot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: merlot
tags:
- Company
- Education
- Open Source
- Community
- Learning
website: https://www.merlot.org/merlot/index.htm
---
