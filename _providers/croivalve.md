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
- group: company
  title: ''
  type: Website
  url: https://www.croivalve.com
- group: other
  title: ''
  type: Leadership
  url: https://www.croivalve.com/our-team/
- group: company
  title: ''
  type: Newsroom
  url: https://www.croivalve.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.croivalve.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://www.croivalve.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.croivalve.com/privacy-policy/
- group: other
  href: https://artifacts.apis.io/croivalve/hosts/croivalve-hosts.yml
  title: ''
  type: Hosts
  url: hosts/croivalve-hosts.yml
- group: other
  href: https://artifacts.apis.io/croivalve/vendors/croivalve-vendors.yml
  title: ''
  type: Vendors
  url: vendors/croivalve-vendors.yml
- group: auth
  href: https://artifacts.apis.io/croivalve/security/croivalve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/croivalve-domain-security.yml
coverage:
  checked: '2026-11-04'
  detail: CroíValve is a Dublin-based clinical-stage medical device company developing the DUO Adapt transcatheter tricuspid valve therapy (under clinical investigation, not commercially available); its only web presence is a WordPress marketing site with no developer portal, API host, docs, GitHub org, Postman workspace or MCP server advertised.
  evidence:
  - status: 200
    url: https://www.croivalve.com/
  - status: 200
    url: https://www.croivalve.com/our-team/
  - status: 200
    url: https://www.croivalve.com/news/
  reason: not-a-software-company
  state: none
created: '2026-10-11'
description: CroíValve is a Dublin, Ireland-based clinical-stage medical device company developing the DUO Adapt™ System, a minimally invasive transcatheter device designed to treat patients suffering from tricuspid regurgitation (TR) by assisting the native tricuspid valve rather than replacing it. The company's stated mission is to shorten the learning curve for practitioners, preserve native anatomy and extend lives. The DUO Adapt™ System is under clinical investigation and not commercially available in any geography.
image: https://www.croivalve.com/wp-content/uploads/2025/09/logo-1-1.png
layout: provider
modified: '2026-11-04'
name: CroíValve
nav: Providers
network: true
overview: 'CroíValve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Heart Valve, Tricuspid Regurgitation, and Structural Heart.


  CroíValve''s developer surface includes support and 8 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
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
      reason: no_resolvable_host
  previous_composite: 1.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Croivalve Domain Security
  slug: croivalve-domain-security
  summary_line: TLSv1.3 · DMARC
slug: croivalve
tags:
- Company
- Medical Devices
- Heart Valve
- Tricuspid Regurgitation
- Structural Heart
- Cardiovascular
- Clinical Stage
- Dublin
- Ireland
website: https://www.croivalve.com
---
