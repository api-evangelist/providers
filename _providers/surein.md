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
  href: https://artifacts.apis.io/surein/hosts/surein-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surein-hosts.yml
- group: other
  href: https://artifacts.apis.io/surein/vendors/surein-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surein-vendors.yml
- group: auth
  href: https://artifacts.apis.io/surein/security/surein-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surein-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.surein.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.surein.de/
- group: start
  title: ''
  type: SignUp
  url: https://app.surein.de/
- group: docs
  title: ''
  type: Documentation
  url: https://surein.de/en/
- group: operate
  title: ''
  type: Support
  url: https://surein.de/contact/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://surein.de/en/legal/terms-and-conditions
coverage:
  checked: '2026-10-29'
  detail: Documentation site returns HTML pages with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://app.surein.de/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: SureIn provides commercial insurance solutions, helping businesses manage risk with expert support. The platform offers various insurance products such as vehicle, gastronomy, agency, and artist coverage. Users can report damage, access contact support, and log in to manage policies via the app.surein.de portal. The company emphasizes risk control and expert guidance, positioning itself as a trusted partner for commercial insurance needs.
image: https://framerusercontent.com/assets/0SPlApHdMlZ2MKFQrKdc43XLfM.png
layout: provider
modified: '2026-10-29'
name: SureIn
nav: Providers
network: true
overview: 'SureIn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Commercial, Risk Management, Germany, and B2B.


  SureIn''s developer surface includes signup flow, documentation, support, and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 7.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/surein/surein-2026-11-03T144110.png
security:
- kind: domain-security
  name: Surein Domain Security
  slug: surein-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: surein
tags:
- Insurance
- Commercial
- Risk Management
- Germany
- B2B
website: https://www.surein.de/
---
