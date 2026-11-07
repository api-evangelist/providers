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
  href: https://artifacts.apis.io/esb/hosts/esb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esb-hosts.yml
- group: auth
  href: https://artifacts.apis.io/esb/security/esb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://esb.ie/
- group: docs
  title: ''
  type: Documentation
  url: https://esb.ie/who-we-are
- group: company
  title: ''
  type: Blog
  url: https://esb.ie/news---insights/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://esb.ie/data-protection
coverage:
  checked: '2026-10-27'
  detail: The provider's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://esb.ie/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: ESB ecars is an Irish energy company focused on delivering sustainable electricity and smart energy solutions. It operates a diversified portfolio including renewable generation, telecoms infrastructure, and smart‑energy services for residential and commercial customers. The company emphasizes innovation, community engagement, and a transition to low‑carbon energy sources, supporting Ireland’s climate goals while providing reliable power and digital services.
layout: provider
modified: '2026-10-27'
name: ESB ecars
nav: Providers
network: true
overview: 'ESB ecars is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Ireland, Renewables, and Telecommunications.


  ESB ecars'' developer surface includes documentation, engineering blog, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/esb/esb-2026-11-03T131614.png
security:
- kind: domain-security
  name: Esb Domain Security
  slug: esb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: esb
tags:
- Energy
- Utilities
- Ireland
- Renewables
- Telecommunications
website: https://esb.ie/
---
