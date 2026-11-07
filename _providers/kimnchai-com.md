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
  href: https://artifacts.apis.io/kimnchai-com/vendors/kimnchai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kimnchai-com-vendors.yml
- group: other
  href: https://artifacts.apis.io/kimnchai-com/hosts/kimnchai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kimnchai-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kimnchai.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://mulddae.kimnchai.com/blog
- group: company
  title: ''
  type: Website
  url: https://kimnchai.com/
- group: auth
  href: https://artifacts.apis.io/kimnchai-com/security/kimnchai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kimnchai-com-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: All attempted OpenAPI spec URLs on kimnchai.com and its subdomains returned 404, and no documentation host was found.
  evidence:
  - status: 404
    url: https://kimnchai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: kimnchai.com appears to be a personal Korean website that aggregates public data related to fishing tides, water temperature, and wave information, providing tools such as mulddae.kimnchai.com for tide forecasts and learnk.kimnchai.com for personal notes. The site does not present itself as a corporate entity, nor does it publish an API, developer portal, or any formal documentation. Consequently, there is insufficient evidence to confirm the existence of a company behind the domain, and no official website or API endpoints can be verified.
layout: provider
modified: '2026-10-29'
name: kimnchai-com
nav: Providers
network: true
overview: 'kimnchai-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Site, Data Aggregation, Fishing, Korean, and Public Data.


  kimnchai-com''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kimnchai-com/kimnchai-com-2026-11-03T134412.png
security:
- kind: domain-security
  name: Kimnchai Com Domain Security
  slug: kimnchai-com-domain-security
  summary_line: TLSv1.3
slug: kimnchai-com
tags:
- Personal Site
- Data Aggregation
- Fishing
- Korean
- Public Data
website: https://kimnchai.com/
---
