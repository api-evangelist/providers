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
- description: 'SDK and onboard vehicle APIs for building Android Automotive OS apps on Renault Group openR / openR evo infotainment systems: SDK setup, IVI emulators, and partner-only Android vehicle properties (veh'
  name: Renault Group Android Automotive SDK and Vehicle Properties
  slug: rg-android-automotive-sdk
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/renault-group/well-known/renault-group-media-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/renault-group-media-security.txt
- group: agent
  href: https://artifacts.apis.io/renault-group/well-known/renault-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/renault-group-well-known.yml
- group: other
  href: https://artifacts.apis.io/renault-group/hosts/renault-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/renault-group-hosts.yml
- group: auth
  href: https://artifacts.apis.io/renault-group/security/renault-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/renault-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.renaultgroup.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.renaultgroup.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.renaultgroup.com/en/develop/rg-sdk/rg-android-sdk-setup/1-overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.renaultgroup.com/en/design/ui-guide-for-automotive-app/1-introduction
- group: start
  title: ''
  type: Sandbox
  url: https://developer.renaultgroup.com/en/develop/rg-emulators
- group: company
  title: ''
  type: Partner
  url: https://developer.renaultgroup.com/en/be-partner/developer-journey
- group: company
  title: ''
  type: Newsroom
  url: https://media.renaultgroup.com/
- group: other
  title: ''
  type: Leadership
  url: https://www.renaultgroup.com/en/group/leadership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.renaultgroup.com/en/footer/legal-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.renault.fr/donnees-personnelles.html
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://assets.renaultgroup.com/mcp
  - status: 200
    url: https://www.renaultgroup.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Renault Group is the French automotive group behind the Renault, Dacia, Alpine and Mobilize brands. Its developer program, the Renault Group Developer Portal (developer.renaultgroup.com, launched May 2025), targets in-vehicle app development on the openR and openR evo infotainment platforms built on Android Automotive OS with Google Automotive Services: an RG Android SDK setup guide, public Android Automotive emulators for Renault 5 and Renault Scenic, UX/UI guidelines for driver-distraction-safe partner apps, and partner-only Android vehicle properties (onboard vehicle APIs and signals) for the software-defined-vehicle platform. No public web/REST API contract is published; vehicle access is onboard via the SDK.'
image: https://assets.renaultgroup.com/uploads/2025/06/Logo-RG-yoast.png
layout: provider
modified: '2026-10-13'
name: Renault Group
nav: Providers
network: true
overview: 'Renault Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Android Automotive, In-Vehicle Apps, and SDK.


  Renault Group''s developer surface includes getting-started guide, documentation, sandbox, and 11 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/renault-group/renault-group-2026-11-03T142149.png
security:
- kind: domain-security
  name: Renault Group Domain Security
  slug: renault-group-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: renault-group
tags:
- Company
- Automotive
- Android Automotive
- In-Vehicle Apps
- SDK
- Software Defined Vehicle
- Vehicle Signals
website: https://www.renaultgroup.com/en/
---
