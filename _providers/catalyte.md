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
  href: https://artifacts.apis.io/catalyte/hosts/catalyte-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catalyte-hosts.yml
- group: other
  href: https://artifacts.apis.io/catalyte/vendors/catalyte-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catalyte-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://artifacts.apis.io/catalyte/security/catalyte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalyte-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.catalyte.io/
coverage:
  checked: '2026-10-07'
  detail: API endpoints return 403/401 without authentication, indicating a partner login wall.
  evidence:
  - status: 403
    url: https://api.catalyte.io/mcp
  reason: partner-login
  state: gated
created: '2026-10-07'
description: Catalyte is an AI‑enabled workforce platform that uses proprietary technology and over 500 data points to discover, develop, and place high‑potential talent. Founded in 2000 and based in Baltimore, the company offers employers a talent‑as‑a‑service model, providing trained software developers and other skilled workers on demand. Catalyte’s services include talent sourcing, training, and placement, helping organizations accelerate hiring, reduce turnover, and build high‑performing teams. The platform also partners with educational institutions to create pipelines of skilled workers, delivering a blend of technology and human expertise to meet modern workforce needs.
layout: provider
modified: '2026-10-07'
name: Catalyte
nav: Providers
network: true
overview: Catalyte is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tech consulting, Staff Augmentation, Apprenticeship programs, Digital Transformation, and AI enablement.
random_paper: 15
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/catalyte/catalyte-2026-11-03T123517.png
security:
- kind: domain-security
  name: Catalyte Domain Security
  slug: catalyte-domain-security
  summary_line: TLSv1.3 · DMARC
slug: catalyte
tags:
- Tech consulting
- Staff Augmentation
- Apprenticeship programs
- Digital Transformation
- AI enablement
- Data Engineering
- Cloud Services
- Enterprise Services
website: https://www.catalyte.io/
---
