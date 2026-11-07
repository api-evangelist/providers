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
- description: API for BigTeams athletic scheduling platform
  name: BigTeams API
  slug: bigteams-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bigteams/hosts/bigteams-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigteams-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.bigteams.com/topics/log-in/
- group: company
  title: ''
  type: Blog
  url: https://www.bigteams.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BigTeams
- group: auth
  href: https://artifacts.apis.io/bigteams/security/bigteams-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigteams-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigteams.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigteams.com/big-teams-privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigteams.com/terms-conditions-big-teams/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: BigTeams provides athletic scheduling and team management software for high schools and colleges in the United States and Canada. Founded in 2001, the platform helps athletic directors, coaches, and administrators streamline event scheduling, roster management, eligibility compliance, and communication with athletes and parents. Over 55 years of experience have made BigTeams a leading digital solution in K‑12 athletics, serving thousands of schools across more than 40 states.
image: https://www.bigteams.com/wp-content/uploads/2023/12/BigTeams-baseball-stadium_v2b.jpg
layout: provider
modified: '2026-09-28'
name: BigTeams
nav: Providers
network: true
overview: 'BigTeams is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Athletic Software, K-12, Scheduling, Team Management, and USA.


  BigTeams'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bigteams/bigteams-2026-10-11T102142.png
security:
- kind: domain-security
  name: Bigteams Domain Security
  slug: bigteams-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bigteams
tags:
- Athletic Software
- K-12
- Scheduling
- Team Management
- USA
- Canada
website: https://www.bigteams.com
---
