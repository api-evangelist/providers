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
  href: https://artifacts.apis.io/livsmedelsverket/hosts/livsmedelsverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livsmedelsverket-hosts.yml
- group: other
  href: https://artifacts.apis.io/livsmedelsverket/vendors/livsmedelsverket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/livsmedelsverket-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.livsmedelsverket.se/om-oss/press/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.livsmedelsverket.se/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Livsmedelsverket
- group: auth
  href: https://artifacts.apis.io/livsmedelsverket/security/livsmedelsverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livsmedelsverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livsmedelsverket.se/
coverage:
  checked: '2026-10-26'
  detail: The provider's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.livsmedelsverket.se
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Livsmedelsverket, the Swedish Food Agency, is a government authority responsible for food safety, nutrition, and consumer information in Sweden. It develops regulations, conducts research, and provides guidance to ensure safe and healthy food for the public, covering areas such as food labeling, contaminants, and dietary advice.
layout: provider
modified: '2026-10-26'
name: Livsmedelsverket (Swedish Food Agency)
nav: Providers
network: true
overview: 'Livsmedelsverket (Swedish Food Agency) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Food Safety, Nutrition, and Sweden.


  Livsmedelsverket (Swedish Food Agency)''s developer surface includes documentation and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 45.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/livsmedelsverket/livsmedelsverket-2026-11-03T134943.png
security:
- kind: domain-security
  name: Livsmedelsverket Domain Security
  slug: livsmedelsverket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livsmedelsverket
tags:
- Company
- Government
- Food Safety
- Nutrition
- Sweden
website: https://www.livsmedelsverket.se/
---
