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
  href: https://artifacts.apis.io/anyang-university/hosts/anyang-university-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anyang-university-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anyang.ac.kr/main/activities/privacy-policy.do
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.anyang.ac.kr/
- group: auth
  href: https://artifacts.apis.io/anyang-university/security/anyang-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anyang-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anyang.ac.kr/main/index.do
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.anyang.ac.kr/main/index.do
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Anyang University is a public university located in Anyang, South Korea. It offers a wide range of undergraduate and graduate programs across various fields such as engineering, humanities, natural sciences, and social sciences. The university emphasizes research, innovation, and community engagement, aiming to foster global talent and contribute to societal development. Its campus provides modern facilities, libraries, and collaborative spaces for students and faculty.
image: https://www.anyang.ac.kr/_res/anyang/_share/img/logo_b_l.png
layout: provider
modified: '2026-10-23'
name: Anyang University
nav: Providers
network: true
overview: Anyang University is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, University, South Korea, Higher Education, and Research.
random_paper: 5
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/anyang-university/anyang-university-2026-11-03T120901.png
security:
- kind: domain-security
  name: Anyang University Domain Security
  slug: anyang-university-domain-security
  summary_line: TLSv1.3
slug: anyang-university
tags:
- Education
- University
- South Korea
- Higher Education
- Research
website: https://www.anyang.ac.kr/main/index.do
---
