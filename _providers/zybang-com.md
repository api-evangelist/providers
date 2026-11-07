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
  href: https://artifacts.apis.io/zybang-com/hosts/zybang-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zybang-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/zybang-com/security/zybang-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zybang-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zybang.com/
coverage:
  checked: '2026-10-25'
  detail: The provider's website does not expose any machine‑readable API specifications and appears to rely on JavaScript‑rendered pages.
  evidence:
  - status: 200
    url: https://www.zybang.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Zuoyebang, also known as 作业帮, is a leading online education platform founded in 2015 in Guangzhou, China. It offers AI‑driven tutoring, homework assistance, and a suite of educational tools for primary and secondary students. The company emphasizes technology for education, providing mobile apps, smart hardware, and a cloud‑based learning ecosystem. It has received numerous awards and media coverage, reflecting its impact on the Chinese ed‑tech market. Zuoyebang is backed by Coatue and continues to expand its services and social responsibility initiatives.
layout: provider
modified: '2026-10-25'
name: Zuoyebang
nav: Providers
network: true
overview: Zuoyebang is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, EdTech, Artificial Intelligence, Homework, and China.
random_paper: 7
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zybang-com/zybang-com-2026-11-03T150601.png
security:
- kind: domain-security
  name: Zybang Com Domain Security
  slug: zybang-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: zybang-com
tags:
- Education
- EdTech
- Artificial Intelligence
- Homework
- China
website: https://www.zybang.com/
---
