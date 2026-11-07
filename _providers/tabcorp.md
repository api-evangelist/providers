---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: TAB Studio is Tabcorp's developer portal for the TAB wagering API, a hypermedia API whose start page at https://api.beta.tab.com.au links to its capabilities and resources (per the TAB Studio concepts
  name: TAB Studio API
  slug: tab-studio-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/tabcorp/conventions/tabcorp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tabcorp-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tabcorp/authentication/tabcorp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tabcorp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tabcorp/scopes/tabcorp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tabcorp-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://studio.tab.com.au/intro/versioning.html
- group: design
  href: https://artifacts.apis.io/tabcorp/lifecycle/tabcorp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tabcorp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tabcorp/errors/tabcorp-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/tabcorp-error-codes.yml
- group: design
  href: https://artifacts.apis.io/tabcorp/conformance/tabcorp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tabcorp-conformance.yml
- group: other
  href: https://artifacts.apis.io/tabcorp/hosts/tabcorp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tabcorp-hosts.yml
- group: other
  href: https://artifacts.apis.io/tabcorp/vendors/tabcorp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tabcorp-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tabcorp/security/tabcorp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tabcorp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tabcorp.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tabcorp
created: '2026-10-22'
description: Tabcorp Holdings Limited is an ASX-listed (TAH) Australian wagering, media and gaming services company headquartered in Melbourne. Its Wagering and Media business runs the TAB brand (totalisator and fixed-odds betting through retail venues, online, mobile and phone channels) and Sky Racing television and Sky Sports Radio; its Gaming Services business operates under the MAX brand, monitoring electronic gaming machines for regulators and supplying and maintaining venue gaming systems. Its former Lotteries and Keno arm was demerged in 2022 as The Lottery Corporation. Tabcorp publishes open-source technology projects through its GitHub organization and runs the TAB Studio developer portal (studio.tab.com.au) for the TAB API at api.beta.tab.com.au, both geo-restricted to licensed jurisdictions. Surfaced via the API Evangelist harvest backlog (australia-apidays-2026).
image: https://avatars.githubusercontent.com/u/29614885?v=4
layout: provider
modified: '2026-10-22'
name: Tabcorp
nav: Providers
network: true
overview: 'Tabcorp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wagering, Betting, Gaming, and Media.


  Tabcorp''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Tabcorp Plans Pricing
  plan_count: 0
  slug: tabcorp-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Tabcorp Rate Limits
  slug: tabcorp-rate-limits
scopes:
- name: Tabcorp Scopes
  scope_count: 3
  slug: tabcorp-scopes
  summary_line: 3 scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 6.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tabcorp/tabcorp-2026-11-03T144258.png
security:
- kind: authentication
  name: Tabcorp Authentication
  slug: tabcorp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tabcorp Domain Security
  slug: tabcorp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tabcorp
tags:
- Company
- Wagering
- Betting
- Gaming
- Media
- Racing
- Australia
website: https://tabcorp.com.au/
---
