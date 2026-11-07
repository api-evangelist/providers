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
api_count: 1
apis:
- description: API information not publicly documented.
  name: Fuzhou University API
  slug: fuzhou-university-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/fuzhou-university/hosts/fuzhou-university-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fuzhou-university-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fuzhou-university/security/fuzhou-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fuzhou-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.fzu.edu.cn/html/EN/index.shtml
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI or other machine‑readable contract was found on the provider’s hosts.
  evidence:
  - status: 0
    url: http://api.edu.cn/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Fuzhou University (福州大学) is a comprehensive public university located in Fuzhou, Fujian Province, China. Established in 1958, it offers a wide range of undergraduate, graduate, and doctoral programs across disciplines such as engineering, science, humanities, and medicine. The university is actively involved in research, international collaborations, and community service, contributing to regional development and innovation.
layout: provider
modified: '2026-10-26'
name: Fuzhou University
nav: Providers
network: true
overview: Fuzhou University is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include University, Education, China, Public, and Research.
random_paper: 16
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
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
  previous_composite: 3.5
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
screenshot: https://apis.io/screenshots/fuzhou-university/fuzhou-university-2026-11-03T132435.png
security:
- kind: domain-security
  name: Fuzhou University Domain Security
  slug: fuzhou-university-domain-security
  summary_line: TLSv1.2
slug: fuzhou-university
tags:
- University
- Education
- China
- Public
- Research
website: http://www.fzu.edu.cn/html/EN/index.shtml
---
