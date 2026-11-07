---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ag Leader provides an AgFiniti API for transfer of files to and from its cloud-based AgFiniti system, alongside file components (DLLs) for reading and writing its proprietary file formats; access is r
  name: AgFiniti API
  slug: agfiniti-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/ag-leader/llms/ag-leader-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ag-leader-llms.txt
- group: operate
  href: https://artifacts.apis.io/ag-leader/changelog/ag-leader-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ag-leader-changelog.yml
- group: design
  href: https://artifacts.apis.io/ag-leader/conventions/ag-leader-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ag-leader-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ag-leader/authentication/ag-leader-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ag-leader-authentication.yml
- group: agent
  href: https://artifacts.apis.io/ag-leader/well-known/ag-leader-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ag-leader-well-known.yml
- group: other
  href: https://artifacts.apis.io/ag-leader/hosts/ag-leader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ag-leader-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.agleader.com/community/s/article/1356
- group: docs
  title: ''
  type: Documentation
  url: https://dev.agfiniti.com/
- group: auth
  href: https://artifacts.apis.io/ag-leader/security/ag-leader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ag-leader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agleader.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agleader.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://www.agleader.com/blog/category/articles/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.agleader.com/blog/category/whats-new/
- group: operate
  title: ''
  type: Support
  url: https://www.agleader.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agleader.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.agfiniti.com/Account/Login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ag-leader-technology
created: '2026-10-18'
description: Ag Leader Technology is an American precision agriculture company founded in 1992 by Al Myers that makes displays and data management (InCommand Go, AgFiniti cloud, SMS software), GPS receivers and machine guidance (SteerCommand Z2, SteadySteer), planter, applicator and combine yield-monitoring technology, plus precision turf equipment. For third-party developers it provides file components (DLLs) for reading and writing its proprietary file formats and an AgFiniti API for transferring files to and from its cloud, with access requested via its Developers page.
image: https://www.agleader.com/wp-content/uploads/2024/04/Ag-Leader-Logo1-1.png
layout: provider
modified: '2026-10-18'
name: Ag Leader
nav: Providers
network: true
overview: 'Ag Leader is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Precision Agriculture, Farm Data, and GPS Guidance.


  Ag Leader''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, support, and 11 more developer resources.'
plans:
- name: Ag Leader Plans Pricing
  plan_count: 0
  slug: ag-leader-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Ag Leader Rate Limits
  slug: ag-leader-rate-limits
scopes:
- name: Ag Leader Scopes
  scope_count: 0
  slug: ag-leader-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ag-leader/ag-leader-2026-11-03T120337.png
security:
- kind: authentication
  name: Ag Leader Authentication
  slug: ag-leader-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ag Leader Domain Security
  slug: ag-leader-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ag-leader
tags:
- Company
- Agriculture
- Precision Agriculture
- Farm Data
- GPS Guidance
- Agricultural Equipment
- Cloud File Transfer
website: https://agleader.com
---
